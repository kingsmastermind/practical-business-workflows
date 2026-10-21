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

First clone the repository and enter its folder. Running the commands from your home folder will produce `MODULE_NOT_FOUND`.

```sh
git clone https://github.com/kingsmastermind/practical-business-workflows.git
cd practical-business-workflows
node demo.mjs
node --test workflow.test.mjs
```

## Delivery areas

CRM and intelligent sales tools; fleet portals; membership and affiliate hubs; research workspaces; custom apps; commerce journeys; operational email systems.

This is a reference implementation, not a client repository or production service. Storage is in-memory. Deployment requires durable storage, authentication, monitoring and system-specific consent rules.

## What you will see

The terminal prints an accepted synthetic inquiry, its operations routing, a human-handoff transition, and an event trail. The tests verify duplicate handling and safe follow-up stops. This example does not send messages, connect to a CRM, or display a dashboard.

Already on Robb's M1? Run `node /Users/kingsmastermind/dev/robb-teneo-workflow-showcase/demo.mjs` from any folder.
