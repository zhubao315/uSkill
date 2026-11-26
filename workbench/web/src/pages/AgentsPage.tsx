import { api } from '../api/client';
import { EmptyState } from '../components/EmptyState';
import { ErrorState } from '../components/ErrorState';
import { Loading } from '../components/Loading';
import { PageHeader } from '../components/PageHeader';
import { StatusBadge } from '../components/StatusBadge';
import { useAsync } from '../hooks/useAsync';
import type { AgentInfo, AgentLocation, InstalledSkill } from '../types';
import { countLabel } from '../utils/format';

function locationPath(location: AgentLocation): string {
  return typeof location === 'string' ? location : location.path;
}

function locationScope(location: AgentLocation): string {
  return typeof location === 'string' ? '—' : (location.scope ?? '—');
}

function locationPriority(location: AgentLocation): string {
  return typeof location === 'string' ? '—' : String(location.priority ?? '—');
}

function installedName(skill: InstalledSkill): string {
  return typeof skill === 'string' ? skill : skill.name;
}

function installedDetail(skill: InstalledSkill): string {
  if (typeof skill === 'string') return '';
  return [skill.source, skill.content_hash].filter(Boolean).join(' · ');
}

function AgentCard({ agent }: { agent: AgentInfo }) {
  return (
    <article className="panel agent-card">
      <div className="panel-head">
        <div>
          <p className="panel-eyebrow">AGENT TARGET</p>
          <h2 className="mono">{agent.agent}</h2>
        </div>
        <StatusBadge tone={agent.detected ? 'green' : 'neutral'}>
          {agent.detected ? 'DETECTED' : 'NOT FOUND'}
        </StatusBadge>
      </div>

      <p className="agent-summary">
        {countLabel(agent.installed?.length ?? 0, 'installed skill')} ·{' '}
        {countLabel(agent.locations?.length ?? 0, 'skill location')}
      </p>

      <div className="agent-section">
        <h3>Skill locations</h3>
        {(agent.locations?.length ?? 0) > 0 ? (
          <ul className="location-list">
            {agent.locations.map((location, index) => (
              <li key={`${locationPath(location)}-${index}`}>
                <div>
                  <StatusBadge tone="blue">{locationScope(location)}</StatusBadge>
                  <span className="mono wrap">{locationPath(location)}</span>
                </div>
                <span className="cell-sub">priority {locationPriority(location)}</span>
              </li>
            ))}
          </ul>
        ) : (
          <p className="muted">No skill locations reported.</p>
        )}
      </div>

      <div className="agent-section">
        <h3>Installed skills</h3>
        {(agent.installed?.length ?? 0) > 0 ? (
          <ul className="installed-list">
            {agent.installed.map((skill, index) => (
              <li key={`${installedName(skill)}-${index}`}>
                <strong>{installedName(skill)}</strong>
                {installedDetail(skill) && <span className="cell-sub mono">{installedDetail(skill)}</span>}
              </li>
            ))}
          </ul>
        ) : (
          <p className="muted">No installed skills detected in scanned locations.</p>
        )}
      </div>
    </article>
  );
}

export function AgentsPage() {
  const { data, error, loading, refetch } = useAsync(() => api.agents(), []);

  return (
    <div className="page">
      <PageHeader
        eyebrow="CONNECTORS / INSTALL TARGETS"
        title="Agent Install Hub"
        description="Detection and skill directories reported by the local adapters. Every path below is read from the service; nothing is installed from this page."
        actions={
          data && (
            <div className="header-count">
              <span className="mono">{data.filter((agent) => agent.detected).length}</span>
              <span>detected of {data.length}</span>
            </div>
          )
        }
      />

      {loading && !data ? (
        <section className="panel">
          <Loading label="Scanning for agent targets…" rows={4} />
        </section>
      ) : error ? (
        <section className="panel">
          <ErrorState error={error} title="Could not load agents" onRetry={refetch} />
        </section>
      ) : !data || data.length === 0 ? (
        <section className="panel">
          <EmptyState
            title="No agents reported"
            description="The local service returned an empty connector list. Check the agent adapters on this machine."
            action={
              <button type="button" className="btn btn--primary" onClick={refetch}>
                Rescan
              </button>
            }
          />
        </section>
      ) : (
        <div className="agent-grid">
          {data.map((agent) => (
            <AgentCard key={agent.agent} agent={agent} />
          ))}
        </div>
      )}
    </div>
  );
}
