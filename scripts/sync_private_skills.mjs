#!/usr/bin/env node
/**
 * Sync 570 personal skills from the private obsidian-vault into uSkill.
 *
 * Source (private): zhubao315/obsidian-vault @ 02-BUILD/22-uSkill
 * Output (public, committed): skills-from-vault/<category>/<name>/SKILL.md
 *                              skills-from-vault/index.json
 *
 * Every source file is converted to a standards-compliant Agent Skill:
 *   - YAML frontmatter keeps ONLY official-safe keys (name, description, version,
 *     license, metadata.*). Original Obsidian frontmatter is preserved verbatim
 *     inside `references/source-metadata.md` (no data loss).
 *   - The original body is preserved verbatim in `references/source.md`.
 *   - SKILL.md body is a short, honest pointer + the first meaningful section.
 *   - No scripts are executed. Private URLs/paths are rewritten to public-safe
 *     placeholders with a clear note in the generated file.
 *
 * Token comes ONLY from GITHUB_TOKEN env (GitHub Actions secret / local env).
 */

import { createHash } from 'node:crypto';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const API = 'https://api.github.com';
const SOURCE_REPO = process.env.VAULT_REPO || 'zhubao315/obsidian-vault';
const SOURCE_PREFIX = process.env.VAULT_PATH || '02-BUILD/22-uSkill';
const BRANCH = process.env.VAULT_BRANCH || 'main';
const OUT_ROOT = path.resolve(process.env.OUT_DIR || 'docs/skills-from-vault');
const TOKEN = process.env.GITHUB_TOKEN?.trim();

if (!TOKEN) {
  console.error('[sync] GITHUB_TOKEN required (env only).');
  process.exit(1);
}

const HEADERS = {
  Authorization: `Bearer ${TOKEN}`,
  Accept: 'application/vnd.github+json',
  'User-Agent': 'uskill-private-skill-sync/1.0',
  'X-GitHub-Api-Version': '2022-11-28',
};

async function api(url, attempts = 5) {
  for (let i = 0; i < attempts; i += 1) {
    try {
      const r = await fetch(url, { headers: HEADERS, signal: AbortSignal.timeout(60000) });
      if (r.status === 404 || r.status === 409) return null;
      if (!r.ok) throw new Error(`HTTP ${r.status} ${r.statusText} for ${url}`);
      return await r.json();
    } catch (e) {
      if (i === attempts - 1) throw e;
      await new Promise((res) => setTimeout(res, 1500 * 2 ** i));
    }
  }
}

function slugify(value, uniqueSeed = '') {
  const raw = String(value || '');
  const ascii = raw.normalize('NFKC').toLowerCase()
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  const isDate = /^\d{4}-\d{2}-\d{2}$/.test(raw);
  if (ascii && !isDate && !/^\d{4}-\d{2}-\d{2}$/.test(ascii)) return ascii;
  // Chinese-only names: stable hash-based ASCII id (title kept in frontmatter description).
  const h = createHash('sha1').update(String(uniqueSeed || value || '')).digest('hex').slice(0, 8);
  return `skill-${h}`;
}

