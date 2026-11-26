import { useState } from 'react';
import { Outlet } from 'react-router-dom';
import { Sidebar } from './Sidebar';
import { TopBar } from './TopBar';
import { useTheme } from '../hooks/useTheme';

export function Layout() {
  const { theme, toggle } = useTheme();
  const [navOpen, setNavOpen] = useState(false);

  return (
    <div className="app-shell">
      <a className="skip-link" href="#main-content">
        Skip to content
      </a>
      <Sidebar open={navOpen} onClose={() => setNavOpen(false)} />
      {navOpen && (
        <button
          type="button"
          className="nav-scrim"
          aria-label="Close navigation"
          onClick={() => setNavOpen(false)}
        />
      )}
      <div className="app-main">
        <TopBar
          theme={theme}
          onToggleTheme={toggle}
          onMenu={() => setNavOpen((value) => !value)}
          navOpen={navOpen}
        />
        <main id="main-content" className="app-content" tabIndex={-1}>
          <Outlet />
        </main>
      </div>
    </div>
  );
}
