import { useLocation } from 'react-router-dom';
import { MenuIcon } from './Icons';
import { ThemeToggle } from './ThemeToggle';
import type { Theme } from '../hooks/useTheme';

interface TopBarProps {
  theme: Theme;
  onToggleTheme: () => void;
  onMenu: () => void;
  navOpen: boolean;
}

function pageLabel(pathname: string): string {
  if (pathname.startsWith('/skills/')) return 'Skill detail';
  if (pathname.startsWith('/skills')) return 'My Skills';
  if (pathname.startsWith('/agents')) return 'Agent Hub';
  if (pathname.startsWith('/runs')) return 'Run History';
  return 'Dashboard';
}

export function TopBar({ theme, onToggleTheme, onMenu, navOpen }: TopBarProps) {
  const { pathname } = useLocation();

  return (
    <header className="topbar">
      <button
        type="button"
        className="icon-btn topbar-menu"
        onClick={onMenu}
        aria-label={navOpen ? 'Close navigation' : 'Open navigation'}
        aria-expanded={navOpen}
      >
        <MenuIcon />
      </button>
      <div className="topbar-trail">
        <span>uSkill</span>
        <span className="trail-separator" aria-hidden="true">
          /
        </span>
        <strong>{pageLabel(pathname)}</strong>
      </div>
      <div className="topbar-actions">
        <span className="endpoint-chip" title="Dev proxy target for /api">
          <span className="endpoint-dot" aria-hidden="true" />
          LOCAL API · :8765
        </span>
        <ThemeToggle theme={theme} onToggle={onToggleTheme} />
      </div>
    </header>
  );
}
