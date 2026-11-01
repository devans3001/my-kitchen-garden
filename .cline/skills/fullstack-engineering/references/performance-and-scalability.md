# Performance and Scalability

## Measure first

Establish user-visible performance goals and baseline measurements. Profile before optimizing. Identify whether the bottleneck is network, rendering, database, external service, CPU, memory, or queue throughput.

## Web performance

- Minimize unnecessary JavaScript and client components.
- Optimize images, fonts, caching, and critical rendering.
- Avoid waterfalls and duplicate requests.
- Use pagination and bounded payloads.
- Monitor Core Web Vitals where relevant.
- Test on realistic mobile devices and constrained networks.

## Backend and data

- Inspect query plans and add indexes for measured access patterns.
- Avoid N+1 queries, unbounded scans, and unbounded concurrency.
- Cache only with clear invalidation, tenant isolation, and staleness semantics.
- Use queues for long-running work when appropriate.
- Apply backpressure, timeouts, and resource limits.

## Scaling decisions

Scale vertically or tune existing services before adding distributed complexity. Introduce replicas, queues, caches, partitions, or service decomposition only when measurements and workload justify them. Model cost alongside latency and reliability.
