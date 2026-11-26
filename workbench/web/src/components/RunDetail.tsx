import { useAsync } from '../hooks/useAsync';
import { api } from '../api/client';
import { type StepRecord } from '../types';
import { formatDuration, formatTimestamp } from '../utils/format';
import { DataTable, type Column } from './DataTable';
import { EmptyState } from './EmptyState';
import { ErrorState } from './ErrorState';
import { JsonView } from './JsonView';
import { Loading } from './Loading';
import { StatusBadge, toneForRunStatus } from './StatusBadge';

const stepColumns: Column<StepRecord>[] = [
  {
    key: 'step_id',
    header: 'Step',
    render: (step) => <span className="mono">{step.step_id}</span>,
  },
  { key: 'kind', header: 'Kind', render: (step) => step.kind },
  {
    key: 'status',
    header: 'Status',
    render: (step) => (
      <StatusBadge tone={toneForRunStatus(step.status)}>{step.status}</StatusBadge>
    ),
  },
  { key: 'attempts', header: 'Attempts', render: (step) => String(step.attempts ?? 0) },
  {
    key: 'time',
    header: 'Execution',
    render: (step) => formatDuration(step.started_at, step.finished_at),
  },
  {
    key: 'error',
    header: 'Error',
    render: (step) => (step.error ? <span className="error-text">{step.error}</span> : '—'),
  },
];

export function RunDetail({ runId }: { runId: string }) {
  const { data, error, loading, refetch } = useAsync(() => api.run(runId), [runId]);

  if (loading) return <Loading label={`Loading run ${runId}…`} compact />;
  if (error) return <ErrorState error={error} title="Could not load run detail" onRetry={refetch} compact />;
  if (!data) return <EmptyState title="No run record" description="The service returned no record for this run." compact />;

  return (
    <div className="run-detail">
      <div className="run-detail-head">
        <div>
          <p className="panel-eyebrow">RUN DETAIL</p>
          <h3 className="mono">{data.run_id}</h3>
        </div>
        <StatusBadge tone={toneForRunStatus(data.status)}>{data.status}</StatusBadge>
      </div>

      <dl className="run-facts">
        <div>
          <dt>Skill ID</dt>
          <dd className="mono">{data.skill_id}</dd>
        </div>
        <div>
          <dt>Started</dt>
          <dd>{formatTimestamp(data.started_at)}</dd>
        </div>
        <div>
          <dt>Finished</dt>
          <dd>{formatTimestamp(data.finished_at)}</dd>
        </div>
        <div>
          <dt>Duration</dt>
          <dd>{formatDuration(data.started_at, data.finished_at)}</dd>
        </div>
        <div>
          <dt>Steps</dt>
          <dd>{data.steps.length}</dd>
        </div>
        <div>
          <dt>Events</dt>
          <dd>{data.events.length}</dd>
        </div>
      </dl>

      {data.error && (
        <div className="inline-error" role="alert">
          <div>
            <strong>Run error</strong>
            <p>{data.error}</p>
          </div>
        </div>
      )}

      <div className="run-detail-section">
        <h4>Steps</h4>
        <DataTable
          columns={stepColumns}
          rows={data.steps}
          rowKey={(step) => step.step_id}
          caption={`Steps for run ${data.run_id}`}
          empty={<p className="muted">No steps were recorded for this run.</p>}
        />
      </div>

      {data.events.length > 0 && (
        <div className="run-detail-section">
          <h4>Events ({data.events.length})</h4>
          <ol className="event-list">
            {data.events.map((event, index) => (
              <li key={`${index}-${String(event.event ?? 'event')}`}>
                <span className="mono">{formatTimestamp(String(event.time ?? ''))}</span>{' '}
                <span>{String(event.event ?? 'event')}</span>
              </li>
            ))}
          </ol>
        </div>
      )}

      <JsonView value={data} label="Full run record" />
    </div>
  );
}
