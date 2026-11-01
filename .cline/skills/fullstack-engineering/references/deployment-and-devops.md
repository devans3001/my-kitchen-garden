# Deployment and DevOps

## Reproducibility

Document runtime/tool versions, package manager, lockfile, build, test, migration, and deployment commands. Pin dependencies through lockfiles. Keep development, staging, and production configuration distinct.

## Environments and secrets

Validate required environment variables at startup or build time as appropriate. Provide `.env.example` with placeholders only. Never commit real credentials. Restrict production secret access.

## CI/CD

Automate formatting/lint, type checks, tests, build, dependency/security checks, and migration validation. Use least-privilege pipeline credentials. Protect production deploys with appropriate approvals and branch policies.

## Releases

Use repeatable deployment steps, health checks, migration sequencing, smoke tests, and rollback plans. Prefer backward-compatible migrations and expand/contract changes. Avoid destructive migration-and-deploy coupling.

## Infrastructure

Choose managed services when they reduce operational burden and fit budget, reliability, data residency, and portability requirements. Track cost drivers, quotas, backups, and vendor lock-in. Do not provision paid resources without approval.

## Containers

Use minimal trusted base images, non-root users, pinned versions, health checks, and multi-stage builds when useful. Do not containerize by default if the platform already provides a simpler reliable deployment model.
