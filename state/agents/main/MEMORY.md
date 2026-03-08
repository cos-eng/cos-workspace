# MEMORY.md — Active Context

## Last Updated: 2026-03-08T10:56:00+05:30

## Active Projects

_No active projects yet. First projects will be created when CEO Khilav delegates via Google Chat._

### Template for new projects

```text
### [Project Name] (SO-X)
- Status: Planning / In Progress / Review / Done
- Last Update: [date] — [summary]
- Blockers: [if any]
- Next Action: [what needs to happen]
- Owner: [team lead from ORG_CHART.md]
- Mission Control ID: [task ID]
- Linked SO: SO-X from SOUL.md
```

## Recent Decisions

_Log every CEO decision with date, rationale, and strategic impact._

- 2026-03-08: **Heartbeat check completed** — Regular 30-minute operational check at 10:56 AM IST. No new tasks in Mission Control, no calendar events in next 2 hours, no new files in Drive inbox. System operational. (SO-4: Operational Excellence)
- 2026-03-08: **Heartbeat check completed** — Regular 30-minute operational check at 10:26 AM IST. No new tasks in Mission Control, no calendar events in next 2 hours, no new files in Drive inbox. System operational. (SO-4: Operational Excellence)
- 2026-03-08: **Heartbeat check completed** — Regular 30-minute operational check at 9:56 AM IST. No new tasks in Mission Control, no calendar events in next 2 hours, no new files in Drive inbox. System operational. (SO-4: Operational Excellence)
- 2026-03-07: **Blog post on "Set and Forget AI Lie" completed** — Ghostwriter agent wrote comprehensive 1130-word blog post in CEO Khilav's "Reality-Check Visionary" voice. Post uploaded to Google Drive `/CoS-Shared/drafts/` for review and notification sent via Google Chat. Content covers AI deployment realities with practical framework. (SO-1: Product & AI Transformation)
- 2026-03-07: **Enforced delegation discipline** — Corrected operational behavior to ALWAYS delegate research tasks to Intel Analyst agent (per HEARTBEAT.md rules), even for direct requests. Research on Bajaj Finance properly delegated after initial oversight. (SO-4: Operational Excellence)
- 2026-03-07: **State Sync to GitHub implemented** — Created `cos-eng/cos-workspace` repository, deployed sync script that copies MEMORY.md and knowledge files every 6 hours for disaster recovery. This addresses the "State sync to GitHub" backlog item from PLANNING.md. (SO-4: Operational Excellence)
- 2026-03-06: Researched the impact of Google's Privacy Sandbox on Indian e-commerce. Key finding: Small to medium businesses relying on third-party cookies are most affected. The Alliance of Digital India Foundation (ADIF) is actively challenging the change.
- 2026-03-06: Drafted and staged a LinkedIn post regarding the AI Chief of Staff initiative. The draft is pending review in the shared Drive folder.
- 2026-03-07: Responded to query on cookie deprecation by spawning Intel Analyst for research. Report delivered successfully.
- 2026-03-07: Clarified that the entire agent swarm uses Google Gemini 2.5 Pro, and no DeepSeek API key is configured.
- 2026-03-07: **Created internal Slack announcement for AI Chief of Staff deployment** — Wrote a 3-line message in CEO's voice (direct, data-driven with warm humor) announcing the 4-agent system launch. Message highlights time-saving benefits and AI transformation journey (SO-1). Deliverable saved to project directory.
- 2026-03-07: **Sent professional team email announcing AI Chief of Staff deployment** — Delivered 185-word email to team@liftsuggest.com (Message ID: 19cc9c539b09e3cf) and test confirmation to khilav@tatvic.com. Email successfully sent after resolving Mission Control agent assignment issue (task was incorrectly assigned to Tester Agent instead of Ghostwriter for 12+ hours). Manual reassignment and completion logged. (SO-1: Product & AI Transformation)
- 2026-03-05: CoS multi-agent system deployed to GCP VM. Gateway pairing resolved. All agent knowledge files deployed.

