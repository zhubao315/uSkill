import { useCallback, useEffect, useState, type DependencyList } from 'react';
import { ApiError, errorMessage } from '../api/client';

export interface AsyncState<T> {
  data: T | null;
  error: Error | null;
  loading: boolean;
}

/**
 * Minimal request lifecycle. The caller owns `deps`; `load` is intentionally
 * excluded so inline arrow functions don't retrigger on every render.
 */
export function useAsync<T>(load: () => Promise<T>, deps: DependencyList) {
  const [state, setState] = useState<AsyncState<T>>({
    data: null,
    error: null,
    loading: true,
  });
  const [revision, setRevision] = useState(0);

  useEffect(() => {
    let active = true;
    setState((previous) => ({ ...previous, loading: true, error: null }));
    load()
      .then((data) => {
        if (active) setState({ data, error: null, loading: false });
      })
      .catch((error: unknown) => {
        if (!active) return;
        setState({
          data: null,
          error: error instanceof Error ? error : new ApiError(errorMessage(error), 0, ''),
          loading: false,
        });
      });
    return () => {
      active = false;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [...deps, revision]);

  const refetch = useCallback(() => setRevision((value) => value + 1), []);

  return { ...state, refetch };
}