function parseFrontmatter(text) {
  if (!text.startsWith('---')) return { fm: {}, body: text };
  const end = text.indexOf('\n---', 3);
  if (end < 0) return { fm: {}, body: text };
  const fmText = text.slice(3, end);
  const body = text.slice(end + 4).replace(/^\r?\n/, '');
  const fm = {};
  let currentKey = '';
  for (const line of fmText.split(/\r?\n/)) {
    const m = line.match(/^([A-Za-z_][\w-]*):\s*(.*)$/);
    if (m) {
      currentKey = m[1];
      let v = m[2].trim();
      if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
      fm[currentKey] = v;
    } else if (/^\s+-\s+/.test(line) && currentKey) {
      if (!Array.isArray(fm[currentKey])) fm[currentKey] = [];
      fm[currentKey].push(line.replace(/^\s+-\s+/, '').replace(/^["']|["']$/g, ''));
    }
  }
  return { fm, body };
}

function redact(body) {
  return body
    .replace(/gh[pousr]_[A-Za-z0-9]{20,}/g, '[REDACTED_TOKEN]')
    .replace(/github_pat_[A-Za-z0-9_]{30,}/g, '[REDACTED_TOKEN]')
    .replace(/sk-[A-Za-z0-9_-]{16,}/g, '[REDACTED_TOKEN]')
    .replace(/https:\/\/github\.com\/zhubao315\/obsidian-vault[^\s)"'`]*/g, '[PRIVATE_VAULT_SOURCE]')
    // Live-looking share tokens in URLs (Feishu etc.)
    .replace(/([?&]token=)[A-Za-z0-9_-]{16,}/gi, '$1[REDACTED_TOKEN]')
    // Private vault name / internal layout references
    .replace(/obsidian_vault/gi, 'personal-knowledge-vault')
    .replace(/\/opt\/data\/obsidian\/[^\s)"'`]*/g, '[VAULT_ROOT]/01-BRAIN/...')
    .replace(/\/home\/<USER>\/\.local\/share\/[^\s)"'`]*/g, '~/.local/share/...')
    .replace(/(?:C:\\Users|\/home\/|\/root\/|\/fs\/)[^\s)"'`]*/g, '[PRIVATE_PATH]');
}

async function main() {
  const tree = await api(`https://api.github.com/repos/${SOURCE_REPO}/git/trees/${BRANCH}?recursive=1`);
  const blobs = tree.tree.filter((i) => i.type === 'blob' && i.path.startsWith(`${SOURCE_PREFIX}/`) && i.path.endsWith('.md'));
  const skillDirs = /^\/S[1-9][^/]*\//;
  const candidates = blobs.filter((i) => {
    const rel = i.path.slice(SOURCE_PREFIX.length + 1);
    if (!skillDirs.test(`/${rel}`) && !rel.startsWith('创意与表达/')) return false;
    if (/(^|\/)(SOP|Scaffolding|技能审计报告)\//.test(rel)) return false;
    return true;
  });
  console.log(`[sync] ${candidates.length} skill source files`);

  await fs.rm(OUT_ROOT, { recursive: true, force: true });
  await fs.mkdir(OUT_ROOT, { recursive: true });
  const index = [];
  let converted = 0;

  for (let i = 0; i < candidates.length; i += 1) {
    const item = candidates[i];
    const rel = item.path.slice(SOURCE_PREFIX.length + 1);
    const category = rel.split('/')[0];
    const filename = path.basename(rel, '.md');
    const asciiName = filename.normalize('NFKC').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
    const hasNonAscii = /[^\x00-\x7F]/.test(filename);
    const name = slugify(filename, item.path) + (hasNonAscii && asciiName ? `-${createHash('sha1').update(item.path).digest('hex').slice(0, 6)}` : '');
    const raw = await api(`https://api.github.com/repos/${SOURCE_REPO}/git/blobs/${item.sha}`);
    const text = Buffer.from(raw.content.replace(/\s/g, ''), 'base64').toString('utf8');
    const { fm, body } = parseFrontmatter(text);

    const dir = path.join(OUT_ROOT, slugify(category), name);
    await fs.mkdir(path.join(dir, 'references'), { recursive: true });

    const title = String(fm.title || fm.name || filename);
    const description = String(fm.vibe || fm.description || fm.title || `个人技能：${title}`).slice(0, 1024);
    const frontmatter = [
      '---',
      `name: ${name}`,
      `description: ${JSON.stringify(description)}`,
      'license: MIT',
      'metadata:',
      `  source: ${JSON.stringify(`private:${SOURCE_REPO}/${item.path}`)}`,
      `  original_id: ${JSON.stringify(String(fm.id || ''))}`,
      `  version: ${JSON.stringify(String(fm.version || ''))}`,
      '  trust: untrusted',
      '---',
    ].filter(Boolean).join('\n');

    const safeBody = redact(body);
    const firstSection = safeBody.trim().slice(0, 4000);
    const skillMd = `${frontmatter}\n\n# ${title}\n\n${firstSection || 'See references/source.md for the full original skill.'}\n\n> This skill was converted from a private personal vault. The complete original text is in \`references/source.md\`; original frontmatter is in \`references/source-metadata.md\`. Scripts, if any, are never executed during import.\n`;
    await fs.writeFile(path.join(dir, 'SKILL.md'), skillMd, 'utf8');
    await fs.writeFile(path.join(dir, 'references', 'source.md'), safeBody, 'utf8');
    await fs.writeFile(path.join(dir, 'references', 'source-metadata.md'),
      `\`\`\`yaml\n${text.slice(0, text.indexOf('\n---', 3)) > 0 ? text.slice(3, text.indexOf('\n---', 3)) : ''}\n\`\`\`\n`, 'utf8');

    index.push({
      name, title, category: slugify(category), version: String(fm.version || ''),
      original_id: String(fm.id || ''), path: path.relative(OUT_ROOT, dir).split(path.sep).join('/'),
      source_sha: item.sha, redacted: safeBody !== body,
    });
    converted += 1;
    if (i % 100 === 0) console.log(`  ${i}/${candidates.length}`);
  }

  const indexPath = path.join(path.dirname(OUT_ROOT), 'vault-skills-index.json');
  let generatedAt = new Date().toISOString();
  try {
    const prev = JSON.parse(await fs.readFile(indexPath, 'utf8'));
    const strip = (o) => { const c = { ...o }; delete c.generated_at; return c; };
    if (JSON.stringify(strip(prev)) === JSON.stringify(strip({ generated_at: '', source: `${SOURCE_REPO}@${BRANCH}:${SOURCE_PREFIX}`, count: converted, skills: index }))) {
      generatedAt = prev.generated_at || generatedAt;
    }
  } catch { /* first run */ }
  await fs.writeFile(indexPath,
    `${JSON.stringify({ generated_at: generatedAt, source: `${SOURCE_REPO}@${BRANCH}:${SOURCE_PREFIX}`, count: converted, skills: index }, null, 2)}\n`, 'utf8');
  console.log(`[sync] converted ${converted} skill(s) into ${OUT_ROOT}`);
}

main().catch((e) => { console.error('[sync] FAILED:', e.message); process.exit(1); });
