# Project Planning

## Discovery checklist

Establish:
- Problem, target users, jobs-to-be-done, and measurable outcome.
- Actors, roles, permissions, and organization/tenant model.
- Core workflows and state transitions.
- Functional scope, exclusions, and acceptance criteria.
- Data classification, retention, privacy, and regulatory constraints.
- Integrations, reliability expectations, traffic assumptions, and operational ownership.
- Budget, team capability, deadline, hosting and data residency constraints.

## Requirements quality

Write requirements so they are observable and testable. Avoid vague statements such as "fast", "secure", "intuitive", or "scalable" without measurable or reviewable criteria.

For each critical workflow capture:
1. Starting state and actor.
2. Preconditions and authorization.
3. Main success path.
4. Validation and failure paths.
5. Side effects and notifications.
6. State changes and audit requirements.
7. Acceptance tests.

## Scope

Separate must-have, should-have, later, and explicitly out-of-scope. Identify assumptions and unresolved questions. Prefer the smallest end-to-end slice that validates the product's core value.

## Risk-first planning

Prioritize unknowns involving money, identity, privacy, data migration, vendor dependency, concurrency, and irreversible actions. Prototype risky integrations early in sandbox environments.

## Estimate responsibly

Use task ranges and dependencies rather than false precision. Call out external blockers and uncertainty. Never promise a date based only on code-generation speed.
