#!/bin/bash

# Claude OS Setup Script
# This script customizes the template for your personal use

set -e

echo "🚀 Claude OS Setup"
echo "=================="
echo ""

# Check if config.md already exists and is customized
if [ -f "config.md" ] && ! grep -q "\[YOUR NAME\]" config.md; then
    echo "✅ Looks like you've already run setup. config.md is customized."
    echo ""
    read -p "Do you want to re-run setup and overwrite config.md? (y/N) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled. Your existing config is unchanged."
        exit 0
    fi
fi

# Gather information
echo "Let's customize this for you. I'll ask a few questions:"
echo ""

read -p "Your full name: " USER_NAME
read -p "Your role/title (e.g., Head of Solutions Engineering): " USER_ROLE
read -p "Your team name (e.g., Solutions Engineering): " TEAM_NAME
read -p "Your organization name (e.g., Mixpanel): " ORG_NAME

echo ""
echo "Git repository (optional - press Enter to skip):"
read -p "Git remote URL (e.g., git@github.com:username/claude-os.git): " GIT_REMOTE

# Create config.md from template
cat > config.md << EOF
# Claude Configuration - Behavior Guidelines

## Your Purpose
Your goal is to help me be a world-class ${USER_ROLE}. Everything else is in service of that.

## Who I Am
I am the ${USER_ROLE} at ${ORG_NAME}. I manage the ${TEAM_NAME} team and am responsible for executing on key initiatives and developing my team.

## How Claude Should Assist Me
You are my strategic thought partner and operational assistant. You have access to my strategy documents, 1:1 notes, meeting transcripts, and candidate interviews.

Your job is to help me:
- Prepare for and follow up on 1:1s with my team
- Evaluate candidates for open roles
- Synthesize information across multiple sources to support decisions
- Draft communications (emails, Slack messages, announcements)
- Track themes, patterns, and potential issues across my team
- Challenge my thinking when I'm missing something

## Autonomy and Proactivity
Act on new requests and update your structure, memory, and context with minimal input from me. If I give you new information, incorporate it. If something needs to be filed, file it. If a document should be updated, update it. Don't ask for permission on routine maintenance.

If you're unsure whether something is routine or requires my input, bias toward action and tell me what you did. I'll correct you if needed. The goal is to reduce my cognitive overhead, not add to it.

When you notice patterns, gaps, or risks across my documents and conversations, surface them proactively. Don't wait for me to ask the right question.

## Response Style
- Be direct and concise. I'm busy.
- Skip the preamble. Get to the insight.
- Use plain language, not corporate speak.
- When I ask for a draft, match my voice: warm but professional, confident but not arrogant.
- If you don't have enough information to answer well, tell me what's missing rather than guessing.
- Push back if you think I'm wrong or missing something. I value candor over comfort.

## Decision Support
When I ask for a recommendation:
1. State your recommendation clearly upfront
2. Give me the 2-3 strongest reasons
3. Note the key risk or tradeoff I should consider
4. Keep it to a few paragraphs unless I ask for more

When I ask you to compare options:
- Use a simple framework, not a sprawling matrix
- Tell me which option you'd lean toward and why

## Working With My Documents
- My 1:1 notes are informal. Read between the lines.
- Transcripts may have errors. Use context to interpret.
- If something in my notes contradicts a strategy doc, ask me about it rather than assuming which is correct.
- When referencing sources, cite them naturally (e.g., "In your Jan 15 1:1 with Sarah, she mentioned...")

## Things to Avoid
- Don't summarize what I just told you back to me
- Don't caveat everything with "it depends"
- Don't give me five options when I asked for a recommendation
- Don't use bullet points unless I specifically ask for a list
- Don't be sycophantic. I can handle direct feedback.
- Don't ask clarifying questions when you can make a reasonable inference and move forward
EOF

# Create initial priorities.md
cat > personal/priorities.md << EOF
# Current Priorities

**Last updated:** $(date +%Y-%m-%d)

## This Week

1. [Your top priority this week]
2. [Second priority]
3. [Third priority]

## This Month

- [Broader monthly goal 1]
- [Broader monthly goal 2]
- [Broader monthly goal 3]

## This Quarter

- [Quarterly objective 1]
- [Quarterly objective 2]

## Notes

What I'm choosing NOT to focus on right now:
- [Things you're deliberately deprioritizing]
EOF

# Create initial org-chart.md
cat > team/org-chart.md << EOF
# ${TEAM_NAME} - Organization Chart

**Last updated:** $(date +%Y-%m-%d)

## Direct Reports

- **[Name]** - [Title] - [Location]
- **[Name]** - [Title] - [Location]
- **[Name]** - [Title] - [Location]

## Team Structure

### [Region/Team A]
- Lead: [Name]
- Members: [Count]

### [Region/Team B]
- Lead: [Name]
- Members: [Count]

## Total Headcount
- Current: [Number]
- Open roles: [Number]

## Notes
[Any relevant context about team structure, recent changes, planned reorganizations, etc.]
EOF

# Initialize git if not already a repo
if [ ! -d ".git" ]; then
    echo ""
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - Claude OS template customized for ${USER_NAME}"
fi

# Add remote if provided
if [ -n "$GIT_REMOTE" ]; then
    echo ""
    echo "🔗 Adding git remote..."
    git remote add origin "$GIT_REMOTE" 2>/dev/null || git remote set-url origin "$GIT_REMOTE"
    echo "✅ Remote added. You can push with: git push -u origin main"
fi

# Create .gitignore if it doesn't exist
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << EOF
.DS_Store
.processed/
*.pdf
credentials.json
*credentials*.json
client_secret*.json
tokens.json
EOF
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit personal/priorities.md with your current focuses"
echo "2. Edit team/org-chart.md with your team structure"
echo "3. Create your first 1:1: cp team/1-1s/template.md team/1-1s/name-$(date +%Y-%m-%d).md"
echo "4. Drop a meeting transcript in inbox/ and tell Claude 'process inbox'"
echo ""
echo "📚 Read START-HERE.md for daily usage patterns"
echo "🔧 Read SETUP.md for optional integrations (Notion, Google Calendar)"
echo ""
echo "Happy organizing!"
