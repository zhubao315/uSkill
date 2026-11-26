import { useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../api/client';
import { DataTable, type Column } from '../components/DataTable';
import { EmptyState } from '../components/EmptyState';
import { ErrorState } from '../components/ErrorState';
import { Loading } from '../components/Loading';
import { PageHeader } from '../components/PageHeader';
import { StatusBadge, toneForFormat, toneForLifecycle, toneForRisk } from '../components/StatusBadge';
import { useAsync } from '../hooks/useAsync';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import { CATEGORIES, LIFECYCLE_STATUSES, SOURCE_TYPES, type SkillRecord } from '../types';
import { shortHash } from '../utils/format';

const columns: Column<SkillRecord>[] = [
  {
    key: 'name',
    header: 'Name / Skill ID',
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
    key: 'description',
    header: 'Description',
    className: 'col-description',
    render: (skill) => (
      <span className="cell-clamp" title={skill.description || ''}>
        {skill.description || '—'}
      </span>
    ),
  },
  {
    key: 'format',
    header: 'Format',
    render: (skill) => (
      <StatusBadge tone={toneForFormat(skill.format)}>{skill.format || '—'}</StatusBadge>
    ),
  },
  {
    key: 'risk',
    header: 'Risk',
    render: (skill) => <StatusBadge tone={toneForRisk(skill.risk_level)}>{skill.risk_level || '—'}</StatusBadge>,
  },
  {
    key: 'lifecycle',
    header: 'Lifecycle',
    render: (skill) => (
      <StatusBadge tone={toneForLifecycle(skill.lifecycle_status)}>
        {skill.lifecycle_status || '—'}
      </StatusBadge>
    ),
  },
  { key: 'category', header: 'Category', render: (skill) => skill.category || '—' },
  {
    key: 'path',
    header: 'Path',
    className: 'col-path',
    render: (skill) => (
      <span className="mono cell-truncate" title={skill.path}>
        {skill.path || '—'}
      </span>
    ),
  },
  {
    key: 'hash',
    header: 'Content hash',
    className: 'col-hash',
    render: (skill) => (
      <span className="mono" title={skill.content_hash || ''}>
        {shortHash(skill.content_hash)}
      </span>
    ),
  },
];

export function SkillsPage() {
  const [query, setQuery] = useState('');
  const [category, setCategory] = useState('');
  const [sourceType, setSourceType] = useState('');
  const [status, setStatus] = useState('');
  const debouncedQuery = useDebouncedValue(query, 250);

  const { data, error, loading, refetch } = useAsync(
    () => api.skills({ query: debouncedQuery, category, source_type: sourceType, status }),
    [debouncedQuery, category, sourceType, status],
  );

  const filtersActive = Boolean(query || category || sourceType || status);
  const reset = () => {
    setQuery('');
    setCategory('');
    setSourceType('');
    setStatus('');
  };

  const rows = data?.skills ?? [];

  return (
    <div className="page">
      <PageHeader
        eyebrow="REGISTRY / ALL RECORDS"
        title="My Skills"
        description="Live view of the filesystem-backed registry. Search runs across name, description, tags, domain, source, agent, risk and format."
        actions={
          <div className="header-count">
            <span className="mono">{rows.length}</span>
            <span>record(s) returned</span>
          </div>
        }
      />

      <section className="panel filter-panel" aria-label="Skill filters">
        <div className="filter-grid">
          <div className="form-field search-field">
            <label htmlFor="skill-search">Search</label>
            <input
              id="skill-search"
              type="search"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Name, tag, domain, hash…"
              autoComplete="off"
            />
          </div>
          <div className="form-field">
            <label htmlFor="skill-category">Category</label>
            <select
              id="skill-category"
              value={category}
              onChange={(event) => setCategory(event.target.value)}
            >
              <option value="">All categories</option>
              {CATEGORIES.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </div>
          <div className="form-field">
            <label htmlFor="skill-source">Source type</label>
            <select
              id="skill-source"
              value={sourceType}
              onChange={(event) => setSourceType(event.target.value)}
            >
              <option value="">All formats</option>
              {SOURCE_TYPES.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </div>
          <div className="form-field">
            <label htmlFor="skill-status">Status</label>
            <select
              id="skill-status"
              value={status}
              onChange={(event) => setStatus(event.target.value)}
            >
              <option value="">All statuses</option>
              {LIFECYCLE_STATUSES.map((value) => (
                <option key={value} value={value}>
                  {value}
                </option>
              ))}
            </select>
          </div>
        </div>
        <div className="filter-foot">
          <span className="cell-sub">
            {filtersActive ? 'Filters applied locally to the query sent to /api/skills.' : 'No filters applied.'}
          </span>
          <button type="button" className="btn btn--ghost btn--small" onClick={reset} disabled={!filtersActive}>
            Clear filters
          </button>
        </div>
      </section>

      <section className="panel" aria-label="Skill records">
        {loading && !data ? (
          <Loading label="Querying the skill registry…" rows={6} />
        ) : error ? (
          <ErrorState error={error} title="Skill query failed" onRetry={refetch} />
        ) : (
          <DataTable
            columns={columns}
            rows={rows}
            rowKey={(skill) => `${skill.skill_id}:${skill.path}`}
            caption="Skill records from the local registry"
            empty={
              <EmptyState
                title={filtersActive ? 'No skills match these filters' : 'No skills in the registry'}
                description={
                  filtersActive
                    ? 'Try a different search term or clear the filters to see all records.'
                    : 'Add a skill file on disk, then reload this page.'
                }
                action={
                  filtersActive ? (
                    <button type="button" className="btn btn--primary" onClick={reset}>
                      Clear filters
                    </button>
                  ) : (
                    <button type="button" className="btn btn--primary" onClick={refetch}>
                      Reload
                    </button>
                  )
                }
              />
            }
          />
        )}
      </section>

      {data?.health && !data.health.ok && (
        <aside className="inline-notice" role="status">
          Registry reports {data.health.broken.length} broken file(s) and{' '}
          {Object.keys(data.health.duplicates).length} duplicate hash(es). Records above are still
          the real registry output.
        </aside>
      )}
    </div>
  );
}
