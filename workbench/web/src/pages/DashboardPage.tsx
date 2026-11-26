import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { DataTable, type Column } from '../components/DataTable';
import { EmptyState } from '../components/EmptyState';
import { ErrorState } from '../components/ErrorState';
import { Loading } from '../components/Loading';
import { Metric } from '../components/Metric';
import { PageHeader } from '../components/PageHeader';
import { StatusBadge, toneForFormat, toneForRisk, toneForRunStatus } from '../components/StatusBadge';
import { useAsync } from '../hooks/useAsync';
import type { AgentInfo, RunSummary, SkillRecord } from '../types';
import { countLabel, formatTimestamp } from '../utils/format';

const skillColumns: Column<SkillRecord>[] = [
  {
    key: 'name',
    header: 'Skill',
    render: (skill) => (
      <div className="cell-stack">
        <Link to={`/skills/${encodeURIComponent(skill.skill_id)}`} className="text-link">
          {skill.name || skill.skill_id}
        </Link>
        <span className="cell-sub mono">{skill.skill_id}</span>
      </div>
    ),
  },
  {
    key: 'format',
    header: 'Format',
    render: (skill) => (
      <StatusBadge tone={toneForFormat(skill.format)}>{skill.format || '—'}</StatusBadge>
    ),
  },
  { key: 'category', header: 'Category', render: (skill) => skill.category || '—' },
  {
    key: 'risk',
    header: 'Risk',
    render: (skill) => <StatusBadge tone={toneForRisk(skill.risk_level)}>{skill.risk_level || '—'}</StatusBadge>,
  },
];

const runColumns: Column<RunSummary>[] = [
  {
    key: 'run_id',
    header: 'Run ID',
    render: (run) => <Link to="/runs" className="mono text-link">{run.run_id}</Link>,
  },
  { key: 'skill_id', header: 'Skill ID', render: (run) => <span className="mono cell-truncate">{run.skill_id}</span> },
  {
    key: 'status',
    header: 'Status',
    render: (run) => <StatusBadge tone={toneForRunStatus(run.status)}>{run.status}</StatusBadge>,
  },
  { key: 'started', header: 'Started', render: (run) => formatTimestamp(run.started_at) },
];

function AgentRow({ agent }: { agent: AgentInfo }) {
  return (
    <li className="compact-row">
      <div>
        <strong>{agent.agent}</strong>
        <span className="cell-sub">
          {countLabel(agent.installed?.length ?? 0, 'installed skill')}
        </span>
      </div>
      <StatusBadge tone={agent.detected ? 'green' : 'neutral'}>
        {agent.detected ? 'DETECTED' : 'NOT FOUND'}
      </StatusBadge>
    </li>
  );
}

