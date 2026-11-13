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
            args.path, args.output, domain=args.domain, owner=args.owner,
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
        print(f"\n{len(reports) - failed}/{len(reports)} migrated"
              + (" (dry-run)" if args.dry_run else ""))
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
    from core.uskills.runtime import SkillLibrary, SkillRuntime, create_provider
    from core.uskills.runtime.state import RunStore
    from core.uskills.validator import load_skill

    try:
        provider_kind = args.provider
        provider = create_provider(provider_kind)
        runtime = SkillRuntime(provider, store=RunStore(args.runs_dir))
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
    from core.uskills.evaluation import EvalSuite, run_eval_suite
    from core.uskills.runtime import SkillRuntime, create_provider
    from core.uskills.validator import load_skill

    try:
        skill = load_skill(args.skill)
        suite = EvalSuite.load(args.suite)
        provider = create_provider(args.provider)
        runtime = SkillRuntime(provider)
        repeats = getattr(args, "repeats", 1)
        report = run_eval_suite(runtime, skill, suite, repeats=repeats)
        if args.format == "json":
            print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
        else:
            print(report.to_markdown())
        if args.output:
            out = Path(args.output)
            out.parent.mkdir(parents=True, exist_ok=True)
            if args.format == "json":
                out.write_text(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
            else:
                out.write_text(report.to_markdown(), encoding="utf-8")
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
        print(f"IR: goal={report.ir['goal'][:60]!r} steps={len(report.ir['steps'])} "
              f"kinds={report.ir['step_kind_summary']}")
        for note in report.notes:
            print(f"  ℹ {note}")
        for c in report.candidates:
            flag = "⚠ review" if c.score.review_required else "ok"
            print(f"  [{flag}] {c.skill.skill_id}  quality={c.score.total}/100 "
                  f"lifecycle={c.lifecycle.value}")
            if c.score.total < 100:
                for dim in c.score.dimensions:
                    if dim.score < dim.max:
                        print(f"      - {dim.name}: {dim.score}/{dim.max} :: "
                              + "; ".join(dim.evidence))
        print(f"\n{len(report.candidates)} draft candidate(s) → {args.output}/drafts/")
        print("policy: drafts require human review before publish (Draft→Validated→…)")
        return 0 if report.candidates else 1
    except Exception as e:
        print(f"Build failed: {e}", file=sys.stderr)
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
        "--target", choices=["skill", "manifest", "both"], default="skill",
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
        choices=["mock", "openai-chat", "openai-responses"],
        help="Model provider (mock requires no API key).",
    )
    p.add_argument("--library", default="skills", help="Skill library directory.")
    p.add_argument("--runs-dir", default=".uskills/runs", help="Checkpoint directory.")
    p.set_defaults(func=cmd_run)

    p = sub.add_parser("eval", help="Run an evaluation suite against a skill.")
    p.add_argument("--skill", required=True, help="Path to skill YAML/JSON.")
    p.add_argument("--suite", required=True, help="Path to eval suite JSON.")
    p.add_argument(
        "--provider", default="mock", choices=["mock", "openai-chat", "openai-responses"]
    )
    p.add_argument("--repeats", type=int, default=1)
    p.add_argument("--format", default="markdown", choices=["markdown", "json"])
    p.add_argument("--output", default=None, help="Write report to file.")
    p.set_defaults(func=cmd_eval)

    p = sub.add_parser("doctor", help="Check environment and asset health.")
    p.set_defaults(func=cmd_doctor)

    return parser


def main() -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
