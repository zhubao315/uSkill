import type { ReactNode } from 'react';
import type { SkillRecord } from '../types';
import { formatTimestamp } from '../utils/format';
import { ExternalIcon } from './Icons';
import { StatusBadge, toneForFormat, toneForLifecycle, toneForRisk } from './StatusBadge';

interface Field {
  label: string;
  value: ReactNode;
  mono?: boolean;
  wide?: boolean;
}

const dash = <span className="muted">—</span>;

function listOrDash(values: string[] | undefined, tone?: 'blue' | 'teal') {
  if (!values || values.length === 0) return dash;
  return (
    <span className="inline-list">
      {values.map((value) => (
        <StatusBadge key={value} tone={tone ?? 'neutral'}>
          {value}
        </StatusBadge>
      ))}
    </span>
  );
}

export function RecordFields({ record }: { record: SkillRecord }) {
  const fields: Field[] = [
    { label: 'Skill ID', value: record.skill_id, mono: true, wide: true },
    { label: 'Name', value: record.name },
    { label: 'Description', value: record.description || dash, wide: true },
    {
      label: 'Format',
      value: <StatusBadge tone={toneForFormat(record.format)}>{record.format || dash}</StatusBadge>,
    },
    { label: 'Category', value: record.category || dash },
    { label: 'Domain', value: record.domain || dash },
    { label: 'Tags', value: listOrDash(record.tags, 'blue'), wide: true },
    { label: 'Content hash', value: record.content_hash || dash, mono: true, wide: true },
    { label: 'Version', value: record.version || dash, mono: true },
    { label: 'Source', value: record.source || dash },
    {
      label: 'Source URL',
      value: record.source_url ? (
        <a href={record.source_url} target="_blank" rel="noopener noreferrer" className="text-link">
          {record.source_url}
          <ExternalIcon size={14} />
        </a>
      ) : (
        dash
      ),
      wide: true,
    },
    { label: 'License', value: record.license || dash },
    { label: 'Compatible agents', value: listOrDash(record.compatible_agents, 'teal'), wide: true },
    {
      label: 'Lifecycle',
      value: (
        <StatusBadge tone={toneForLifecycle(record.lifecycle_status)}>
          {record.lifecycle_status || dash}
        </StatusBadge>
      ),
    },
    { label: 'Eval status', value: record.eval_status || dash },
    {
      label: 'Risk level',
      value: <StatusBadge tone={toneForRisk(record.risk_level)}>{record.risk_level || dash}</StatusBadge>,
    },
    { label: 'Trust status', value: record.trust_status || dash },
    { label: 'Discovered at', value: formatTimestamp(record.discovered_at) },
    {
      label: 'Issues',
      value:
        record.issues && record.issues.length > 0 ? (
          <ul className="issue-list">
            {record.issues.map((issue, index) => (
              <li key={`${index}-${issue}`}>{issue}</li>
            ))}
          </ul>
        ) : (
          <span className="muted">none reported</span>
        ),
      wide: true,
    },
  ];

  return (
    <dl className="field-grid">
      {fields.map((field) => (
        <div className={`field${field.wide ? ' field--wide' : ''}`} key={field.label}>
          <dt>{field.label}</dt>
          <dd className={field.mono ? 'mono' : undefined}>{field.value}</dd>
        </div>
      ))}
    </dl>
  );
}
