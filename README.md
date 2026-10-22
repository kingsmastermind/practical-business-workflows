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


## Guided product walkthrough

Open index.html or the GitHub Pages site. The former generic button demonstration was removed after operator review. The replacement is a silent 48-second guided video using existing synthetic-data product demonstration captures, animated camera framing, on-screen takeaways and synchronized below-player guidance. It does not depict live product actions.

Use `?audience=application` to omit the booking link. No narration or audio track. Review platform link rules before submission.
