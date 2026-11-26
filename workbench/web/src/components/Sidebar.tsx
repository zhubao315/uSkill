import { NavLink } from 'react-router-dom';
import { CloseIcon, CubeIcon, GridIcon, PlugIcon, PulseIcon } from './Icons';
import type { ComponentType } from 'react';
import type { SVGProps } from 'react';

type IconComponent = ComponentType<SVGProps<SVGSVGElement> & { size?: number }>;

interface NavEntry {
  to: string;
  label: string;
  hint: string;
  icon: IconComponent;
  end?: boolean;
}

const NAV: NavEntry[] = [
  { to: '/', label: 'Dashboard', hint: 'Overview', icon: GridIcon, end: true },
  { to: '/skills', label: 'My Skills', hint: 'Registry', icon: CubeIcon },
  { to: '/agents', label: 'Agent Hub', hint: 'Install targets', icon: PlugIcon },
  { to: '/runs', label: 'Run History', hint: 'Execution log', icon: PulseIcon },
];

interface SidebarProps {
  open: boolean;
  onClose: () => void;
}

export function Sidebar({ open, onClose }: SidebarProps) {
  return (
    <aside className={`sidebar${open ? ' sidebar--open' : ''}`} aria-label="Primary navigation">
      <div className="sidebar-brand">
        <span className="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 32 32" width="28" height="28">
            <path d="M5 6h22v6H18v14h-4V12H5z" fill="var(--accent-blue)" />
            <circle cx="24" cy="23" r="4" fill="var(--brand-orange)" />
          </svg>
        </span>
        <span className="brand-wordmark">
          <strong>uSkill</strong>
          <small>WORKBENCH 3.0</small>
        </span>
        <button
          type="button"
          className="icon-btn sidebar-close"
          onClick={onClose}
          aria-label="Close navigation"
        >
          <CloseIcon size={18} />
        </button>
      </div>

      <nav className="sidebar-nav" aria-label="Workspace">
        <p className="nav-label">WORKSPACE</p>
        <ul>
          {NAV.map(({ to, label, hint, icon: Icon, end }) => (
            <li key={to}>
              <NavLink
                to={to}
                end={end}
                onClick={onClose}
                className={({ isActive }) => `nav-item${isActive ? ' is-active' : ''}`}
              >
                <Icon size={19} />
                <span className="nav-item-text">
                  <span className="nav-item-label">{label}</span>
                  <span className="nav-item-hint">{hint}</span>
                </span>
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>

      <div className="sidebar-foot">
        <p className="foot-label">LOCAL-FIRST</p>
        <p>Filesystem is the source of truth. No remote data, no sample records.</p>
      </div>
    </aside>
  );
}
