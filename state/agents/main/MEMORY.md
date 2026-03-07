# MEMORY.md — Active Context

## Last Updated: 2026-03-05T22:30:00+05:30

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

- 2026-03-06: Researched the impact of Google's Privacy Sandbox on Indian e-commerce. Key finding: Small to medium businesses relying on third-party cookies are most affected. The Alliance of Digital India Foundation (ADIF) is actively challenging the change.
- 2026-03-06: Drafted and staged a LinkedIn post regarding the AI Chief of Staff initiative. The draft is pending review in the shared Drive folder.
- 2026-03-07: Responded to query on cookie deprecation by spawning Intel Analyst for research. Report delivered successfully.
- 2026-03-07: Clarified that the entire agent swarm uses Google Gemini 2.5 Pro, and no DeepSeek API key is configured.
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

- **Critical Cron Scheduler Failure (2026-03-07):** The master scheduler failed to trigger any of the overnight cron jobs (Client News, LinkedIn, Team Progress). No sub-agents were spawned. This resulted in a total failure to assemble the 7:00 AM Daily Briefing. This is a high-priority system outage.
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
- ⬜ State sync to GitHub

## Lessons Learned

_Things that worked, things that didn't. Update after significant events._

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
