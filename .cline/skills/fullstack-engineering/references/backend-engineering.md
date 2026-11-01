# Backend Engineering

## Responsibilities

Keep transport handlers thin. They should parse/validate input, establish trusted identity/context, call application use cases, and map results/errors to transport responses. Put business invariants in domain/application code, not in UI or route handlers.

## Reliability

- Validate all untrusted input at server boundaries.
- Use explicit timeouts, bounded retries, and backoff for transient external failures.
- Retry only operations safe to retry; use idempotency keys for payment/order/webhook workflows where appropriate.
- Use transactions for atomic database changes.
- Make asynchronous jobs idempotent and observable.
- Apply pagination and resource limits.
- Avoid leaking stack traces, secrets, SQL, or internal identifiers in public errors.
- Use structured logs with correlation/request IDs; redact sensitive fields.

## Integrations

Wrap vendor APIs behind small adapters. Handle authentication, timeouts, rate limits, schema drift, retries, and vendor outages. Verify webhooks cryptographically and protect against replay. Store vendor identifiers and event-processing state safely.

## Files

Validate file type using content/signature where possible, size, ownership, and authorization. Generate safe object names; store outside executable/public paths where appropriate; scan high-risk uploads; use short-lived signed URLs for private objects. Do not trust file extensions or client MIME headers alone.

## Background work

Use a queue when work is long-running, retryable, scheduled, or should not block a request. Define retry limits, dead-letter handling, idempotency, and operational visibility. Avoid introducing a queue for trivial synchronous work.
