"""
Remote MCP servers the dashboard can fill in for you (Settings → Agents that connect by URL): pick the app, paste its
token, done. Only servers whose official docs give a remote endpoint that takes a token in a header are listed, since
the gateway sends fixed headers and can't sign in through a browser (OAuth-only servers, like Notion's and Slack's
hosted ones, aren't here). Each entry says where its details come from; checked 7 Oct 2026.

Fields: name, category, url, header (name), value (what goes in it, with <TOKEN> where the token goes),
token (where to get it), note (anything a person must know), source.
"""
from __future__ import annotations

CATALOG: dict[str, dict] = {
    "github": {
        "name": "GitHub", "category": "Code", "url": "https://api.githubcopilot.com/mcp/",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "GitHub → Settings → Developer settings → Personal access tokens",
        "source": "https://github.com/github/github-mcp-server",
    },
    "stripe": {
        "name": "Stripe", "category": "Payments", "url": "https://mcp.stripe.com",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Stripe Dashboard → API keys → create an Agent API key",
        "note": "From 31 Oct 2026 Stripe's MCP server accepts only Agent API keys.",
        "source": "https://docs.stripe.com/mcp",
    },
    "linear": {
        "name": "Linear", "category": "Project management", "url": "https://mcp.linear.app/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Linear → Settings → Security & access → Personal API keys",
        "source": "https://linear.app/docs/mcp",
    },
    "atlassian": {
        "name": "Atlassian (Jira, Confluence)", "category": "Project management", "url": "https://mcp.atlassian.com/v2/mcp",
        "header": "Authorization", "value": "Basic <TOKEN>",
        "token": "Atlassian account → API tokens (a scoped token); the value is base64 of email:token",
        "note": "Your org admin must allow API-token sign-in. A service-account key goes as 'Bearer <key>' instead.",
        "source": "https://developer.atlassian.com/cloud/rovo-mcp/guides/configuring-authentication-via-api-token/",
    },
    "sentry": {
        "name": "Sentry", "category": "Observability", "url": "https://mcp.sentry.dev/mcp",
        "header": "Authorization", "value": "Sentry-Bearer <TOKEN>",
        "token": "Sentry → Settings → User Auth Tokens",
        "note": "Sentry uses 'Sentry-Bearer', not 'Bearer'.",
        "source": "https://github.com/getsentry/sentry-mcp",
    },
    "supabase": {
        "name": "Supabase", "category": "Database", "url": "https://mcp.supabase.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Supabase Dashboard → Account → Access Tokens",
        "note": "Add ?project_ref=<ref> to the URL to limit it to one project, &read_only=true to only read.",
        "source": "https://supabase.com/docs/guides/getting-started/mcp",
    },
    "neon": {
        "name": "Neon", "category": "Database", "url": "https://mcp.neon.tech/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Neon Console → Settings → API keys",
        "source": "https://neon.com/docs/ai/neon-mcp-server",
    },
    "cloudflare": {
        "name": "Cloudflare", "category": "Cloud", "url": "https://mcp.cloudflare.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Cloudflare Dashboard → My Profile → API Tokens",
        "source": "https://developers.cloudflare.com/agents/model-context-protocol/mcp-servers-for-cloudflare/",
    },
    "intercom": {
        "name": "Intercom", "category": "Support", "url": "https://mcp.intercom.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Intercom Developer Hub → your app → access token",
        "note": "EU workspaces: https://mcp.eu.intercom.com/mcp",
        "source": "https://developers.intercom.com/docs/guides/mcp",
    },
    "zapier": {
        "name": "Zapier", "category": "Automation", "url": "https://mcp.zapier.com/api/v1/connect",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "mcp.zapier.com → your server → Connect → Other → Generate token",
        "source": "https://docs.zapier.com/mcp/get-started/connect/other.md",
    },
    "make": {
        "name": "Make", "category": "Automation", "url": "https://eu2.make.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Make → Profile → API access → Add token (scope mcp:use)",
        "note": "Use your own zone in the URL, e.g. eu1.make.com or us2.make.com.",
        "source": "https://developers.make.com/mcp-server/connect-using-mcp-token",
    },
    "monday": {
        "name": "monday.com", "category": "Project management", "url": "https://mcp.monday.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "monday.com → your profile picture → Developers → My access tokens",
        "source": "https://github.com/mondaycom/mcp",
    },
    "airtable": {
        "name": "Airtable", "category": "Database", "url": "https://mcp.airtable.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "airtable.com/create/tokens (a personal access token)",
        "source": "https://airtable.com/developers/agents/mcp/getting-started",
    },
    "pagerduty": {
        "name": "PagerDuty", "category": "Observability", "url": "https://mcp.pagerduty.com/mcp",
        "header": "Authorization", "value": "Token token=<TOKEN>",
        "token": "PagerDuty → My Profile → User Settings → API Access → Create API User Token",
        "note": "PagerDuty uses 'Token token=', not 'Bearer'.",
        "source": "https://docs.pagerduty.com/developer/mcp-tooling-remote-server",
    },
    "context7": {
        "name": "Context7", "category": "Docs", "url": "https://mcp.context7.com/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "context7.com/dashboard",
        "source": "https://github.com/upstash/context7",
    },
    "exa": {
        "name": "Exa", "category": "Search", "url": "https://mcp.exa.ai/mcp",
        "header": "x-api-key", "value": "<TOKEN>",
        "token": "dashboard.exa.ai → API keys",
        "source": "https://exa.ai/docs/reference/exa-mcp",
    },
    "firecrawl": {
        "name": "Firecrawl", "category": "Search", "url": "https://mcp.firecrawl.dev/v2/mcp",
        "header": "Authorization", "value": "Bearer <TOKEN>",
        "token": "Firecrawl dashboard → API keys (fc-...)",
        "source": "https://docs.firecrawl.dev/mcp-server",
    },
}

# Official servers that run locally with a token (a laptop's agents via `squidbrake connect guard` / `proxy`, or a
# self-hosted gateway with SQUIDBRAKE_MCP_COMMANDS=1), and hosted ones that sign in only through a browser (OAuth),
# which the gateway can't do for you yet. Listed so people know where each stands.
LOCAL = ["Notion", "Square", "PayPal", "MongoDB", "Grafana", "Postgres", "Filesystem", "Playwright", "Brave Search",
         "Twilio"]
OAUTH_ONLY = ["Slack", "Notion (hosted)", "HubSpot", "Asana", "Vercel", "Figma", "ClickUp", "Google Workspace",
              "Salesforce (hosted)"]


def public() -> list[dict]:
    return [{"id": k, **v} for k, v in CATALOG.items()]
