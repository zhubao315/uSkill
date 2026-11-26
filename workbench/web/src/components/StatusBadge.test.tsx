import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { StatusBadge, toneForRisk, toneForRunStatus } from './StatusBadge';
import { DataTable } from './DataTable';

describe('StatusBadge', () => {
  it('renders its label, tone class and title', () => {
    render(
      <StatusBadge tone="orange" title="elevated risk">
        L3
      </StatusBadge>,
    );
    const badge = screen.getByText('L3');
    expect(badge).toHaveClass('badge', 'badge--orange');
    expect(badge).toHaveAttribute('title', 'elevated risk');
  });

  it('maps backend states to tones', () => {
    expect(toneForRisk('L4')).toBe('red');
    expect(toneForRunStatus('FAILED')).toBe('red');
    expect(toneForRunStatus('COMPLETED')).toBe('green');
  });
});

describe('DataTable', () => {
  it('renders rows and falls back to an empty state', () => {
    const rows = [{ id: 'a', label: 'Alpha' }];
    const columns = [
      { key: 'id', header: 'ID', render: (row: (typeof rows)[number]) => row.id },
      { key: 'label', header: 'Label', render: (row: (typeof rows)[number]) => row.label },
    ];

    const { rerender } = render(
      <DataTable rows={rows} columns={columns} rowKey={(row) => row.id} caption="Test rows" />,
    );
    expect(screen.getByRole('table', { name: 'Test rows' })).toBeInTheDocument();
    expect(screen.getByText('Alpha')).toBeInTheDocument();

    rerender(
      <DataTable
        rows={[]}
        columns={columns}
        rowKey={(row) => row.id}
        caption="Test rows"
        empty={<p>There are no rows.</p>}
      />,
    );
    expect(screen.queryByRole('table')).not.toBeInTheDocument();
    expect(screen.getByText('There are no rows.')).toBeInTheDocument();
  });
});
