#!/usr/bin/env node
/** Generate a static, publishable catalog page for the synced private skills. */
import { promises as fs } from 'node:fs';
import path from 'node:path';

const ROOT = path.resolve(process.env.OUT_DIR || 'docs/skills-from-vault');
const index = JSON.parse(await fs.readFile(path.join(path.dirname(ROOT), 'vault-skills-index.json'), 'utf8'));

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const byCat = new Map();
for (const s of index.skills) {
  if (!byCat.has(s.category)) byCat.set(s.category, []);
  byCat.get(s.category).push(s);
}

const sections = [...byCat.entries()].sort((a, b) => a[0].localeCompare(b[0])).map(([cat, skills]) => `
## ${esc(cat)} <small>(${skills.length})</small>

| 技能 | 版本 | 来源 SHA | 正文 |
|---|---|---|---|
${skills.map((s) => `| [${esc(s.title)}](/uSkill/skills-from-vault/${esc(s.path)}/SKILL/) | ${esc(s.version || '—')} | \`${esc(s.source_sha.slice(0, 10))}\` | [原文](/uSkill/skills-from-vault/${esc(s.path)}/references/source/) |`).join('\n')}
`).join('\n');

const md = `---
title: 个人技能库（私库同步）
description: 从私有 Obsidian 仓库同步的 ${index.count} 个个人技能 · 自动生成
---

# 个人技能库 · ${index.count} 个技能

> 本页由 \`scripts/sync_private_skills.mjs\` 自动生成，来源：\`${esc(index.source)}\`。
> 生成时间：${esc(index.generated_at)}。所有条目是**个人技能资产**，标记为 \`untrusted\`；脚本永不自动执行。

<div class="vault-filter">
  <input id="vault-search" type="search" placeholder="搜索技能名称…" />
  <span id="vault-count">${index.count} 个技能</span>
</div>

${sections}

<script>
(function () {
  const input = document.getElementById('vault-search');
  const rows = Array.from(document.querySelectorAll('#vault-table tbody tr, table tbody tr'));
  const count = document.getElementById('vault-count');
  input && input.addEventListener('input', () => {
    const q = input.value.trim().toLowerCase();
    let shown = 0;
    rows.forEach((r) => { const hit = r.textContent.toLowerCase().includes(q); r.hidden = !!q && !hit; if (hit) shown++; });
    if (count) count.textContent = (q ? shown : rows.length) + ' 个技能';
  });
})();
</script>
`;

const outDir = path.resolve(process.env.PAGES_DIR || 'docs/generated');
await fs.mkdir(outDir, { recursive: true });
const target = path.join(outDir, 'vault-skills.md');
await fs.writeFile(target, md, 'utf8');
console.log(`[pages] wrote ${target}`);
