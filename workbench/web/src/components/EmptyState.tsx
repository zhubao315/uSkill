import type { ReactNode } from 'react';

interface EmptyStateProps {
  title: string;
  description: string;
  action?: ReactNode;
  compact?: boolean;
}

export function EmptyState({ title, description, action, compact = false }: EmptyStateProps) {
  return (
    <div className={`state-block${compact ? ' state-block--compact' : ''}`} role="status">
      <div className="state-glyph" aria-hidden="true">
        <svg viewBox="0 0 48 48" width="36" height="36" fill="none" stroke="currentColor" strokeWidth="1.6">
          <rect x="8" y="10" width="32" height="28" rx="3" />
          <path d="M8 18h32M15 26h9M15 32h16" />
        </svg>
      </div>
      <h3>{title}</h3>
      <p>{description}</p>
      {action && <div className="state-action">{action}</div>}
    </div>
  );
}
