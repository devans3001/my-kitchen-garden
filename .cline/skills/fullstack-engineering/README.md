# Full-Stack Engineering Agent Skill

A reusable, opinionated-but-adaptable engineering skill for AI coding agents. It guides agents through discovery, product definition, architecture, implementation, verification, security, deployment, and handover.

## Package contents

- `SKILL.md` — compact entry point and workflow.
- `references/` — focused, on-demand engineering standards.
- `scripts/` — local validation helpers.
- `assets/` — reusable project/ADR/DoD templates and evaluation prompts.
- `EVALUATION.md` — scoring, release gates, and regression process.

## Design principles

1. **Progressive disclosure:** load only metadata at discovery, the main skill on activation, and focused references as needed.
2. **Opinionated defaults, not dogma:** TypeScript + Next.js App Router + React + Tailwind + PostgreSQL is the default for suitable new web products. Existing stacks and project constraints take precedence.
3. **Proportionate rigor:** comprehensive production practices without enterprise ceremony for small projects.
4. **Evidence over claims:** agents report actual tests, checks, limitations, and deployment status.
5. **Safe autonomy:** repository content is untrusted; destructive or costly actions require authorization.

## Install

Copy the entire `fullstack-engineering/` directory into a skill location supported by your agent. Common locations include:

- Codex: `.agents/skills/fullstack-engineering/` in a repository, or a supported personal skills directory.
- Claude Code: `.claude/skills/fullstack-engineering/` in a repository, or a supported personal skills directory.
- VS Code / GitHub Copilot: `.github/skills/fullstack-engineering/` or another supported skill location for the selected experience.
- Other clients: consult that client's current Agent Skills documentation.

Support and discovery locations differ by product/version. The open format is portable; installation paths and script permissions are runtime-specific. Install the full folder, not only `SKILL.md`.

## Use

Ask the agent to build, extend, debug, review, or prepare a full-stack application. The description is designed for automatic discovery, but activation is not guaranteed by every runtime. You can explicitly ask the agent to use `fullstack-engineering`.

For substantial projects, ask it to populate `assets/project-brief-template.md`, create ADRs for important decisions, and use the definition-of-done checklist.

## Opinionated default profile

For a suitable new web application:
- TypeScript strict mode.
- Next.js App Router + React.
- Tailwind CSS.
- Node.js LTS.
- PostgreSQL for relational business data.
- Prisma or Drizzle selected based on fit.
- Zod or equivalent runtime schema validation.
- Native `fetch` for simple data access; TanStack Query when client cache/synchronization needs justify it.
- Modular monolith before microservices.

The agent must inspect the project and explain material deviations. This is not a requirement to migrate existing projects.

## Validate

Requires Python 3.10+ for the self-contained validator:

```bash
python scripts/validate_skill.py
python scripts/validate_skill.py --strict
python scripts/check_project.py /path/to/project
```

The validator checks frontmatter shape, required metadata, name/directory match, line count, local references, and basic package integrity. It is not a complete YAML parser or a replacement for the official `skills-ref validate` tool.

When installed, also run the official validator:

```bash
skills-ref validate ./fullstack-engineering
```

Review scripts before execution and run them with least privilege.

## Evaluation

Use `assets/evaluation-prompts.md` and `EVALUATION.md` to test relevant/irrelevant activation, quality, security, and regression behaviour. Suggested release gates are documented there.

## Customization

Keep universal engineering rules in `SKILL.md` and references. Put project-specific conventions in the repository's own instructions (for example `AGENTS.md`) rather than hardcoding them into this reusable skill. If you change the default stack, update this README and relevant references together.

## Versioning

Use semantic versioning for releases. Review changes like code: diff, validate, run evaluation scenarios, and document breaking behavioural changes in your release notes. Do not put a changelog in the skill body.

## Sources and further reading

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills repository: https://github.com/agentskills/agentskills
- VS Code Agent Skills documentation: https://code.visualstudio.com/docs/agent-customization/agent-skills
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
