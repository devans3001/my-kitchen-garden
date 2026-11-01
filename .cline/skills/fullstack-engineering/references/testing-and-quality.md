# Testing and Quality

## Test pyramid

Use a balanced mix:
- Unit tests for pure domain rules, calculations, validation, and edge cases.
- Integration tests for persistence, transactions, APIs, queues, and vendor adapters.
- End-to-end tests for critical user journeys and authorization boundaries.
- Contract tests where independently deployed systems exchange data.

Do not maximize test count at the expense of meaningful coverage.

## Test design

For each critical workflow test:
- Happy path.
- Invalid input and boundary values.
- Unauthenticated and unauthorized actors.
- Missing/deleted/foreign-owned resources.
- Duplicate submissions and retries.
- Concurrency and partial failure where relevant.
- Empty, loading, timeout, and external-service failure states.

Use deterministic fixtures and isolate tests from production data. Avoid brittle tests coupled to implementation details.

## Quality gates

Run repository-native checks, typically:
1. Formatter/linter.
2. Type checker.
3. Focused unit/integration tests.
4. Relevant end-to-end tests.
5. Production build.
6. Security/dependency checks appropriate to risk.

Do not invent commands; inspect package scripts and project docs. Report skipped checks.

## Change review

Inspect the diff, test coverage, migrations, generated files, dependency changes, logs, permissions, and accessibility. Confirm that tests actually exercise the changed behaviour.

## Definition of done

Use `assets/definition-of-done.md` and tailor it to the task. A green build is necessary in many projects but never sufficient by itself.
