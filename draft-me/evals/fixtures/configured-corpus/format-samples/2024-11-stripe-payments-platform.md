Stripe's recent writeup on the payments platform rewrite — the one where you moved the ledger to a cell-based architecture — was the most honest engineering post I'd read all year. The bit about choosing to slow down the rollout after the first cell hit a latency cliff told me more about your team than any job description would.

I'm a senior engineer at Acme, where I've spent the last four years on the infrastructure team. I built our distributed tracing system from scratch — OpenTelemetry on the collection side, a custom aggregation layer because the SaaS options couldn't handle our cardinality. It saved us roughly forty incidents last year that would have otherwise been diagnosed by gut feel. I've also led the migration from a monolithic Kafka cluster to a tiered setup across three regions; we held under 100ms p99 the whole time.

The thing I want to bring to Stripe is a bias for engineering that survives contact with real production. I'm not interested in clean architectures that work in a whiteboard session. I want systems that page oncall once a quarter and degrade gracefully when they do.

Here's what I'd want to dig into in my first week: where the payments-platform team's cell boundaries are costing the most operational complexity, and whether the ledger's consistency guarantees match what the product actually needs.

I'd love to talk.
