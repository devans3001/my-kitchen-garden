# Observability and Operations

## Signals

Instrument the service with:
- Structured logs with timestamp, severity, request/correlation ID, and useful context.
- Metrics for traffic, errors, latency, saturation, queue depth, and domain outcomes.
- Traces across service and external boundaries where complexity warrants it.

Avoid logging secrets, passwords, tokens, payment data, or unnecessary personal data.

## Alerting

Alert on actionable symptoms and user impact, not every transient event. Define severity, owner, runbook, and escalation for critical alerts. Monitor business-critical workflows such as checkout, login, order processing, and webhook delivery.

## Resilience

Define timeouts, retry budgets, circuit breaking where justified, graceful degradation, and recovery procedures. Ensure retries do not duplicate payments or other irreversible effects.

## Operations

Document health/readiness checks, backup schedules, restore tests, data retention, incident response, rollback, and vendor outage procedures. Define service objectives proportionate to business impact.
