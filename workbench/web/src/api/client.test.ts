import { afterEach, describe, expect, it, vi } from 'vitest';
import { ApiError, api } from './client';

function jsonResponse(body: unknown, status = 200): Response {
  return {
    ok: status >= 200 && status < 300,
    status,
    text: async () => (typeof body === 'string' ? body : JSON.stringify(body)),
  } as unknown as Response;
}

function setToken(token: string | undefined) {
  if (token === undefined) delete (window as unknown as Record<string, unknown>).__USKILL_TOKEN__;
  else (window as unknown as Record<string, unknown>).__USKILL_TOKEN__ = token;
}

afterEach(() => {
  setToken(undefined);
  vi.unstubAllGlobals();
});

describe('api client', () => {
  it('sends the pairing token and parses the JSON body', async () => {
    setToken('pair-123');
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse({ status: 'ok', version: '3.0.0' }));
    vi.stubGlobal('fetch', fetchMock);

    const result = await api.health();

    expect(result).toEqual({ status: 'ok', version: '3.0.0' });
    expect(fetchMock).toHaveBeenCalledTimes(1);
    const [path, init] = fetchMock.mock.calls[0] as [string, RequestInit];
    expect(path).toBe('/api/health');
    expect((init.headers as Headers).get('Authorization')).toBe('Bearer pair-123');
    expect((init.headers as Headers).get('Accept')).toBe('application/json');
  });

  it('raises an ApiError carrying status, path and service detail', async () => {
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(jsonResponse({ detail: 'Skill not found' }, 404)));

    await expect(api.skill('missing')).rejects.toMatchObject({
      name: 'ApiError',
      status: 404,
      path: '/api/skills/missing',
      message: 'Skill not found',
    });
    await expect(api.skill('missing')).rejects.toBeInstanceOf(ApiError);
  });

  it('wraps a failed network call in a status-0 ApiError', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new TypeError('Failed to fetch')));

    await expect(api.runs()).rejects.toMatchObject({
      status: 0,
      path: '/api/runs',
      message: expect.stringContaining('Cannot reach the local uSkill service'),
    });
  });

  it('encodes query parameters and posts a JSON install preview body', async () => {
    const fetchMock = vi.fn().mockResolvedValue(jsonResponse([]));
    vi.stubGlobal('fetch', fetchMock);

    await api.skills({ query: 'a b', category: 'BUILD' });
    expect(fetchMock.mock.calls[0][0]).toBe('/api/skills?query=a+b&category=BUILD');

    await api.previewInstall({ skill_path: 'skills/demo/SKILL.md', agent: 'codex', scope: 'user' });
    const [path, init] = fetchMock.mock.calls[1] as [string, RequestInit];
    expect(path).toBe('/api/install/preview');
    expect(init.method).toBe('POST');
    expect((init.headers as Headers).get('Content-Type')).toBe('application/json');
    expect(JSON.parse(init.body as string)).toEqual({
      skill_path: 'skills/demo/SKILL.md',
      agent: 'codex',
      scope: 'user',
    });
    expect((init.headers as Headers).get('Authorization')).toBeNull();
  });
});
