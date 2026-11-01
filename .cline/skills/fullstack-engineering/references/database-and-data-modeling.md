# Database and Data Modeling

## Choose deliberately

Use PostgreSQL by default for relational business domains, transactional workflows, reporting, and strong integrity. Choose document or key-value stores only when access patterns and data shape justify them. Do not choose based on trend.

## Model the domain

Identify entities, value objects, relationships, lifecycle/state transitions, ownership, invariants, and deletion/retention rules before tables. Normalize transactional data sensibly; denormalize only for measured read needs with a consistency strategy.

## Integrity

Use primary keys, foreign keys, unique constraints, check constraints, and non-null constraints to enforce invariants close to the data. Include tenant scope in uniqueness when the business rule is tenant-specific. Define cascade/restrict/set-null behaviour intentionally.

## Migrations

- Commit reproducible migrations.
- Review generated SQL for destructive or locking operations.
- Prefer expand-and-contract for zero/low-downtime changes.
- Back up and rehearse risky migrations.
- Do not reset or drop production data without explicit approval.
- Keep schema and application rollout compatibility in mind.

## Performance and concurrency

Index actual query patterns; consider selectivity and write overhead. Inspect query plans for expensive queries. Avoid N+1 and unbounded scans. Use transactions and appropriate isolation/locking for inventory, balances, counters, and competing updates. Use decimal/numeric types for money, never binary floating point.

## Data lifecycle

Define retention, deletion, anonymization, export, backup, restore, and audit requirements. Test restore procedures for critical systems. Avoid storing data without a clear purpose.
