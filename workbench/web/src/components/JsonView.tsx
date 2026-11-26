import { useState } from 'react';
import { CheckIcon, CopyIcon } from './Icons';

interface JsonViewProps {
  value: unknown;
  label?: string;
}

export function JsonView({ value, label = 'Raw JSON' }: JsonViewProps) {
  const [copied, setCopied] = useState(false);
  const text = JSON.stringify(value ?? null, null, 2) ?? 'null';

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1600);
    } catch {
      setCopied(false);
    }
  };

  return (
    <div className="json-view">
      <div className="json-toolbar">
        <span className="panel-eyebrow">{label}</span>
        <button type="button" className="btn btn--ghost btn--small" onClick={copy}>
          {copied ? <CheckIcon size={15} /> : <CopyIcon size={15} />}
          {copied ? 'Copied' : 'Copy JSON'}
        </button>
      </div>
      <pre tabIndex={0} aria-label={`${label} payload`}>
        <code>{text}</code>
      </pre>
    </div>
  );
}
