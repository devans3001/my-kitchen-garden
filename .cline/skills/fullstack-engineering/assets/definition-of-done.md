# Definition of Done

Tailor this checklist to the scope; mark not applicable items with a reason.

## Product
- [ ] Acceptance criteria are met.
- [ ] Business rules and state transitions are correct.
- [ ] Empty, loading, success, failure, and permission states are handled where relevant.

## Engineering
- [ ] Changes follow repository conventions and have clear boundaries.
- [ ] No unnecessary dependencies or unrelated refactors were introduced.
- [ ] Types, validation, and error handling are appropriate.
- [ ] Migrations are reviewed and safe for the rollout plan.

## Security and data
- [ ] Server-side authorization is enforced.
- [ ] Tenant/resource boundaries are tested where applicable.
- [ ] Secrets and sensitive data are not exposed.
- [ ] Inputs, uploads, webhooks, and external integrations are handled safely.

## Quality
- [ ] Relevant unit/integration/E2E tests pass.
- [ ] Lint, type-check, and build checks pass where configured.
- [ ] Important negative and edge cases are tested.
- [ ] Diff reviewed for regressions and unintended changes.

## UX and accessibility
- [ ] Responsive behaviour is verified.
- [ ] Keyboard and semantic accessibility are considered.
- [ ] Feedback, validation, and recovery are understandable.

## Operations and handover
- [ ] Required configuration is documented.
- [ ] Logs/metrics/alerts are appropriate to risk.
- [ ] Deployment, migration, backup, and rollback needs are documented.
- [ ] Known limitations and unrun checks are disclosed.
