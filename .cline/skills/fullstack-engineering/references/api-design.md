# API Design

## Contract

Define resource names, methods, request/response schemas, auth requirements, error codes, pagination, filtering, sorting, rate limits, and versioning policy. Prefer predictable conventions over clever endpoints.

## Validation and errors

Validate path, query, headers, and body at the server boundary. Return stable machine-readable error codes with safe human-readable messages. Do not expose internals. Distinguish authentication, authorization, validation, conflict, not-found, rate-limit, and unexpected server errors.

## Semantics

Use HTTP methods/status codes consistently. Use `409 Conflict` for state conflicts where appropriate. Use `202 Accepted` for genuinely asynchronous work. Define idempotency for operations where clients or gateways may retry.

## Pagination

Prefer cursor pagination for large/changing datasets. Enforce maximum page sizes. Make sort order deterministic. Avoid unbounded list endpoints.

## Documentation

Document examples, schemas, auth, errors, limits, and webhook behaviour. Keep generated API docs aligned with implementation. For public APIs, consider compatibility and deprecation before breaking changes.
