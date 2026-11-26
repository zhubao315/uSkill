interface LoadingProps {
  label?: string;
  rows?: number;
  compact?: boolean;
}

export function Loading({ label = 'Loading data from the local service…', rows = 4, compact = false }: LoadingProps) {
  return (
    <div
      className={`loading-block${compact ? ' loading-block--compact' : ''}`}
      role="status"
      aria-live="polite"
    >
      <div className="loading-line">
        <span className="spinner" aria-hidden="true" />
        <span>{label}</span>
      </div>
      {!compact && (
        <div className="skeleton-list" aria-hidden="true">
          {Array.from({ length: rows }, (_, index) => (
            <div className="skeleton-row" key={index}>
              <span style={{ width: `${38 - (index % 3) * 7}%` }} />
              <span style={{ width: `${22 + (index % 4) * 6}%` }} />
              <span style={{ width: '14%' }} />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
