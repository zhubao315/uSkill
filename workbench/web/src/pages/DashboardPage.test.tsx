import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { DashboardPage } from './DashboardPage';

const payloads: Record<string, unknown> = {
  '/api/health': { status: 'ok', version: '3.0.0' },
  '/api/skills': {
    skills: [
      {
        skill_id: 'uskill-atomic-translate-v1-0-0',
        name: 'Translate Text',
        description: 'Translates text',
        format: 'agent-skill',
        path: 'skills/translate/SKILL.md',
        category: 'BUILD',
        domain: 'language',
        tags: ['i18n'],
        content_hash: 'abc123',
        version: '1.0.0',
        source: 'local',
        source_url: '',
        license: '',
        compatible_agents: ['codex'],
        lifecycle_status: 'validated',
        eval_status: 'unknown',
        risk_level: 'L0',
        trust_status: 'untrusted',
        discovered_at: '2026-11-26T00:00:00Z',
        issues: [],
      },
    ],
    health: { skills: 1, by_format: { 'agent-skill': 1 }, broken: [], duplicates: {}, ok: true },
  },
  '/api/agents': [
    {
      agent: 'codex',
      detected: true,
      locations: [{ scope: 'user', path: '/home/u/.agents/skills', priority: 10 }],
      installed: [{ name: 'Translate Text', path: '/home/u/.agents/skills/translate' }],
    },
  ],
  '/api/runs': [
    {
      run_id: 'run-abc123',
      status: 'COMPLETED',
      started_at: '2026-11-26T00:00:00Z',
      finished_at: '2026-11-26T00:00:05Z',
      skill_id: 'uskill-atomic-translate-v1-0-0',
    },
  ],
};

function stubFetch(handler: (path: string) => Promise<unknown>) {
  vi.stubGlobal(
    'fetch',
    vi.fn(async (input: RequestInfo | URL) => {
      const body = await handler(String(input));
      return {
        ok: true,
        status: 200,
        text: async () => JSON.stringify(body),
      } as unknown as Response;
    }),
  );
}

afterEach(() => {
  vi.unstubAllGlobals();
});

describe('DashboardPage', () => {
  it('renders values returned by the real API contract', async () => {
    stubFetch(async (path) => payloads[path]);

    render(
      <MemoryRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
        <DashboardPage />
      </MemoryRouter>,
    );

    expect(await screen.findByText('Translate Text')).toBeInTheDocument();
    expect(screen.getByText(/version 3\.0\.0/)).toBeInTheDocument();
    expect(screen.getByText('run-abc123')).toBeInTheDocument();
    expect(screen.getByText('DETECTED')).toBeInTheDocument();
    expect(screen.getByText('Skills indexed')).toBeInTheDocument();
  });

  it('shows an honest error when the service is unavailable', async () => {
    stubFetch(async () => {
      throw new Error('network down');
    });

    render(
      <MemoryRouter future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
        <DashboardPage />
      </MemoryRouter>,
    );

    expect(await screen.findByText('Service unreachable')).toBeInTheDocument();
    expect(screen.getAllByText('Could not load skills').length).toBeGreaterThan(0);
    expect(screen.queryByText('Translate Text')).not.toBeInTheDocument();
  });
});
