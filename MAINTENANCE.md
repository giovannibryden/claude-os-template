# Maintenance Guide for Template Maintainers

This document is for people maintaining the blessed version of the Claude OS template.

## Release Process

### When to Release

- Monthly: Minor improvements, new templates, workflow additions
- Quarterly: Major structural changes, new features
- As needed: Critical bug fixes, documentation updates

### Versioning

Use semantic versioning:
- **Major (1.0, 2.0):** Breaking changes to structure or setup
- **Minor (1.1, 1.2):** New features, templates, workflows
- **Patch (1.1.1, 1.1.2):** Bug fixes, doc updates

### Release Checklist

- [ ] Update version in README.md
- [ ] Update CHANGELOG.md with changes
- [ ] Test SETUP.sh on clean installation
- [ ] Review all documentation for accuracy
- [ ] Tag release in git: `git tag v1.1.0`
- [ ] Push tag: `git push origin v1.1.0`
- [ ] Create GitHub release with notes

## Managing Contributions

### Reviewing PRs

Check for:
1. **Broad applicability** - Will this help most users?
2. **Simplicity** - Does it maintain the low-friction philosophy?
3. **Documentation** - Is it clearly explained?
4. **Testing** - Has the contributor tested it?
5. **Style** - Does it match existing tone and format?

### Merging Guidelines

- Require at least one approval
- Test locally before merging
- Update CHANGELOG.md in the same PR or immediately after
- Thank contributors in the merge message

### Declining Contributions

When saying no:
- Be kind and explain why
- Suggest alternatives if possible
- Encourage them to use it in their personal fork
- Leave the door open for revised versions

## Managing Issues

### Triage Process

Label issues promptly:
- **bug** - Something broken
- **enhancement** - New feature request
- **documentation** - Doc improvements
- **question** - Help needed
- **wontfix** - Not aligned with goals
- **good first issue** - Easy for newcomers

### Response Times

- Acknowledge new issues within 48 hours
- Provide initial response to questions within 3 days
- Review PRs within 1 week

## Template Quality Standards

### Code Quality

- SETUP.sh must be POSIX-compliant (work on bash/zsh)
- All paths should use forward slashes
- Scripts should handle errors gracefully
- Test on macOS and Linux

### Documentation Quality

- Clear, direct language
- Real examples over abstract descriptions
- Consistent tone across all docs
- No broken links
- Spell-checked and grammar-checked

### Template Quality

- Generic (no company-specific terms)
- Clear variable markers ([brackets])
- Usage instructions included
- Follow existing format

## Testing Checklist

Before releases, test:

- [ ] Fresh clone on macOS
- [ ] Fresh clone on Linux
- [ ] Run SETUP.sh with various inputs
- [ ] Process inbox workflow
- [ ] 1:1 prep workflow
- [ ] Template copying
- [ ] Git integration
- [ ] All documentation links work

## Community Management

### Building Community

- Encourage users to share workflows
- Highlight good contributions in releases
- Create examples from real usage (anonymized)
- Ask for feedback on direction

### Communication Channels

- GitHub Issues for bugs/features
- Discussions for questions and sharing
- Consider: Discord/Slack for community
- Consider: Monthly office hours

### Gathering Feedback

- Quarterly user surveys
- Monitor GitHub stars/forks as interest indicator
- Track which templates get most use
- Ask "what's missing?" regularly

## Long-term Maintenance

### Preventing Bit Rot

- Review quarterly: Are docs still accurate?
- Test SETUP.sh regularly
- Update examples to stay current
- Archive outdated workflows

### Evolution

As the system evolves:
- Document breaking changes clearly
- Provide migration guides
- Maintain backwards compatibility when possible
- Version documentation (link to old versions)

### Succession Planning

If you can't maintain anymore:
- Document your workflow in this file
- Train a successor
- Hand off GitHub admin access
- Announce the transition to users

## Metrics to Track

- GitHub stars (interest)
- Forks (adoption)
- Issues opened (engagement)
- PRs submitted (community contribution)
- Downloads/clones (usage)

## Common Maintenance Tasks

### Adding a New Template

1. Create file in appropriate directory
2. Follow existing template format
3. Test it yourself
4. Update relevant docs to reference it
5. Add to next release notes

### Updating SETUP.sh

1. Test changes locally
2. Test on both macOS and Linux
3. Update version comment at top
4. Document any new prompts or behavior

### Restructuring Directories

1. Create migration guide
2. Bump major version
3. Provide script to migrate (if complex)
4. Update all docs referencing old structure
5. Clear communication in release notes

### Deprecating Features

1. Mark as deprecated in docs
2. Wait one major version
3. Remove in next major version
4. Provide alternatives
5. Clear migration path

## Resources for Maintainers

- Keep this doc updated as you learn
- Document decisions in GitHub Discussions
- Create runbooks for common tasks
- Share knowledge with co-maintainers

## Questions?

If you're a new maintainer, reach out to previous maintainers or open a Discussion.
