# Architecture

## Default: modular monolith

Start with one deployable application and explicit internal modules. Separate deployables only when independent scaling, release cadence, fault isolation, regulatory boundaries, or team ownership justify the operational cost.

## Boundaries

Organize around business capabilities (for example: identity, catalog, ordering, billing), not only technical layers. Within a capability, keep domain rules, application use cases, and infrastructure adapters distinguishable where complexity warrants it.

A practical Next.js starting layout:

```text
src/
  app/                 # routes, layouts, route handlers
  modules/
    orders/
      domain/          # invariants and domain types
      application/     # use cases
      infrastructure/  # persistence and external adapters
      ui/              # feature components
  components/          # genuinely shared UI
  lib/                 # cross-cutting utilities
  config/
  server/
```

Adapt to the framework. Do not create empty layers or folders merely to imitate this example.

## Dependency direction

- Domain rules should not depend on UI frameworks, databases, or vendor SDKs.
- Application use cases orchestrate domain logic and ports/interfaces.
- Infrastructure implements persistence, messaging, storage, and vendor integrations.
- UI and transport layers translate inputs/outputs; they do not own core business rules.
- Avoid circular dependencies and hidden global mutable state.

## Decisions

For meaningful choices, record context, decision, alternatives, consequences, and revisit triggers in the ADR template. Examples: relational vs document database, modular monolith vs services, server actions vs REST, managed auth vs custom identity.

## Multi-tenancy

Decide tenancy model explicitly: shared database/shared schema, schema-per-tenant, or database-per-tenant. For most early SaaS products, shared relational tables with mandatory tenant ownership and strong enforcement are economical, but require rigorous query scoping and tests. Use database row-level security where suitable as defense in depth, not as a substitute for application authorization.

Never trust a tenant ID supplied only by a browser. Resolve the active tenant from authenticated membership and verify membership/role for every operation. Include tenant scope in unique constraints, cache keys, background jobs, object storage paths, exports, and audit events.

## Avoid

- Microservices without an operational need.
- Generic repository/service/factory layers that add indirection without value.
- Shared "utils" dumping grounds.
- Cross-module imports into another module's private internals.
- Premature event sourcing, CQRS, plugin systems, or distributed transactions.
