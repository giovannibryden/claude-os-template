# Google Calendar MCP Server Setup

**Status**: ✅ COMPLETE - Authenticated and ready to use

## What's Done

✅ Google Calendar MCP server added to Claude Code via `claude mcp add`
✅ Configuration file created at `~/.claude.json`

## What's Needed - Google Cloud Setup

### 1. Create Google Cloud Project & Enable Calendar API

1. Go to https://console.cloud.google.com/
2. Create a new project (or use existing)
3. Enable the Google Calendar API:
   - Go to "APIs & Services" → "Library"
   - Search for "Google Calendar API"
   - Click "Enable"

### 2. Create OAuth 2.0 Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "OAuth client ID"
3. If prompted, configure OAuth consent screen first:
   - User Type: Internal (if Mixpanel workspace) or External
   - Add your email as test user
   - Scopes: Add `https://www.googleapis.com/auth/calendar`
4. Application type: **Desktop app**
5. Name it: "Claude Calendar Access" (or similar)
6. Click "Create"
7. **Download the JSON file** - this is your credentials file

### 3. Add Credentials to Configuration

Edit `~/.claude.json` and add the path to your credentials file:

```json
"google-calendar": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@cocal/google-calendar-mcp"],
  "env": {
    "GOOGLE_OAUTH_CREDENTIALS": "/path/to/your/gcp-oauth.keys.json"
  }
}
```

**Recommended location for credentials file**:
`~/.config/google-calendar-mcp/credentials.json`

### 4. First-Run Authentication

After adding credentials path:

```bash
export GOOGLE_OAUTH_CREDENTIALS="/path/to/your/gcp-oauth.keys.json"
npx @cocal/google-calendar-mcp auth
```

This will:
- Open browser for OAuth flow
- Ask you to authorize calendar access
- Save access token locally

### 5. Restart Claude Session

After authentication, restart your Claude Code session to activate the calendar integration.

## What You'll Be Able to Do

Once set up, Claude can:
- Check your calendar availability
- Find free time slots
- Schedule meetings
- Detect conflicts
- Create/update/delete events
- Manage multiple calendars
- Handle recurring events

## Token Expiry

**Test mode**: OAuth tokens expire after 7 days, requiring re-authentication

**To avoid weekly re-auth**: Publish your app in Google Cloud Console OAuth consent screen (doesn't require verification for personal use)

## Resources

- [GitHub: google-calendar-mcp](https://github.com/nspady/google-calendar-mcp)
- [Google Cloud Console](https://console.cloud.google.com/)
- [Google Calendar API Docs](https://developers.google.com/calendar/api)

## Current Status

- [x] Create Google Cloud project
- [x] Enable Calendar API
- [x] Create OAuth credentials
- [x] Download credentials JSON
- [x] Add credentials path to ~/.claude.json
- [x] Run authentication flow
- [ ] Restart Claude session to activate
- [ ] Test calendar access

**Credentials location**: `~/.config/google-calendar-mcp/credentials.json`
**Tokens location**: `~/.config/google-calendar-mcp/tokens.json`
**Both files added to .gitignore**: ✅
