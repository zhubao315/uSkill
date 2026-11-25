"""uSkill CLI Tool.

Command-line interface for uSkill operations:
validate / convert / schema / index / stats (legacy) plus
init / inspect / import-skill / export-skill / run / eval / doctor (v1.2).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.uskills import __version__  # noqa: E402
from core.uskills.converter import ConversionError, convert_sop_file  # noqa: E402
from core.uskills.indexer import build_skills_index, get_skill_stats  # noqa: E402
from core.uskills.schema import exported_json_schema, get_schema_version  # noqa: E402
from core.uskills.validator import validate_directory, validate_skill_file  # noqa: E402


def cmd_validate(args: argparse.Namespace) -> int:
    """Validate skill file(s) (schema + semantics)."""
    path = Path(args.path)

    if path.is_dir():
        results = validate_directory(path, recursive=args.recursive)
        failed = 0
        for file_path, (ok, message) in sorted(results.items()):
            status = "✓" if ok else "✗"
            print(f"{status} {file_path}: {message}")
            if not ok:
                failed += 1

        total = len(results)
        print(f"\n{total - failed}/{total} files valid")
        return 0 if failed == 0 else 1

    if (path / "SKILL.md").exists():
        from core.uskills.agentskills import validate_agent_skill

        ok, issues = validate_agent_skill(path)
        for issue in issues:
            print(f"  - {issue}")
        print(f"{'✓' if ok else '✗'} {path}: {'valid Agent Skill' if ok else 'invalid'}")
        return 0 if ok else 1

    ok, message = validate_skill_file(path)
    print(f"{'✓' if ok else '✗'} {path}: {message}")
    return 0 if ok else 1


def cmd_convert(args: argparse.Namespace) -> int:
    """Convert SOP file to uSkill files."""
    try:
        written = convert_sop_file(
            args.path,
            args.output,
            domain=args.domain,
            owner=args.owner,
            version=args.version,
        )
        print(f"Generated {len(written)} skills:")
        for item in written:
            print(f"  → {item}")
        return 0
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ConversionError as e:
        print(f"Conversion error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


def cmd_schema(args: argparse.Namespace) -> int:
    """Export JSON Schema for uSkill (skill V1 and/or Manifest V2)."""
    from core.uskills.standards_compat import manifest_json_schema

    if args.target in ("skill", "both"):
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        schema = exported_json_schema()
        target.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Skill schema v{get_schema_version()} exported to: {target}")
    if args.target in ("manifest", "both"):
        mtarget = Path(args.manifest_output)
        mtarget.parent.mkdir(parents=True, exist_ok=True)
        mtarget.write_text(
            json.dumps(manifest_json_schema(), ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Manifest schema (uskills/v2) exported to: {mtarget}")
    return 0


def cmd_migrate(args: argparse.Namespace) -> int:
    """Migrate legacy skill files into two-layer Agent Skill directories."""
    from core.uskills.standards_compat import migrate_directory, migrate_skill

    path = Path(args.path)
    try:
        if path.is_dir():
            reports = migrate_directory(path, args.output, force=args.force, dry_run=args.dry_run)
        else:
            reports = [migrate_skill(path, args.output, force=args.force, dry_run=args.dry_run)]
        failed = 0
        for r in reports:
            mark = "✓" if r.ok else "✗"
            print(f"{mark} {r.source} → {r.target or '-'}")
            for action in r.actions:
                print(f"    {action}")
            for warning in r.warnings:
                print(f"    ⚠ {warning}")
            for loss in r.lossy:
                print(f"    ⚠ not representable in pure Agent Skills: {loss}")
            if not r.ok:
                failed += 1
        print(
            f"\n{len(reports) - failed}/{len(reports)} migrated"
            + (" (dry-run)" if args.dry_run else "")
        )
        return 0 if failed == 0 else 1
    except Exception as e:
        print(f"Migrate failed: {e}", file=sys.stderr)
        return 1


def cmd_index(args: argparse.Namespace) -> int:
    """Build skills index markdown file."""
    try:
        target = build_skills_index(args.path, args.output)
        stats = get_skill_stats(args.path)
        print(f"Index generated: {target}")
        if args.json:
            print(json.dumps(stats, indent=2, ensure_ascii=False))
        else:
            print(f"  Skills: {stats['total_skills']}")
            print(f"  Sources: {stats['total_sources']}")
            print(f"  Categories: {stats['categories']}")
        return 0
    except Exception as e:
        print(f"Error building index: {e}", file=sys.stderr)
        return 1


def cmd_stats(args: argparse.Namespace) -> int:
    """Show skill statistics."""
    try:
        stats = get_skill_stats(args.path)
        print(json.dumps(stats, indent=2, ensure_ascii=False))
        return 0
    except Exception as e:
        print(f"Error getting stats: {e}", file=sys.stderr)
        return 1


def cmd_init(args: argparse.Namespace) -> int:
    """Scaffold a new Agent Skill directory (SKILL.md + uskill.yaml + evals)."""
    from core.uskills.agentskills import SKILL_FILE
    from core.uskills.manifest import USkillManifest, dump_manifest

    name = args.name
    root = Path(args.output) / name
    if root.exists() and not args.force:
        print(f"Error: {root} exists (use --force)", file=sys.stderr)
        return 1

    (root / "references").mkdir(parents=True, exist_ok=True)
    (root / "scripts").mkdir(parents=True, exist_ok=True)
    (root / "evals").mkdir(parents=True, exist_ok=True)

    desc = args.description or f"{name}: describe what this skill does and when to use it."
    (root / SKILL_FILE).write_text(
        "---\n"
        f"name: {name}\n"
        f"description: {desc}\n"
        "---\n\n"
        f"# {name}\n\n"
        "## When to use\n\nTODO: positive triggers, and similar tasks that should NOT trigger.\n\n"
        "## Instructions\n\n1. TODO step\n\n"
        "## References\n\nKeep this file under 500 lines; move details to references/.\n",
        encoding="utf-8",
    )
    manifest = USkillManifest(
        metadata={"name": name, "description": desc[:1024]},
        execution={"mode": "instruction"},
    )
    dump_manifest(manifest, root)

    print(f"Initialized Agent Skill at {root}/")
    print("  SKILL.md     standard layer (portable across agents)")
    print("  uskill.yaml  uSkill augmentation layer")
    print("  evals/       add dataset.json to prove the skill works")
    return 0


def cmd_import_skill(args: argparse.Namespace) -> int:
    """Import a standard Agent Skill folder (adds uskill.yaml manifest)."""
    from core.uskills.agentskills import import_agent_skill

    try:
        target, manifest, notes = import_agent_skill(args.path, args.output, force=args.force)
        print(f"Imported {manifest.metadata.name}@{manifest.metadata.version} → {target}")
        for note in notes:
            print(f"  - {note}")
        return 0
    except Exception as e:
        print(f"Import failed: {e}", file=sys.stderr)
        return 1


def cmd_export_skill(args: argparse.Namespace) -> int:
    """Export a legacy uSkill YAML as an Agent Skill directory."""
    from core.uskills.agentskills import export_agent_skill, inspect_compatibility
    from core.uskills.manifest import manifest_from_legacy_skill
    from core.uskills.validator import load_skill

    try:
        skill = load_skill(args.path)
        manifest = manifest_from_legacy_skill(skill)
        body = (
            f"# {skill.meta.name}\n\n{skill.meta.description}\n\n"
            "## Instructions\n\n" + skill.execute.prompt_template
        )
        out = export_agent_skill(manifest, body, args.output, force=args.force)
        print(f"Exported Agent Skill → {out}")
        for note in inspect_compatibility(manifest):
            print(f"  ⚠ {note}")
        return 0
    except Exception as e:
        print(f"Export failed: {e}", file=sys.stderr)
        return 1


def cmd_inspect(args: argparse.Namespace) -> int:
    """Inspect an Agent Skill directory or a skill file."""
    from core.uskills.agentskills import agent_skill_to_dict, inspect_agent_skill

    path = Path(args.path)
    if path.is_dir() and (path / "SKILL.md").exists():
        info = agent_skill_to_dict(inspect_agent_skill(path))
        print(json.dumps(info, indent=2, ensure_ascii=False))
        return 0
    try:
        from core.uskills.validator import load_skill

        skill = load_skill(path)
        out = {
            "skill_id": skill.skill_id,
            "name": skill.meta.name,
            "category": skill.meta.category.value,
            "version": skill.meta.version,
            "params": [p.name for p in skill.input.params],
            "tools": skill.execute.tools,
            "control": {
                "timeout": skill.control.timeout,
                "retry": skill.control.retry,
            },
            "source": skill.source.sop_name if skill.source else None,
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0
    except Exception as e:
        print(f"Inspect failed: {e}", file=sys.stderr)
        return 1


def cmd_run(args: argparse.Namespace) -> int:
    """Execute a skill via the governed runtime."""
    from core.uskills.governance.audit import AuditLogger
    from core.uskills.runtime import SkillLibrary, SkillRuntime, create_provider
    from core.uskills.runtime.state import RunStore
    from core.uskills.validator import load_skill

    try:
        provider_kind = args.provider
        provider = create_provider(provider_kind)
        auditor = AuditLogger(args.audit) if args.audit else None
        runtime = SkillRuntime(provider, store=RunStore(args.runs_dir), auditor=auditor)
        if args.library:
            runtime.library = SkillLibrary()
            runtime.library.load_directory(args.library)

        skill_path = Path(args.skill)
        if skill_path.exists():
            skill = load_skill(skill_path)
        else:
            runtime.library.load_directory(args.library or "skills")
            skill_found = runtime.library.resolve(args.skill)
            if skill_found is None:
                print(f"Error: skill not found: {args.skill}", file=sys.stderr)
                return 1
            skill = skill_found

        inputs = json.loads(args.input) if args.input else {}
        record = runtime.run(skill, inputs)
        payload = {
            "run_id": record.run_id,
            "status": record.status.value,
            "result": record.result,
            "error": record.error,
            "usage": record.usage,
            "execution_time": record.execution_time,
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0 if record.status.value == "COMPLETED" else 1
    except Exception as e:
        print(f"Run failed: {e}", file=sys.stderr)
        return 1


def cmd_eval(args: argparse.Namespace) -> int:
    """Run an evaluation suite against a skill."""
    from core.uskills.evaluation import (
        EvalSuite,
        check_release_gate,
        judge_eval_suite,
        matrix_summary,
        run_eval_matrix,
        run_eval_suite,
    )
    from core.uskills.runtime import SkillRuntime, create_provider
    from core.uskills.validator import load_skill

    try:
        skill = load_skill(args.skill)
        suite = EvalSuite.load(args.suite)

        def make_runtime() -> SkillRuntime:
            if args.provider == "mock" and args.mock_response:
                return SkillRuntime(create_provider("mock", script=args.mock_response))
            return SkillRuntime(create_provider(args.provider))

        if args.models:
            models = [m.strip() for m in args.models.split(",") if m.strip()]
            reports = run_eval_matrix(
                make_runtime,
                skill,
                suite,
                models,
                repeats=args.repeats,
            )
            summary = matrix_summary(reports)
            if args.format == "json":
                print(json.dumps(summary, indent=2, ensure_ascii=False))
            else:
                print(f"# Model matrix: {suite.skill} ({len(suite.cases)} cases)")
                for model, row in summary.items():
                    print(
                        f"- `{model}`: success={row['success_rate']} "
                        f"consistency={row['consistency']} cost=${row['cost_usd']} "
                        f"latency={row['latency_mean_ms']}ms"
                    )
            if args.output:
                out = Path(args.output)
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
            return 0

        runtime = make_runtime()
        report = run_eval_suite(runtime, skill, suite, repeats=args.repeats)

        if args.judge:
            judge_eval_suite(runtime, report, model=args.judge_model or skill.execute.model)

        gate_problems: list[str] = []
        if args.compare:
            previous = json.loads(Path(args.compare).read_text(encoding="utf-8"))
            from core.uskills.evaluation import compare_reports

            diff = compare_reports(report, previous)
            print(
                f"vs previous: {diff['delta_pp']:+.1f} pp, "
                f"regressed={diff['regressed_cases'] or 'none'} "
                f"improved={diff['improved_cases'] or 'none'}"
            )
            if args.gate:
                gate_problems = check_release_gate(report, previous, max_drop_pp=args.max_drop_pp)
                for problem in gate_problems:
                    print(f"  ✗ GATE: {problem}", file=sys.stderr)
        elif args.gate:
            print("GATE: --gate requires --compare <previous report.json>", file=sys.stderr)
            return 2

        if args.format == "json":
            print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        else:
            print(report.to_markdown())
        if args.output:
            out = Path(args.output)
            out.parent.mkdir(parents=True, exist_ok=True)
            if args.format == "json":
                out.write_text(
                    json.dumps(report.to_dict(), indent=2, ensure_ascii=False),
                    encoding="utf-8",
                )
            else:
                out.write_text(report.to_markdown(), encoding="utf-8")
        if gate_problems:
            return 1
        return 0
    except Exception as e:
        print(f"Eval failed: {e}", file=sys.stderr)
        return 1


def cmd_build(args: argparse.Namespace) -> int:
    """Build skill drafts from a source document (never auto-publishes)."""
    from core.uskills.builder import build_skills

    try:
        report = build_skills(args.path, args.output, domain=args.domain)
        print(f"source: {report.source}")
        print(
            f"IR: goal={report.ir['goal'][:60]!r} steps={len(report.ir['steps'])} "
            f"kinds={report.ir['step_kind_summary']}"
        )
        for note in report.notes:
            print(f"  ℹ {note}")
        for c in report.candidates:
            flag = "⚠ review" if c.score.review_required else "ok"
            print(
                f"  [{flag}] {c.skill.skill_id}  quality={c.score.total}/100 "
                f"lifecycle={c.lifecycle.value}"
            )
            if c.score.total < 100:
                for dim in c.score.dimensions:
                    if dim.score < dim.max:
                        print(
                            f"      - {dim.name}: {dim.score}/{dim.max} :: "
                            + "; ".join(dim.evidence)
                        )
        print(f"\n{len(report.candidates)} draft candidate(s) → {args.output}/drafts/")
        print("policy: drafts require human review before publish (Draft→Validated→…)")
        return 0 if report.candidates else 1
    except Exception as e:
        print(f"Build failed: {e}", file=sys.stderr)
        return 1


def cmd_search(args: argparse.Namespace) -> int:
    """Search the local skill registry by metadata (five modes)."""
    from core.uskills.registry import SkillRegistry, SkillRegistryV3

    registry = SkillRegistry(args.path)
    hits = registry.search(args.query, mode=args.mode, limit=args.limit)
    if args.json:
        print(json.dumps([h.to_dict() for h in hits], indent=2, ensure_ascii=False))
    else:
        if not hits:
            print(f"no skills matched {args.query!r} (mode={args.mode}, root={args.path})")
        for h in hits:
            print(f"  {h.skill_id}  [{h.matched_by}]  {h.name}")
            print(f"      {h.path}  domain={h.domain} tags={','.join(h.tags) or '-'}")
    return 0 if hits else 1


def cmd_package(args: argparse.Namespace) -> int:
    """Package a skill into a verifiable zip with checksums."""
    from core.uskills.packaging import package_skill

    try:
        result = package_skill(args.path, args.output, force=args.force)
        print(f"package: {result.path}")
        print(f"sha256:  {result.sha256}")
        print(f"files:   {len(result.files)} (incl. package.json manifest)")
        return 0
    except Exception as e:
        print(f"Package failed: {e}", file=sys.stderr)
        return 1


def cmd_risk(args: argparse.Namespace) -> int:
    """Show derived risk level (L0-L4) for skills from real capabilities."""
    from typing import Any

    from core.uskills.builder.scan import scan_risk_level, scan_scripts
    from core.uskills.governance.risk import assess_skill_risk, skill_directory_flags
    from core.uskills.standards_compat import FORMAT_AGENT_SKILL, detect_format
    from core.uskills.validator import load_skill

    path = Path(args.path)
    rows: list[dict[str, Any]] = []
    if detect_format(path) == FORMAT_AGENT_SKILL:
        flags = skill_directory_flags(path)
        findings = scan_scripts(path / "scripts") if flags["has_scripts"] else []
        level = max(
            (int(scan_risk_level(findings)) if findings else 0),
            3 if flags["has_scripts"] else 0,
        )
        rows.append(
            {
                "path": str(path),
                "level": f"L{level}",
                "scripts": flags["scripts"],
                "findings": [f.to_dict() for f in findings][:10],
            }
        )
    else:
        files = (
            sorted(
                p
                for p in path.rglob("*")
                if p.is_file()
                and p.suffix.lower() in (".yaml", ".yml", ".json")
                and p.stem != "uskill"
            )
            if path.is_dir()
            else [path]
        )
        for f in files:
            try:
                skill = load_skill(f)
            except Exception:
                continue
            assessment = assess_skill_risk(skill)
            rows.append(
                {
                    "path": str(f),
                    "level": f"L{int(assessment.level)}",
                    "factors": assessment.factors,
                }
            )
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
    else:
        for r in rows:
            print(f"  {r['level']}  {r['path']}")
            for note in r.get("factors", []):
                print(f"       - {note}")
            for finding in r.get("findings", []):
                print(
                    f"       ! scripts/{finding['file']}:{finding['line']} "
                    f"{finding['pattern']} ({finding['description']})"
                )
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """List skills in the local registry."""
    from core.uskills.registry import SkillRegistry, SkillRegistryV3

    registry = SkillRegistry(args.path)
    skills = registry.all()
    if args.filter:
        hits = registry.search(args.filter, mode="auto")
        ids = {h.skill_id for h in hits}
        skills = [s for s in skills if s.skill_id in ids]
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "skill_id": s.skill_id,
                        "name": s.meta.name,
                        "category": s.meta.category.value,
                        "domain": s.meta.domain,
                        "version": s.meta.version,
                        "tags": s.meta.tags,
                    }
                    for s in skills
                ],
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        for s in skills:
            print(
                f"  {s.skill_id}  {s.meta.name}  "
                f"[{s.meta.category.value}/{s.meta.domain}] v{s.meta.version}"
            )
    health = registry.health()
    if not health["ok"]:
        print(
            f"⚠ registry health: broken={len(health['broken'])} "
            f"duplicates={health['duplicate_ids']}",
            file=sys.stderr,
        )
        return 1
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    """Show a redacted audit trail (JSONL written by AuditLogger)."""
    from core.uskills.governance.audit import AuditLogger

    path = Path(args.path)
    if not path.exists():
        print(f"audit file not found: {path}", file=sys.stderr)
        return 1
    entries = AuditLogger(path).read()
    if args.action:
        entries = [e for e in entries if e.get("action") == args.action]
    for entry in entries[-args.limit :]:
        if args.json:
            print(json.dumps(entry, ensure_ascii=False))
        else:
            detail = {
                k: v for k, v in entry.items() if k not in ("time", "action", "run_id", "skill_id")
            }
            print(
                f"  {entry['time']}  {entry['action']:<22} "
                f"run={entry.get('run_id') or '-'}  {detail or ''}"
            )
    return 0


def cmd_test(args: argparse.Namespace) -> int:
    """Run a skill suite as pass/fail tests (assertions only, no baseline)."""
    from core.uskills.evaluation import EvalSuite, run_case
    from core.uskills.runtime import SkillRuntime, create_provider
    from core.uskills.validator import load_skill

    try:
        skill = load_skill(args.skill)
        suite = EvalSuite.load(args.suite)
        if args.provider == "mock" and args.mock_response:
            runtime = SkillRuntime(create_provider("mock", script=args.mock_response))
        else:
            runtime = SkillRuntime(create_provider(args.provider))
        failures = 0
        for case in suite.cases:
            result = run_case(runtime, skill, case)
            mark = "PASS" if result.passed else "FAIL"
            print(f"  [{mark}] {case.task_id}: {result.detail[:100]}")
            failures += 0 if result.passed else 1
        total = len(suite.cases)
        print(f"{total - failures}/{total} test cases passed")
        return 1 if failures else 0
    except Exception as e:
        print(f"Test failed: {e}", file=sys.stderr)
        return 1


def cmd_doctor(args: argparse.Namespace) -> int:  # noqa: ARG001
    """Report environment and asset health."""
    import sys as _sys

    problems = 0
    checks: list[tuple[bool, str]] = []

    checks.append((_sys.version_info >= (3, 11), f"python {_sys.version.split()[0]} (need >=3.11)"))
    try:
        import pydantic  # noqa: F401
        import yaml  # noqa: F401

        checks.append((True, "core dependencies (pydantic, PyYAML) present"))
    except ImportError as e:
        checks.append((False, f"missing dependency: {e}"))
    try:
        import openai  # noqa: F401

        checks.append((True, f"optional llm extra (openai {openai.__version__})"))
    except ImportError:
        checks.append((True, "llm extra not installed (optional: pip install 'uskills[llm]')"))

    skills_dir = Path("skills")
    if skills_dir.exists():
        results = validate_directory(skills_dir)
        bad = {k: v for k, v in results.items() if not v[0]}
        checks.append((not bad, f"skills/ valid ({len(results) - len(bad)}/{len(results)})"))
        for path, (_, msg) in sorted(bad.items()):
            print(f"  ✗ {path}: {msg}")

    for ok, detail in checks:
        print(f"{'✓' if ok else '✗'} {detail}")
        if not ok:
            problems += 1
    return 1 if problems else 0


def cmd_registry_scan(args: argparse.Namespace) -> int:
    """Scan all roots and emit a unified machine-readable asset report."""
    from pathlib import Path
    roots = list(args.path) if isinstance(args.path, list) else [args.path]
    registry = SkillRegistryV3(roots[0], extra_roots=roots[1:])
    report = registry.report()
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(text)
    return 0


def cmd_registry_report(args: argparse.Namespace) -> int:
    """Print registry health summary."""
    from pathlib import Path
    roots = list(args.path) if isinstance(args.path, list) else [args.path]
    registry = SkillRegistryV3(roots[0], extra_roots=roots[1:])
    print(json.dumps(registry.health(), ensure_ascii=False, indent=2))
    return 0


def cmd_registry_duplicates(args: argparse.Namespace) -> int:
    """Print duplicate asset groups (identical content hashes)."""
    from pathlib import Path
    roots = list(args.path) if isinstance(args.path, list) else [args.path]
    registry = SkillRegistryV3(roots[0], extra_roots=roots[1:])
    print(json.dumps(registry.duplicates, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build argument parser."""
    parser = argparse.ArgumentParser(
        prog="uskills",
        description="uSkill - Agent Skill Engineering Platform CLI.",
        epilog="For more information, visit: https://zhubao315.github.io/uSkill/",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("validate", help="Validate uSkill files or Agent Skill directories.")
    p.add_argument("path")
    p.add_argument("-r", "--recursive", action="store_true", default=True)
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("convert", help="Convert a SOP text file into atomic skills.")
    p.add_argument("path")
    p.add_argument("--output", default="skills/generated")
    p.add_argument("--domain", default="general")
    p.add_argument("--owner", default="uSkill")
    p.add_argument("--version", default="1.1.0", help="Version tag for generated skills.")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("schema", help="Export the uSkill JSON Schema.")
    p.add_argument("--output", default="standards/uskill.schema.json")
    p.add_argument(
        "--target",
        choices=["skill", "manifest", "both"],
        default="skill",
        help="skill (legacy V1), manifest (uskills/v2) or both.",
    )
    p.add_argument("--manifest-output", default="standards/uskill-manifest.schema.json")
    p.set_defaults(func=cmd_schema)

    p = sub.add_parser("migrate", help="Migrate legacy skills into two-layer Agent Skill dirs.")
    p.add_argument("path", help="Legacy skill file or directory.")
    p.add_argument("--output", default="skills/migrated")
    p.add_argument("--force", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_migrate)

    p = sub.add_parser("build", help="Build Draft skill candidates from a source document.")
    p.add_argument("path", help="SOP/prompt/Markdown file or raw text.")
    p.add_argument("--output", default="skills/generated-builder")
    p.add_argument("--domain", default="general")
    p.set_defaults(func=cmd_build)

    p = sub.add_parser("index", help="Build the markdown skills index.")
    p.add_argument("path")
    p.add_argument("--output", default="docs/generated/skills-index.md")
    p.add_argument("--json", action="store_true", help="Machine-readable stats.")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("stats", help="Show skill statistics.")
    p.add_argument("path")
    p.set_defaults(func=cmd_stats)

    p = sub.add_parser("init", help="Scaffold a new Agent Skill directory.")
    p.add_argument("name")
    p.add_argument("--output", default="skills/agent-skills")
    p.add_argument("--description", default="")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("import-skill", help="Import a standard Agent Skill folder.")
    p.add_argument("path")
    p.add_argument("--output", default=None)
    p.add_argument("--force", action="store_true", help="Import even with validation issues.")
    p.set_defaults(func=cmd_import_skill)

    p = sub.add_parser("export-skill", help="Export a uSkill YAML as an Agent Skill dir.")
    p.add_argument("path")
    p.add_argument("--output", default="skills/agent-skills")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_export_skill)

    p = sub.add_parser("inspect", help="Inspect an Agent Skill dir or skill file.")
    p.add_argument("path")
    p.set_defaults(func=cmd_inspect)

    p = sub.add_parser("run", help="Execute a skill via the governed runtime.")
    p.add_argument("skill", help="Skill file path or name (resolved from --library).")
    p.add_argument("--input", default="{}", help="JSON object of inputs.")
    p.add_argument(
        "--provider",
        default="mock",
        choices=[
            "mock",
            "openai-chat",
            "openai-responses",
            "openai-compatible",
            "anthropic",
            "local",
        ],
        help="Model provider (mock requires no API key).",
    )
    p.add_argument("--library", default="skills", help="Skill library directory.")
    p.add_argument("--runs-dir", default=".uskills/runs", help="Checkpoint directory.")
    p.add_argument(
        "--audit", default=None, help="Write a redacted audit trail (JSONL) to this path."
    )
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("eval", help="Run an evaluation suite against a skill.")
    p.add_argument("--skill", required=True, help="Path to skill YAML/JSON.")
    p.add_argument("--suite", required=True, help="Path to eval suite JSON.")
    p.add_argument(
        "--provider",
        default="mock",
        choices=[
            "mock",
            "openai-chat",
            "openai-responses",
            "openai-compatible",
            "anthropic",
            "local",
        ],
    )
    p.add_argument("--repeats", type=int, default=1)
    p.add_argument(
        "--mock-response",
        default=None,
        help="Deterministic mock provider response (offline regression runs in CI; no API key).",
    )
    p.add_argument(
        "--models", default=None, help="Comma-separated models for a multi-model benchmark matrix."
    )
    p.add_argument(
        "--compare", default=None, help="Previous report JSON to diff for regression tracking."
    )
    p.add_argument(
        "--gate", action="store_true", help="Fail (exit 1) on unexplained regressions vs --compare."
    )
    p.add_argument(
        "--max-drop-pp",
        type=float,
        default=10.0,
        help="Largest tolerated success-rate drop (percentage points).",
    )
    p.add_argument(
        "--judge",
        action="store_true",
        help="Attach separate LLM-as-Judge verdicts (advisory only).",
    )
    p.add_argument("--judge-model", default=None, help="Judge model name.")
    p.add_argument("--format", default="markdown", choices=["markdown", "json"])
    p.add_argument("--output", default=None, help="Write report to file.")
    p.set_defaults(func=cmd_eval)

    p = sub.add_parser("search", help="Search skills by name/tag/domain/keyword/dependency.")
    p.add_argument("query")
    p.add_argument("path", default="skills", nargs="?")
    p.add_argument(
        "--mode",
        default="auto",
        choices=["auto", "name", "tag", "domain", "keyword", "dependency"],
    )
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("package", help="Package a skill dir/file into a checksummed zip.")
    p.add_argument("path")
    p.add_argument("--output", default="dist")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_package)

    p = sub.add_parser("risk", help="Derive risk level (L0-L4) from real capabilities.")
    p.add_argument("path")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_risk)

    p = sub.add_parser("list", help="List skills in the local registry.")
    p.add_argument("path", default="skills", nargs="?")
    p.add_argument("--filter", default=None, help="Query (same modes as search).")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("audit", help="Show a redacted JSONL audit trail.")
    p.add_argument("path")
    p.add_argument("--action", default=None, help="Filter by action.")
    p.add_argument("--limit", type=int, default=50)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_audit)

    p = sub.add_parser("test", help="Run a skill suite as pass/fail tests.")
    p.add_argument("--skill", required=True)
    p.add_argument("--suite", required=True)
    p.add_argument(
        "--provider",
        default="mock",
        choices=[
            "mock",
            "openai-chat",
            "openai-responses",
            "openai-compatible",
            "anthropic",
            "local",
        ],
    )
    p.add_argument(
        "--mock-response",
        default=None,
        help="Deterministic mock provider response (offline CI runs).",
    )
    p.set_defaults(func=cmd_test)

    p = sub.add_parser("doctor", help="Check environment and asset health.")
    p.set_defaults(func=cmd_doctor)

    # Workbench 3.0: unified registry commands
    registry = sub.add_parser("registry", help="Unified multi-format skill registry (3.0).")
    registry_sub = registry.add_subparsers(dest="registry_command")
    for name, fn, help_text in [
        ("scan", cmd_registry_scan, "Scan roots and emit a unified asset report (JSON)."),
        ("report", cmd_registry_report, "Show registry health summary."),
        ("duplicates", cmd_registry_duplicates, "Show duplicate asset groups."),
    ]:
        p = registry_sub.add_parser(name, help=help_text)
        p.add_argument("path", nargs="*", default=["skills"], help="Skill roots to scan.")
        p.add_argument("--output", help="Write report JSON to a file.")
        p.set_defaults(func=fn)

    return parser


def main() -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
