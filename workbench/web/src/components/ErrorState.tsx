import { errorMessage } from '../api/client';
import { AlertIcon } from './Icons';

interface ErrorStateProps {
  error: unknown;
  title?: string;
  onRetry?: () => void;
  compact?: boolean;
}

export function ErrorState({
  error,
  title = 'Could not load data',
  onRetry,
  compact = false,
}: ErrorStateProps) {
  return (
    <div
      className={`state-block state-block--error${compact ? ' state-block--compact' : ''}`}
      role="alert"
      aria-live="assertive"
    >
      <div className="state-glyph" aria-hidden="true">
        <AlertIcon size={34} />
      </div>
      <h3>{title}</h3>
      <p className="error-message">{errorMessage(error)}</p>
      <p className="state-hint">No placeholder data is shown when a request fails.</p>
      {onRetry && (
        <div className="state-action">
          <button type="button" className="btn btn--primary" onClick={onRetry}>
            Retry request
          </button>
        </div>
      )}
    </div>
  );
}
