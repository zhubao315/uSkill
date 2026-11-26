import type {
  AgentInfo,
  HealthResponse,
  InstallPlan,
  InstallPreviewRequest,
  RunRecord,
  RunSummary,
  SkillQuery,
  SkillRecord,
  SkillsResponse,
} from '../types';

/** Injected by the local bootstrap script; never stored by this app. */
declare global {
  interface Window {
    __USKILL_TOKEN__?: string;
  }
}

export class ApiError extends Error {
  readonly status: number;
  readonly path: string;
  readonly cause?: unknown;

  constructor(message: string, status: number, path: string, cause?: unknown) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.path = path;
    this.cause = cause;
  }
}

function getToken(): string {
  if (typeof window === 'undefined') return '';
  return window.__USKILL_TOKEN__ || '';
}

function buildQuery(params: Record<string, string | undefined>): string {
  const search = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    const trimmed = value?.trim();
    if (trimmed) search.set(key, trimmed);
  }
  const encoded = search.toString();
  return encoded ? `?${encoded}` : '';
}

function detailFromBody(text: string, status: number): string {
  if (!text) return `Request failed with HTTP ${status}.`;
  try {
    const body: unknown = JSON.parse(text);
    if (typeof body === 'string') return body;
    if (body && typeof body === 'object') {
      const record = body as Record<string, unknown>;
      const detail = record.detail;
      if (typeof detail === 'string') return detail;
      if (Array.isArray(detail)) {
        const parts = detail.map((item: unknown) => {
          if (item && typeof item === 'object') {
            const issue = item as Record<string, unknown>;
            const loc = Array.isArray(issue.loc) ? issue.loc.join('.') : 'field';
            return `${loc}: ${String(issue.msg ?? 'invalid value')}`;
          }
          return String(item);
        });
        return parts.join('; ');
      }
      for (const key of ['message', 'error']) {
        if (typeof record[key] === 'string') return record[key] as string;
      }
    }
  } catch {
    // Plain-text error body — fall through.
  }
  return text.slice(0, 300);
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const token = getToken();
  const headers = new Headers(init?.headers);
  headers.set('Accept', 'application/json');
  if (init?.body !== undefined) headers.set('Content-Type', 'application/json');
  if (token) headers.set('Authorization', `Bearer ${token}`);

  let response: Response;
  try {
    response = await fetch(path, { ...init, headers });
  } catch (cause) {
    throw new ApiError(
      'Cannot reach the local uSkill service. Check that the Workbench server is running.',
      0,
      path,
      cause,
    );
  }

  let text = '';
  try {
    text = await response.text();
  } catch (cause) {
    throw new ApiError('Could not read the service response.', response.status, path, cause);
  }

  if (!response.ok) {
    throw new ApiError(detailFromBody(text, response.status), response.status, path);
  }
  if (!text) {
    throw new ApiError('The service returned an empty response.', response.status, path);
  }
  try {
    return JSON.parse(text) as T;
  } catch (cause) {
    throw new ApiError('The service returned malformed JSON.', response.status, path, cause);
  }
}

export const api = {
  health: () => request<HealthResponse>('/api/health'),

  skills: (query: SkillQuery = {}) =>
    request<SkillsResponse>(
      `/api/skills${buildQuery({
        query: query.query,
        category: query.category,
        source_type: query.source_type,
        status: query.status,
      })}`,
    ),

  skill: (skillId: string) =>
    request<SkillRecord>(`/api/skills/${encodeURIComponent(skillId)}`),

  agents: () => request<AgentInfo[]>('/api/agents'),

  previewInstall: (body: InstallPreviewRequest) =>
    request<InstallPlan>('/api/install/preview', {
      method: 'POST',
      body: JSON.stringify(body),
    }),

  runs: () => request<RunSummary[]>('/api/runs'),

  run: (runId: string) => request<RunRecord>(`/api/runs/${encodeURIComponent(runId)}`),
};

export const errorMessage = (error: unknown): string =>
  error instanceof Error ? error.message : String(error);
