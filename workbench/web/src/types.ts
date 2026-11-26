/**
 * Wire types for the local Workbench service.
 *
 * These mirror the Python sources rather than inventing new entities:
 *   - SkillRecord / registry health: core/uskills/registry.py (SkillRegistryV3)
 *   - agents / install plans:        core/uskills/agents_hub.py
 *   - runs / steps:                  core/uskills/runtime/state.py (RunRecord)
 *
 * The service is allowed to evolve, so list-ish fields are kept tolerant
 * (unions with string) and rendering code normalises them. Unknown data is
 * never replaced with sample values.
 */

export interface HealthResponse {
  status: string;
  version: string;
}

export interface SkillRecord {
  skill_id: string;
  name: string;
  description: string;
  format: string;
  path: string;
  category: string;
  domain: string;
  tags: string[];
  content_hash: string;
  version: string;
  source: string;
  source_url: string;
  license: string;
  compatible_agents: string[];
  lifecycle_status: string;
  eval_status: string;
  risk_level: string;
  trust_status: string;
  discovered_at: string;
  issues: string[];
}

export interface RegistryIssue {
  path: string;
  error: string;
}

export interface RegistryHealth {
  skills: number;
  by_format: Record<string, number>;
  broken: RegistryIssue[];
  duplicates: Record<string, string[]>;
  ok: boolean;
}

export interface SkillsResponse {
  skills: SkillRecord[];
  health: RegistryHealth;
}

export interface SkillQuery {
  query?: string;
  category?: string;
  source_type?: string;
  status?: string;
}

/** A skill location may be a full object or a plain path string. */
export type AgentLocation =
  | { scope?: string; path: string; priority?: number }
  | string;

/** An installed entry may be a full object or a plain skill name. */
export type InstalledSkill =
  | { name: string; path?: string; content_hash?: string; source?: string }
  | string;

export interface AgentInfo {
  agent: string;
  detected: boolean;
  locations: AgentLocation[];
  installed: InstalledSkill[];
}

export interface InstallAction {
  kind: string;
  source: string;
  target: string;
  reason: string;
}

export interface InstallPlan {
  target_agent: string;
  scope: string;
  skill_name: string;
  source_path: string;
  actions: InstallAction[];
  conflicts: string[];
  risks: string[];
  rollback: string[];
  approved: boolean;
}

export interface InstallPreviewRequest {
  skill_path: string;
  agent: string;
  scope: 'user' | 'project';
}

export interface RunSummary {
  run_id: string;
  status: string;
  started_at: string | null;
  finished_at: string | null;
  skill_id: string;
}

export interface StepRecord {
  step_id: string;
  kind: string;
  via?: string;
  status: string;
  input?: unknown;
  output?: unknown;
  error?: string | null;
  started_at?: string | null;
  finished_at?: string | null;
  attempts?: number;
  retry_errors?: string[];
  usage?: Record<string, unknown> | null;
  execution_time?: number | null;
}

export interface RunRecord {
  run_id: string;
  skill_id: string;
  status: string;
  inputs: unknown;
  outputs: unknown;
  steps: StepRecord[];
  events: Array<Record<string, unknown>>;
  error: string | null;
  started_at: string | null;
  finished_at: string | null;
  usage: Record<string, unknown>;
  execution_time: number | null;
  result: unknown;
}

export const CATEGORIES = ['BUILD', 'THINK', 'MEASURE', 'CREATE'] as const;
export const SOURCE_TYPES = [
  'legacy-yaml',
  'manifest-v2',
  'agent-skill',
  'agent-skill+manifest',
] as const;
export const LIFECYCLE_STATUSES = [
  'draft',
  'validated',
  'reviewed',
  'published',
  'deprecated',
] as const;
/** Mirrors agents_hub.all_adapters() in core/uskills/agents_hub.py. */
export const KNOWN_AGENTS = ['codex', 'claude-code', 'opencode'] as const;
