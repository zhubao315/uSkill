# uSkill Workbench 3.0 — Web UI

React + TypeScript + Vite frontend for the local Workbench service. It reads real data only;
a failed request renders an error with a retry button, never fabricated numbers.

## Run locally

```bash
npm install
npm run dev        # http://localhost:5173, /api proxied to 127.0.0.1:8765
npm run typecheck
npm run build
npx vitest run
```

The FastAPI service in `workbench/server/` (implemented separately) must listen on port 8765.
The pairing token is supplied by a bootstrap script as `window.__USKILL_TOKEN__` and is sent as
`Authorization: Bearer <token>` on every `/api` call. The UI does not persist or display it.

## Pages

| Route | Data source | What it shows |
| --- | --- | --- |
| `/` | health, skills, agents, runs | Service status, derived summary, inventory, integrity, detection, recent runs |
| `/skills` | `/api/skills?...` | Debounced search + category/format/status filters, full record table |
| `/skills/:skillId` | `/api/skills/{id}`, `/api/install/preview` | All record fields, raw JSON, agent/scope install-plan preview |
| `/agents` | `/api/agents` | Detection badge, skill locations, installed skills |
| `/runs` | `/api/runs`, `/api/runs/{id}` | Expandable run history with steps, events and full record |

## Structure

- `src/api/client.ts` — typed fetch wrapper, token header, unified `ApiError`
- `src/hooks/` — request lifecycle, debounce, theme persistence
- `src/components/` — reusable layout, tables, badges, states, JSON view, install panel
- `src/pages/` — route-level composition
- `src/styles/tokens.css` — light/dark tokens, uSkill's three brand colors
- `src/styles/app.css` — component styles, no gradients or glass surfaces

The install panel previews a plan only. Applying a plan requires an approved plan via the CLI;
this UI never writes files.
