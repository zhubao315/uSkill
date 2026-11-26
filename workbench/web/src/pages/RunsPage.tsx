import { useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { DataTable, type Column } from '../components/DataTable';
import { EmptyState } from '../components/EmptyState';
import { ErrorState } from '../components/ErrorState';
import { ChevronIcon } from '../components/Icons';
import { Loading } from '../components/Loading';
import { PageHeader } from '../components/PageHeader';
import { RunDetail } from '../components/RunDetail';
import { StatusBadge, toneForRunStatus } from '../components/StatusBadge';
import { useAsync } from '../hooks/useAsync';
import type { RunSummary } from '../types';
import { formatDuration, formatTimestamp } from '../utils/format';

function detailId(runId: string): string {
  return `run-detail-${runId.replace(/[^a-zA-Z0-9_-]/g, '_')}`;
}

export function RunsPage() {
  const [expanded, setExpanded] = useState<string | null>(null);
  const { data, error, loading, refetch } = useAsync(() => api.runs(), []);

  const toggle = (runId: string) => {
    setExpanded((current) => (current === runId ? null : runId));
  };

  const columns: Column<RunSummary>[] = [
    {
      key: 'run_id',
      header: 'Run ID',
      render: (run) => (
        <button
          type="button"
          className="link-button mono run-toggle"
          onClick={() => toggle(run.run_id)}
          aria-expanded={expanded === run.run_id}
          aria-controls={detailId(run.run_id)}
        >
          <ChevronIcon
            size={16}
            className={expanded === run.run_id ? 'chevron chevron--open' : 'chevron'}
          />
          {run.run_id}
        </button>
      ),
    },
    {
      key: 'skill_id',
      header: 'Skill ID',
      render: (run) => (
        <Link to={`/skills/${encodeURIComponent(run.skill_id)}`} className="mono text-link cell-truncate">
          {run.skill_id}
        </Link>
      ),
    },
    {
      key: 'status',
      header: 'Status',
      render: (run) => <StatusBadge tone={toneForRunStatus(run.status)}>{run.status}</StatusBadge>,
    },
    { key: 'started', header: 'Started', render: (run) => formatTimestamp(run.started_at) },
    {
      key: 'duration',
      header: 'Duration',
      render: (run) => formatDuration(run.started_at, run.finished_at),
    },
  ];

  return (
    <div className="page">
      <PageHeader
        eyebrow="RUNTIME / HISTORY"
        title="Run History"
        description="Checkpointed runs read from the local RunStore. Select a run ID to load its full record, steps and events."
        actions={
          data && (
            <div className="header-count">
              <span className="mono">{data.length}</span>
              <span>run(s) on disk</span>
            </div>
          )
        }
      />

      <section className="panel" aria-label="Recorded runs">
        {loading && !data ? (
          <Loading label="Reading run history…" rows={5} />
        ) : error ? (
          <ErrorState error={error} title="Could not load run history" onRetry={refetch} />
        ) : (
          <DataTable
            columns={columns}
            rows={data ?? []}
            rowKey={(run) => run.run_id}
            caption="Run history from the local service"
            isExpanded={(run) => expanded === run.run_id}
            expandedContent={(run) => (
              <div id={detailId(run.run_id)}>
                <RunDetail runId={run.run_id} />
              </div>
            )}
            empty={
              <EmptyState
                title="No runs recorded"
                description="The RunStore has no run files yet. Execute a skill to create one."
                action={
                  <button type="button" className="btn btn--primary" onClick={refetch}>
                    Reload history
                  </button>
                }
              />
            }
          />
        )}
      </section>
    </div>
  );
}