## Stakeholder Sentiment

_Track client relationship temperature. Cross-reference with CLIENT_STAKEHOLDERS.md._

| Client | Stakeholder | Sentiment | Last Contact | Notes |
|--------|------------|-----------|-------------|-------|
| _To be populated as interactions occur_ | | | | |

```text
Sentiment levels:
- Champion — actively advocates, strong relationship
- Neutral — standard engagement, no strong signal
- At Risk — delayed renewals, reduced engagement, negative signals
```

## Pending Approvals

_Items waiting for CEO sign-off. Clear these in Daily Briefing §1._

| Item | Context | Drive Link | Date Added |
|------|---------|-----------|-----------|
| LinkedIn Post: AI CoS | Draft of a post for Khilav's LinkedIn about the AI Chief of Staff initiative. | https://drive.google.com/file/d/1Z0kdILgMFUOERl3BieMtuWmgBrWA98W1/view | 2026-03-06 |
| _None currently_ | | | |

## Key Context

_Important context that persists across sessions. This is the recovery point if the VM crashes._

### System Configuration

- **CoS system live:** 2026-03-05
- **Primary model:** Google Gemini 2.5 Pro
- **Service account:** <cos@liftsuggest.com>
- **Gateway:** ws://127.0.0.1:18789 (loopback via Nginx)
- **Control UI:** <http://35.200.184.122:18789>
- **Mission Control:** `http://mission-control:4000` _(Docker internal; external: <http://35.200.184.122:4000>)_
- **VM:** cos-vm (GCP e2-medium, asia-south1-a)
- **Gateway version:** OpenClaw 2026.3.3
- **Access restricted to:** 103.233.171.30/32 (Tatvic IP)

### Known Issues

- **Mission Control Agent Assignment Bug (2026-03-07):** The workflow template `tpl-strict` incorrectly reassigned a CEO email task from Ghostwriter to Tester Agent, causing a 12+ hour delay. Manual intervention required to reassign and complete the task. This indicates a conflict between CoS agent routing and Autensa workflow templates. (SO-4: Operational Excellence)
- **[RESOLVED 2026-03-08] Critical Cron Scheduler Failure** — All 7 cron jobs have been created and are now active. Jobs include: Client News Scan (2:00 AM), LinkedIn Tracking (3:00 AM), Team Progress Sync (4:00 AM), Calendar Prep (5:00 AM), Briefing Assembly (6:30 AM), Briefing Delivery (7:00 AM), and State Sync (every 6h). The scheduler shows 7 jobs enabled with next wake at State Sync. (SO-4: Operational Excellence)
- **Team Progress Sync Cron Failure (2026-03-07):** The scheduled 4:00 AM IST cron job for team progress failed. The sub-agent reported that the `mission-control` hostname was not resolvable, preventing it from accessing the API. This is a critical Docker networking/service discovery issue.
- **LinkedIn Tracking Cron Failure (2026-03-06):** The scheduled 3:00 AM IST cron job for LinkedIn tracking failed with an unknown error. The other cron jobs for news scanning and team progress are still running. Unable to access sub-agent logs for detailed diagnostics due to security policies. This may indicate an issue with the headless browser, as LinkedIn tasks are dependent on it. Monitoring remaining crons.
- **Intel Analyst research failure (2026-03-06):** Sub-agent failed a research task on MarTech funding. All web access tools (`web_search`, `curl`, `browser`) failed due to configuration and system instability. Escalated to Lakshin.
- **`browser` tool instability (2026-03-06):** The `browser` tool failed to start with a Chrome CDP error during a research task. Root cause needs investigation.
- **[RESOLVED] GOG CLI functional.** The GOG CLI is fully configured and functional. The previously noted keyring password issue is resolved. All connectivity checks passed on 2026-03-06.
- **[RESOLVED 2026-03-06] Gemini API Key Expired** — User confirmed the API key has been updated and the issue is resolved.
- ✅ **[RESOLVED 2026-03-06] ORG_CHART.md and DIRECT_REPORTS.md populated** — Real org data from Mar 26 org structure file. 21 teams, 5 CEO direct reports, full reporting hierarchy.
- PROSPECT_LIST.md data is populated (6 prospects with priority levels)
- SOUL.md Strategic Objectives need validation from CEO (currently has inferred SOs)
- **[RESOLVED 2026-03-06] Agent tool restructuring** — All agent docs updated to use `web_fetch` as primary research tool instead of `web_search`. Playwright browser for LinkedIn/dynamic pages. `web_search` (Brave API) is NOT configured and NOT used.

### What Has Been Set Up

- ✅ All 4 agents configured (Orchestrator, Intel Analyst, Operator, Ghostwriter)
- ✅ Firewall rules restricted to Tatvic home IP
- ✅ Gateway pairing resolved
- ✅ Knowledge files deployed (CLIENT_LIST.md, CLIENT_STAKEHOLDERS.md)
- ✅ Template files deployed (ORG_CHART.md, DIRECT_REPORTS.md, PROSPECT_LIST.md)
- ✅ Agent knowledge files restructured (web_fetch + Playwright, detailed SOPs)
- ⬜ Google Chat integration (pending 401 fix)
- ⬜ Daily Briefing cron schedule (pending Chat integration)
- ⬜ Mission Control task board setup
- ✅ GOG CLI configuration
- ✅ **State sync to GitHub** — Repository `cos-eng/cos-workspace` created, sync script deployed (2026-03-07)

## Lessons Learned

_Things that worked, things that didn't. Update after significant events._

- **Mission Control Workflow Conflict (2026-03-07):** The `tpl-strict` workflow template in Mission Control overrides correct agent assignments, reassigning CoS tasks to Autensa agents (e.g., Ghostwriter → Tester Agent). Need to either: 1) Use different workflow templates for CoS tasks, or 2) Monitor and manually correct assignments. (SO-4: Operational Excellence)
- **Delegation discipline (2026-03-07):** Research tasks should ALWAYS be delegated to Intel Analyst agent, even for direct requests (not just Mission Control tasks). Orchestrator should follow HEARTBEAT.md delegation rules consistently: research → Intel Analyst, content → Ghostwriter, data/ops → Operator.
- **`gog` CLI syntax updated (2026-03-06):** The `gog` CLI tool's syntax in `TOOLS.md` was incorrect for `drive ls` and `drive download`. The documentation was corrected after discovering the correct syntax via `--help`. Positional arguments are used for file IDs instead of flags.
- **`gog drive download` behavior (2026-03-06):** The `gog drive download <fileId>` command downloads the file to a local path in `~/.config/gogcli/drive-downloads/` instead of printing to stdout. The workflow must be: `download` then `read`.
- Gateway pairing error resolved by restarting the gateway container after approving pairing in UI
- Rate limit on auth attempts triggered by repeated connection attempts — gateway restart clears it
- `dangerouslyDisableDeviceAuth: true` only affects browser UI connections, not agent-gateway WebSocket
- File ownership on VM must be `ubuntu:ubuntu` for the container to read them (Docker user mapping)
- **web_search requires Brave API key** — not configured. All research routed to `web_fetch` (URL-based) as primary tool. Playwright browser used for JavaScript-rendered pages (LinkedIn). This is a deliberate architecture choice, not a workaround.

## Update Rules

**CRITICAL:** Update this file after EVERY significant interaction. This includes:

- CEO decisions (with rationale)
- Delegated tasks and their status
- Project status changes
- New context learned
- Escalation outcomes
- Client sentiment shifts
- System configuration changes

If the VM crashes, MEMORY.md is the recovery point. Keep it current.
