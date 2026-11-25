# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in uSkill, please report it by
opening a **private security advisory** on
[GitHub](https://github.com/zhubao315/uSkill/security/advisories/new).
Do not disclose the issue in a public issue until it is triaged.

Maintainers aim to acknowledge reports within 5 business days.

## Security Model (2.0)

uSkill treats **all skill content as untrusted data, never as policy**:

- SOP files, imported Agent Skills, SKILL.md bodies, and generated skills
  are input data. The runtime's system prompt explicitly states skill text
  and inputs must not be promoted to system instructions.
- `execute.tools` in a skill YAML only *declares* intent. Actual execution
  requires the tool to be registered in the `ToolRegistry` **and** its
  permission class (read / write / network / shell / sensitive_data) to be
  allowed by the runtime `PermissionPolicy` (default: `read` only).
- Skills that execute scripts or write data must be reviewed before
  promotion (`Draft → Validated → Reviewed → Published`).
- Never store API keys, secrets, or personal credentials in skill files;
  configure providers through environment variables or provider profiles.

## Scope Notes

The 2.0 runtime enforces timeout/retry/permission gates for registered
tools. There is **no built-in OS-level sandbox** for `scripts/` in skill
directories: do not auto-execute scripts from imported skills. When you
wire scripts into a ToolRegistry, run them in a container or other
isolation appropriate to your threat model.

## Supported Versions

| Version  | Supported |
| -------- | --------- |
| 2.0.x    | ✅        |
| 1.2.x    | ⚠ (critical fixes only) |
| < 1.2    | ❌ (upgrade) |
