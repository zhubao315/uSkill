interface MetricProps {
  label: string;
  value: string;
  source: string;
  available: boolean;
  note?: string;
}

export function Metric({ label, value, source, available, note }: MetricProps) {
  return (
    <div className={`metric${available ? '' : ' metric--unavailable'}`}>
      <p className="metric-label">{label}</p>
      <p className="metric-value">{available ? value : '—'}</p>
      <p className="metric-source">
        {source}
        {note ? ` · ${note}` : ''}
      </p>
    </div>
  );
}
