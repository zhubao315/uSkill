import { Link, useParams } from 'react-router-dom';
import { api } from '../api/client';
import { ErrorState } from '../components/ErrorState';
import { InstallPanel } from '../components/InstallPanel';
import { JsonView } from '../components/JsonView';
import { Loading } from '../components/Loading';
import { PageHeader } from '../components/PageHeader';
import { RecordFields } from '../components/RecordFields';
import { StatusBadge, toneForFormat, toneForLifecycle, toneForRisk } from '../components/StatusBadge';
import { ArrowLeftIcon } from '../components/Icons';
import { useAsync } from '../hooks/useAsync';

export function SkillDetailPage() {
  const { skillId = '' } = useParams();
  const { data, error, loading, refetch } = useAsync(
    () =>
      skillId
        ? api.skill(skillId)
        : Promise.reject(new Error('No skill ID was provided in the URL.')),
    [skillId],
  );

  return (
    <div className="page">
      <PageHeader
        eyebrow="REGISTRY / RECORD"
        title={data?.name ?? (loading ? 'Loading skill…' : 'Skill detail')}
        description={data?.description || 'Metadata for this skill is read from the local registry.'}
        actions={
          <Link to="/skills" className="btn btn--ghost">
            <ArrowLeftIcon size={17} />
            Back to skills
          </Link>
        }
      />

      {loading && !data ? (
        <section className="panel">
          <Loading label={`Loading ${skillId}…`} rows={6} />
        </section>
      ) : error ? (
        <section className="panel">
          <ErrorState error={error} title="Could not load this skill" onRetry={refetch} />
        </section>
      ) : data ? (
        <>
          <div className="detail-badges">
            <StatusBadge tone={toneForFormat(data.format)}>{data.format || 'unknown format'}</StatusBadge>
            <StatusBadge tone={toneForRisk(data.risk_level)}>risk {data.risk_level || '—'}</StatusBadge>
            <StatusBadge tone={toneForLifecycle(data.lifecycle_status)}>
              {data.lifecycle_status || 'unknown status'}
            </StatusBadge>
            <StatusBadge tone={data.trust_status === 'trusted' ? 'green' : 'orange'}>
              {data.trust_status || 'untrusted'}
            </StatusBadge>
          </div>

          <div className="detail-grid">
            <div className="detail-stack">
              <section className="panel" aria-labelledby="fields-heading">
                <div className="panel-head">
                  <div>
                    <p className="panel-eyebrow">METADATA</p>
                    <h2 id="fields-heading">Record fields</h2>
                  </div>
                  <span className="mono cell-sub">{data.skill_id}</span>
                </div>
                <RecordFields record={data} />
              </section>
              <JsonView value={data} label="Raw skill record" />
            </div>
            <InstallPanel skill={data} />
          </div>
        </>
      ) : null}
    </div>
  );
}
