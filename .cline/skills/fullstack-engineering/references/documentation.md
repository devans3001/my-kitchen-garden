# Documentation and Handover

Keep documentation close to the code and update it when behaviour changes.

## Minimum useful documentation

- README: purpose, prerequisites, setup, environment, common commands, tests, deployment pointer.
- Architecture overview: modules, data flow, external dependencies, trust boundaries.
- ADRs: significant decisions and alternatives.
- API contracts: endpoints, schemas, auth, errors, webhooks.
- Operations: deploy, migrate, backup/restore, monitoring, incident and rollback procedures.
- User-facing docs: only where the product needs them.

## Writing standard

Be concise, accurate, and runnable. Distinguish required from optional configuration. Never include real secrets or fabricated command output. Mark known limitations and version assumptions. Prefer diagrams for complex flows, but keep source representations version-controlled.
