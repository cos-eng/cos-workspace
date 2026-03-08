# CoS Workspace - State Sync Repository

This repository stores synchronized state from the CoS (Chief of Staff) multi-agent system.

## Purpose

- **Disaster Recovery:** If the VM crashes, restore state from this repo
- **Version History:** Track changes to MEMORY.md and knowledge files over time
- **Audit Trail:** Maintain a record of CEO decisions, project status, and stakeholder sentiment

## Structure

```
cos-workspace/
├── state/
│   ├── agents/
│   │   ├── main/          # Orchestrator state (MEMORY.md, etc.)
│   │   ├── intel-analyst/ # Intel Analyst state
│   │   ├── operator/      # Operator state
│   │   └── ghostwriter/   # Ghostwriter state
│   └── knowledge/         # Shared knowledge files (CLIENT_LIST.md, etc.)
├── scripts/              # Sync utilities and automation
└── README.md            # This file
```

## Sync Schedule

| Frequency | What Gets Synced | When |
|-----------|------------------|------|
| Every 6 hours | Dynamic state files (MEMORY.md, knowledge files) | 00:00, 06:00, 12:00, 18:00 UTC |
| On change | Static config files (SOUL.md, HEARTBEAT.md, etc.) | Manual trigger |

## Files Synced

### Dynamic State (Every 6h)
- `MEMORY.md` — Active context, decisions, project status
- `CLIENT_LIST.md` — Client database
- `PROSPECT_LIST.md` — Target companies
- `CLIENT_STAKEHOLDERS.md` — Key contacts and sentiment
- `ORG_CHART.md` — Team structure
- `DIRECT_REPORTS.md` — CEO's direct reports

### Static Config (On Change)
- `SOUL.md` — CEO's operating system
- `HEARTBEAT.md` — Operational rhythm
- `TOOLS.md` — Tool reference
- `IDENTITY.md` — Agent identity
- `USER.md` — CEO profile
- `AGENTS.md` — System overview

## Recovery Process

If the VM crashes:

1. Clone this repo to new VM
2. Copy files from `state/agents/main/` to agent workspace
3. Copy files from `state/knowledge/` to shared workspace
4. Restart CoS agents

## Last Sync
2026-03-08 05:49:22 UTC — Updated automatically by sync script
2026-03-07 06:49:26 UTC — Updated automatically by sync script