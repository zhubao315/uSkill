import { useState, type FormEvent } from 'react';
import { api, errorMessage } from '../api/client';
import { KNOWN_AGENTS, type InstallPlan, type SkillRecord } from '../types';
import { StatusBadge } from './StatusBadge';

interface InstallPanelProps {
  skill: SkillRecord;
}

function PlanList({ title, items, tone }: { title: string; items: string[]; tone?: string }) {
  return (
    <div className="plan-section">
      <h4>{title}</h4>
      {items.length === 0 ? (
        <p className="muted">None.</p>
      ) : (
        <ul className={tone ? `plan-list plan-list--${tone}` : 'plan-list'}>
          {items.map((item, index) => (
            <li key={`${index}-${item}`}>{item}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export function InstallPanel({ skill }: InstallPanelProps) {
  const [agent, setAgent] = useState<string>(KNOWN_AGENTS[0]);
  const [scope, setScope] = useState<'user' | 'project'>('user');
  const [plan, setPlan] = useState<InstallPlan | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [previewKey, setPreviewKey] = useState('');

  const currentKey = `${agent}:${scope}`;
  const stale = plan !== null && previewKey !== currentKey;

  const preview = async (event?: FormEvent) => {
    event?.preventDefault();
    if (loading) return;
    setLoading(true);
    setError(null);
    try {
      const result = await api.previewInstall({
        skill_path: skill.path,
        agent,
        scope,
      });
      setPlan(result);
      setPreviewKey(currentKey);
    } catch (cause) {
      setError(errorMessage(cause));
      setPlan(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="panel" aria-labelledby="install-heading">
      <div className="panel-head">
        <div>
          <p className="panel-eyebrow">AGENT INSTALL</p>
          <h2 id="install-heading">Preview an install plan</h2>
        </div>
        <StatusBadge tone="blue">READ-ONLY</StatusBadge>
      </div>

      <form className="install-form" onSubmit={preview}>
        <div className="form-field">
          <label htmlFor="install-agent">Target agent</label>
          <select
            id="install-agent"
            value={agent}
            onChange={(event) => setAgent(event.target.value)}
          >
            {KNOWN_AGENTS.map((name) => (
              <option key={name} value={name}>
                {name}
              </option>
            ))}
          </select>
        </div>

        <fieldset className="form-field scope-field">
          <legend>Scope</legend>
          <div className="scope-options">
            {(['user', 'project'] as const).map((value) => (
              <label key={value} className="radio-option">
                <input
                  type="radio"
                  name="install-scope"
                  value={value}
                  checked={scope === value}
                  onChange={() => setScope(value)}
                />
                <span>{value}</span>
              </label>
            ))}
          </div>
        </fieldset>

        <button type="submit" className="btn btn--primary btn--full" disabled={loading}>
          {loading ? 'Building plan…' : 'Preview install plan'}
        </button>
      </form>

      <p className="panel-note">
        Preview only. No files are written and no scripts run. Applying a plan requires an
        approved plan through the uSkill CLI.
      </p>

      {error && (
        <div className="inline-error" role="alert" aria-live="assertive">
          <div>
            <strong>Preview failed</strong>
            <p>{error}</p>
          </div>
          <button type="button" className="btn btn--ghost btn--small" onClick={() => void preview()}>
            Retry
          </button>
        </div>
      )}

      {stale && (
        <p className="inline-notice" role="status">
          Selection changed since this preview. Run it again to see the current plan.
        </p>
      )}

      {plan && !stale && (
        <div className="plan-result" aria-live="polite">
          <div className="plan-summary">
            <StatusBadge tone={plan.conflicts.length > 0 ? 'red' : 'green'}>
              {plan.conflicts.length > 0 ? 'CONFLICTS FOUND' : 'NO CONFLICTS'}
            </StatusBadge>
            <StatusBadge tone={plan.approved ? 'green' : 'neutral'}>
              {plan.approved ? 'APPROVED' : 'NOT APPROVED'}
            </StatusBadge>
          </div>
          <dl className="plan-facts">
            <div>
              <dt>Agent</dt>
              <dd>{plan.target_agent}</dd>
            </div>
            <div>
              <dt>Scope</dt>
              <dd>{plan.scope}</dd>
            </div>
            <div>
              <dt>Skill</dt>
              <dd>{plan.skill_name}</dd>
            </div>
            <div>
              <dt>Source</dt>
              <dd className="mono wrap">{plan.source_path}</dd>
            </div>
          </dl>
          <div className="plan-section">
            <h4>Actions</h4>
            {plan.actions.length === 0 ? (
              <p className="muted">No copy actions in this plan.</p>
            ) : (
              <ul className="plan-list">
                {plan.actions.map((action, index) => (
                  <li key={`${index}-${action.target}`}>
                    <span className="mono">{action.kind}</span> →{' '}
                    <span className="mono wrap">{action.target}</span>
                    {action.reason ? <em> — {action.reason}</em> : null}
                  </li>
                ))}
              </ul>
            )}
          </div>
          <PlanList title="Conflicts" items={plan.conflicts} tone="red" />
          <PlanList title="Risks" items={plan.risks} tone="orange" />
          <PlanList title="Rollback" items={plan.rollback} />
        </div>
      )}
    </section>
  );
}
