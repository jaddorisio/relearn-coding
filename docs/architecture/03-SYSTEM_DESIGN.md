# System Design and Resilience

When shifting from single scripts to network-aware applications, failure changes from a "possibility" to a "guarantee". System design is the art of predicting and surviving those failures.

## Designing for Failure
- Assume the network is inherently hostile and fragile. 
- Build fault-tolerant systems that do not completely crash when a secondary dependency is offline.

## System Patterns
- **Circuit Breaker:** Wrap potentially failing remote network requests inside a breaker. If requests begin failing consistently, "open" the breaker to instantly fail-fast without hitting the downstream service. Allow the service time to recover, periodically testing it, before "closing" the breaker again.
- **Retry Pattern:** Remote connections (like database connections or API callbacks) usually suffer from transient faults. Apply retries with **exponential backoff** and "jitter" to avoid overwhelming the target service.
- **Idempotency:** Designing operations such that calling the exact same operation multiple times yields the exact same state end-result, rendering retrying perfectly safe.

## Understanding Scalability
- **CAP Theorem:** Any distributed data store can only simultaneously provide two of three guarantees:
  1. *Consistency*: Every read receives the most recent write or an error.
  2. *Availability*: Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
  3. *Partition tolerance*: The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network.
- **Graceful Shutdowns:** Applications must not aggressively panic. When a generic terminate signal (`SIGTERM`) is received, the app should finish in-flight requests, flush memory to disk, stop consuming queues, close DB connections cleanly, and *then* exit.

## Clean Architecture and DDD
- **Domain-Driven Design (DDD):** Align software abstractions directly with business terms. Use a Ubiquitous language meaning developers and business stakeholders use the exact same vernacular.
- **Bounded Contexts:** Large domain models must be broken down. "Billing" and "Shipping" might both have a concept of an "Account," but keeping them in their own separate walled-off contexts prevents giant monolith spaghetti.
