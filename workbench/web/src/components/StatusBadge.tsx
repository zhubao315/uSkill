import type { ReactNode } from 'react';

export type Tone = 'blue' | 'teal' | 'orange' | 'green' | 'red' | 'neutral' | 'violet';

interface StatusBadgeProps {
  tone?: Tone;
  children: ReactNode;
  title?: string;
}

export function StatusBadge({ tone = 'neutral', children, title }: StatusBadgeProps) {
  return (
    <span className={`badge badge--${tone}`} title={title}>
      {children}
    </span>
  );
}

export function toneForRisk(level?: string): Tone {
  switch ((level ?? '').toUpperCase()) {
    case 'L0':
      return 'neutral';
    case 'L1':
      return 'blue';
    case 'L2':
      return 'teal';
    case 'L3':
      return 'orange';
    case 'L4':
      return 'red';
    default:
      return 'neutral';
  }
}

export function toneForLifecycle(status?: string): Tone {
  switch ((status ?? '').toLowerCase()) {
    case 'validated':
      return 'blue';
    case 'reviewed':
      return 'teal';
    case 'published':
      return 'green';
    case 'deprecated':
      return 'orange';
    default:
      return 'neutral';
  }
}

export function toneForRunStatus(status?: string): Tone {
  switch ((status ?? '').toUpperCase()) {
    case 'COMPLETED':
      return 'green';
    case 'FAILED':
    case 'INTERRUPTED':
      return 'red';
    case 'RUNNING':
      return 'blue';
    case 'WAITING_APPROVAL':
    case 'RETRYING':
      return 'orange';
    case 'SKIPPED':
    case 'CANCELLED':
      return 'neutral';
    default:
      return 'violet';
  }
}

export function toneForFormat(format?: string): Tone {
  const value = (format ?? '').toLowerCase();
  if (value.includes('manifest')) return 'teal';
  if (value.includes('agent-skill')) return 'violet';
  if (value.includes('legacy')) return 'blue';
  return 'neutral';
}
