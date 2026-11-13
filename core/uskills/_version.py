"""Single source of truth for the uSkill package version.

All packaging metadata (pyproject.toml), the CLI, and the core package
import this value so the version number is never duplicated by hand.

Note: the *schema* version (``core.uskills.schema.SCHEMA_VERSION``) tracks
the skill-file format and is intentionally independent from this number.
"""

__version__ = "2.0.0"
