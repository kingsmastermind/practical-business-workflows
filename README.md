# Practical business workflows

Original reference examples by Robb Teneo: reliable intake, lead routing and visible human handoffs.

Written specifically for this public showcase with synthetic data. No production code, private infrastructure, client records or credentials are included.

## Demonstrated patterns

- Validate inquiries before queueing.
- Deduplicate repeated event deliveries.
- Route requests to sales or operations.
- Stop automated follow-up after opt-out, reply, booking or human handoff.
- Keep a readable event trail and test failure cases.

## Run locally

Node.js 18+; no dependencies, accounts or network calls.

```sh
node demo.mjs
node --test workflow.test.mjs
```

## Delivery areas

CRM and intelligent sales tools; fleet portals; membership and affiliate hubs; research workspaces; custom apps; commerce journeys; operational email systems.

This is a reference implementation, not a client repository or production service. Storage is in-memory. Deployment requires durable storage, authentication, monitoring and system-specific consent rules.
