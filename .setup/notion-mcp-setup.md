# Notion MCP Server Setup

**Status**: ⏳ PENDING AUTHENTICATION - Server added, OAuth needed

## What's Done

✅ Notion MCP server added to Claude Code
✅ Configuration file updated at `~/.claude.json`
✅ Scope set to `user` (available across all projects)

## What's Needed - Authentication

### Complete OAuth Flow

1. Exit current Claude Code session
2. Start a new Claude Code session
3. Run `/mcp` command
4. Find "notion" in the list
5. Follow the OAuth prompt to authorize Notion workspace access
6. Grant permissions when prompted

### No API Keys Required

Unlike Google Calendar, Notion MCP is fully hosted and uses OAuth:
- No credentials files to download
- No API keys to manage
- No token expiry issues
- Just authenticate once and you're set

## What You'll Be Able to Do

Once authenticated, Claude can:
- Read and write Notion pages
- Search your workspace
- Create and update databases
- Query database entries
- Manage page properties
- Access all workspaces you're a member of

## Configuration Details

- **MCP Server URL**: `https://mcp.notion.com/mcp`
- **Transport**: HTTP (hosted by Notion)
- **Scope**: User-wide
- **Config location**: `~/.claude.json`

## Management Commands

- `/mcp`: List and manage installed MCP servers
- `/context`: Show token usage including MCP consumption

## Current Status

- [x] Add Notion MCP server via `claude mcp add`
- [x] Configure with user-wide scope
- [ ] Start new Claude session
- [ ] Run `/mcp` command
- [ ] Complete OAuth authorization
- [ ] Test Notion access

## Resources

- [Notion MCP Documentation](https://developers.notion.com/docs/get-started-with-mcp)
- [Official Notion MCP Server (GitHub)](https://github.com/makenotion/notion-mcp-server)
- [Notion's hosted MCP server blog](https://www.notion.com/blog/notions-hosted-mcp-server-an-inside-look)

## Installation Command Used

```bash
claude mcp add --transport http --scope user notion https://mcp.notion.com/mcp
```
