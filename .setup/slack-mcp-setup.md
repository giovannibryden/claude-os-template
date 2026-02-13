# Slack MCP Server Setup - In Progress

**Status**: Waiting for IT approval for Slack app creation

## What's Done

✅ Slack MCP server added to Claude Code via `claude mcp add`
✅ Configuration file created at `~/.claude.json`

## What's Needed

### 1. IT Approval
Request approval from IT team to create a Slack app with these scopes:
- `channels:history` (read channel messages)
- `channels:read` (list channels)
- `chat:write` (post messages)
- `reactions:write` (add emoji reactions)
- `users:read` (list users)
- `users.profile:read` (get user profiles)

### 2. Once Approved - Create Slack App

1. Go to https://api.slack.com/apps
2. Click "Create New App" → "From scratch"
3. Name it: "Claude Assistant" (or similar)
4. Select workspace: Mixpanel workspace

### 3. Configure Permissions

In the Slack app settings:
1. Go to "OAuth & Permissions"
2. Under "Bot Token Scopes", add all scopes listed above
3. Click "Install to Workspace"
4. Authorize the app
5. Copy the **Bot User OAuth Token** (starts with `xoxb-`)

### 4. Get Team ID

1. In Slack, click workspace name → "Settings & administration" → "Workspace settings"
2. Find the Workspace ID (starts with `T`) in the URL or settings page

### 5. Add Credentials to Configuration

Edit `~/.claude.json` and add to the slack server's `env` section:

```json
"slack": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@zencoderai/slack-mcp-server"],
  "env": {
    "SLACK_BOT_TOKEN": "xoxb-your-token-here",
    "SLACK_TEAM_ID": "T-your-team-id-here"
  }
}
```

### 6. Restart & Test

1. Restart your Claude Code session
2. Test by asking Claude to list Slack channels or post a test message

## Current Config Location

`~/.claude.json` - Slack MCP server entry exists but needs environment variables

## Resources

- [Zencoder Slack MCP GitHub](https://github.com/zencoderai/slack-mcp-server)
- [Slack Apps Portal](https://api.slack.com/apps)
- [Slack API Documentation](https://api.slack.com/docs)

## Notes

- Using **bot token** approach (not user token) - messages will appear from bot, not your personal account
- Bot is more secure and follows Slack best practices
- Bot will need to be invited to channels you want it to access