export function DashboardPage() {
  const health = useAsync(() => api.health(), []);
  const skills = useAsync(() => api.skills(), []);
  const agents = useAsync(() => api.agents(), []);
  const runs = useAsync(() => api.runs(), []);

  const registry = skills.data?.health;
  const skillCount = registry?.skills ?? skills.data?.skills.length;
  const installedCount = agents.data?.reduce((total, agent) => total + (agent.installed?.length ?? 0), 0);
  const detectedCount = agents.data?.filter((agent) => agent.detected).length;
  const issueCount = registry ? registry.broken.length + Object.keys(registry.duplicates).length : undefined;

  return (
    <div className="page">
      <PageHeader
        eyebrow="OVERVIEW / LOCAL WORKBENCH"
        title="Skill operations at a glance"
        description="Every number below comes from the local service on this machine. Failed requests show an error instead of a placeholder."
        actions={
          <Link to="/skills" className="btn btn--primary">
            Open registry
          </Link>
        }
      />

      <section className="service-banner" aria-label="Service status">
        <div>
          <p className="panel-eyebrow">LOCAL SERVICE</p>
          {health.loading && !health.data ? (
            <Loading label="Checking service health…" compact />
          ) : health.error ? (
            <ErrorState error={health.error} title="Service unreachable" onRetry={health.refetch} compact />
          ) : (
            <div className="service-readout">
              <StatusBadge tone={health.data?.status?.toLowerCase() === 'ok' ? 'green' : 'orange'}>
                {health.data?.status ?? 'UNKNOWN'}
              </StatusBadge>
              <span className="mono">version {health.data?.version ?? '—'}</span>
              <span className="cell-sub">GET /api/health</span>
            </div>
          )}
        </div>
        <span className="service-note">Read-only console · filesystem is the source of truth</span>
      </section>

      <section className="metrics-row" aria-label="Registry and runtime summary">
        <Metric
          label="Skills indexed"
          value={String(skillCount ?? 0)}
          source="/api/skills · health.skills"
          available={skillCount !== undefined}
        />
        <Metric
          label="Registry integrity"
          value={issueCount === 0 ? 'OK' : `${issueCount ?? 0} issue(s)`}
          source="/api/skills · health"
          available={issueCount !== undefined}
        />
        <Metric
          label="Installed skills"
          value={String(installedCount ?? 0)}
          source="/api/agents · installed[]"
          available={installedCount !== undefined}
        />
        <Metric
          label="Agents detected"
          value={`${detectedCount ?? 0} / ${agents.data?.length ?? 0}`}
          source="/api/agents · detected"
          available={detectedCount !== undefined}
        />
        <Metric
          label="Recorded runs"
          value={String(runs.data?.length ?? 0)}
          source="/api/runs"
          available={runs.data !== null}
        />
      </section>

      <div className="dashboard-grid">
        <section className="panel" aria-labelledby="inventory-heading">
          <div className="panel-head">
            <div>
              <p className="panel-eyebrow">REGISTRY</p>
              <h2 id="inventory-heading">Skill inventory</h2>
            </div>
            <Link to="/skills" className="text-link">
              View all →
            </Link>
          </div>
          {skills.loading && !skills.data ? (
            <Loading rows={4} />
          ) : skills.error ? (
            <ErrorState error={skills.error} title="Could not load skills" onRetry={skills.refetch} />
          ) : (
            <DataTable
              columns={skillColumns}
              rows={skills.data?.skills.slice(0, 5) ?? []}
              rowKey={(skill) => skill.skill_id}
              caption="First five skills in the registry"
              empty={
                <EmptyState
                  title="No skills indexed yet"
                  description="The registry returned no records. Add a skill on disk and reload."
                  compact
                />
              }
            />
          )}
        </section>

        <section className="panel" aria-labelledby="integrity-heading">
          <div className="panel-head">
            <div>
              <p className="panel-eyebrow">HEALTH</p>
              <h2 id="integrity-heading">Registry integrity</h2>
            </div>
            {registry && (
              <StatusBadge tone={registry.ok ? 'green' : 'red'}>
                {registry.ok ? 'OK' : 'ISSUES'}
              </StatusBadge>
            )}
          </div>
          {skills.loading && !registry ? (
            <Loading label="Reading registry health…" compact />
          ) : skills.error || !registry ? (
            <ErrorState
              error={skills.error ?? new Error('The service did not include registry health.')}
              title="Health data unavailable"
              onRetry={skills.refetch}
              compact
            />
          ) : (
            <div className="integrity-body">
              <dl className="format-list">
                {Object.entries(registry.by_format).map(([format, count]) => (
                  <div key={format}>
                    <dt>{format}</dt>
                    <dd className="mono">{count}</dd>
                  </div>
                ))}
                {Object.keys(registry.by_format).length === 0 && (
                  <div>
                    <dt className="muted">No formats reported</dt>
                    <dd>—</dd>
                  </div>
                )}
              </dl>
              <div className="integrity-notes">
                <p>
                  <span className="muted">Broken files</span>{' '}
                  <strong className="mono">{registry.broken.length}</strong>
                </p>
                <p>
                  <span className="muted">Duplicate hashes</span>{' '}
                  <strong className="mono">{Object.keys(registry.duplicates).length}</strong>
                </p>
              </div>
            </div>
          )}
        </section>

        <section className="panel" aria-labelledby="agents-heading">
          <div className="panel-head">
            <div>
              <p className="panel-eyebrow">CONNECTORS</p>
              <h2 id="agents-heading">Agent detection</h2>
            </div>
            <Link to="/agents" className="text-link">
              Open hub →
            </Link>
          </div>
          {agents.loading && !agents.data ? (
            <Loading label="Detecting local agents…" compact />
          ) : agents.error ? (
            <ErrorState error={agents.error} title="Could not detect agents" onRetry={agents.refetch} compact />
          ) : (
            <ul className="compact-list">
              {(agents.data ?? []).map((agent) => (
                <AgentRow key={agent.agent} agent={agent} />
              ))}
              {(agents.data ?? []).length === 0 && (
                <li>
                  <EmptyState
                    title="No agents reported"
                    description="The connector list is empty on this machine."
                    compact
                  />
                </li>
              )}
            </ul>
          )}
        </section>

        <section className="panel" aria-labelledby="runs-heading">
          <div className="panel-head">
            <div>
              <p className="panel-eyebrow">RUNTIME</p>
              <h2 id="runs-heading">Recent runs</h2>
            </div>
            <Link to="/runs" className="text-link">
              Full history →
            </Link>
          </div>
          {runs.loading && !runs.data ? (
            <Loading rows={3} />
          ) : runs.error ? (
            <ErrorState error={runs.error} title="Could not load runs" onRetry={runs.refetch} compact />
          ) : (
            <DataTable
              columns={runColumns}
              rows={runs.data?.slice(0, 5) ?? []}
              rowKey={(run) => run.run_id}
              caption="Five most recent runs returned by the service"
              empty={
                <EmptyState
                  title="No runs recorded"
                  description="Execute a skill to populate the runtime history."
                  compact
                />
              }
            />
          )}
        </section>
      </div>
    </div>
  );
}
