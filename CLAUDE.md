# Woodmont Civic Association — Claude Code Context

## Project Overview

This is the official website for the **Woodmont Civic Association (WCA)**, a neighborhood civic organization in Chesterfield County, VA. The site is built with Nuxt.js 3 + Content Wind and deployed as a static site on GitHub Pages.

- **Live site**: woodmontbonair.com (GitHub Pages)
- **WCA email**: woodmontbonair@gmail.com
- **Board contact**: board@woodmontbonair.com
- **Dues payments**: pay.woodmontbonair.com
- **Annual dues**: $20/household

## Who You're Working With

The user is the **President of the Woodmont Civic Association**. There is also a companion **Claude Web project** for WCA with additional context and longer-form strategy — reference it for campaign history and community notes when relevant.

When drafting communications or making content decisions, apply the presidential lens:

- **Tone**: Welcoming, professional, optimistic — "presidential but neighborly"
- **North star**: "How does this help our neighbors?"
- **Avoid over-engineering**: The association runs on volunteer time and $20 dues
- **Represent the Board**: Spelling, grammar, and professionalism matter in all public-facing content

**Campaign Review Checklist** (for any community-facing copy):
- Is it clear?
- Is the Call to Action obvious?
- Does it feel welcoming to new neighbors?
- Is spelling/grammar perfect?

## Communication Channels

- **Neighborhood Google Group**: woodmont-neighborhood@googlegroups.com (moderated, community-facing)
- **Board Google Group**: woodmontbonair@googlegroups.com (internal board communications)
- **Neighborhood Watch**: Monthly reports from Corporal Craig Eckrich, Chesterfield County
- **Social platforms**: Facebook, Nextdoor

## Tech Stack

- **Framework**: Nuxt.js 3 with Content Wind theme (markdown-driven)
- **Content**: @nuxt/content v2 — Markdown + MDC (Vue components in Markdown)
- **Styling**: TailwindCSS + Pinceau design tokens (primary color: teal)
- **Analytics**: Google Analytics 4 via nuxt-gtag (ID: G-HYRQZ2BGTP)
- **Hosting**: GitHub Pages, deployed via `yarn generate` → static HTML
- **CI/CD**: GitHub Actions (`.github/workflows/`)
- **Package manager**: Yarn

## Directory Structure

```
content/              # All Markdown pages (drives site navigation automatically)
  posts/              # Newsletter posts and event announcements
    YYYY_MM_slug.md   # Naming convention — filename is the primary sort key
components/           # Vue components
  content/            # MDC components usable inside Markdown
campaigns/            # Campaign planning assets
  in-progress/        # Active campaigns
  completed/          # Archived campaigns
  ideas/              # Future ideas
hack/                 # Board tools and templates (gitignored)
.agent/workflows/     # Agent guides for common tasks
public/               # Static assets (images, PDFs)
```

## Creating a New Post

1. Create `content/posts/YYYY_MM_slug.md`
2. Add required frontmatter:

```yaml
---
navigation.title: 'Descriptive title for listing'
layout: 'default'
title: 'Full page title'
description: 'Brief SEO summary'
---
```

3. Do NOT set `navigation.path` — Nuxt generates it automatically
4. Do NOT edit `content/posts/index.md` — `PostList.vue` auto-discovers posts
5. Place images in `public/images/posts/` and reference as `/images/posts/filename.jpg`

See `.agent/workflows/how_to_create_post.md` for full details.

## Build & Deploy

```bash
yarn install    # Install deps
yarn dev        # Local dev server
yarn generate   # Build static site → ./dist
```

Merging to `main` auto-deploys to GitHub Pages. A GitHub Release is also created automatically on each merge, with `neighborhood-covenant.pdf` attached as an asset.

## Running long-lived processes (servers, watchers, tunnels)

Any persistent process — `yarn dev`, `yarn generate --watch`, ngrok, file watchers, etc. — never returns on its own, so a foreground Bash call will hang until your wall-clock budget runs out. This has burned past `/loop` runs.

**Rules:**

1. **Server starts use `run_in_background: true`.** Never wait on the spawning command itself.
2. **Verify readiness out-of-band.** Probe with `curl --max-time 3 http://localhost:3000` in a counter loop. macOS does not ship GNU `timeout`, so don't use `timeout 90 bash -c '…'` — use a `for` counter instead: `for i in {1..45}; do curl -s --max-time 3 http://localhost:3000 > /dev/null 2>&1 && break; sleep 2; done`.
3. **Cap foreground Bash calls.** Pass an explicit `timeout` (e.g. 60000ms) on anything that should be short — better to fail fast than hang.
4. **Don't kill processes you didn't start.** Before killing an unfamiliar `nuxi dev` (or anything else), check `git worktree list` and `ps -eo pid,etime,command | grep nuxi` — the user often has worktree dev servers going for parallel features. Killing one of those destroys their work-in-progress.
5. **Multiple Nuxt instances on the same tree exhaust file watchers.** If you see `EMFILE: too many open files, watch`, that's the symptom. The fix is to use exactly one dev server, not to bump per-process ulimits.
6. **Clean up your own background PIDs** before exiting an iteration or handing off.

This applies especially when running inside `/loop` or under an agent: the parent loop has a wall-clock budget and a hung server burns the whole window.

## Long-running tasks: GitHub issues as state machine

For multi-iteration work (especially `/loop` runs that may restart), use the tracking GitHub issue as the durable state machine. Each iteration should:

1. **Read the issue** to find the latest `### STATE` comment — that's the resume point.
2. **Do one chunk of work** and commit it to the feature branch.
3. **Post a new `### STATE` comment** with: what was just done, current branch SHA, what's next, any blockers.
4. **Open a draft PR** as soon as there's something committed, and link it in the issue. Push screenshots there.

Treat uncommitted working-tree changes as ephemeral — they may not survive a restart. The issue + branch + draft PR are the durable handoff.

## Campaign Planning

Campaign assets live in `campaigns/`. Each campaign gets a folder:

```
campaigns/in-progress/YYYY-MM-slug/
  plan.md           # Strategy and goals
  email_draft.md    # Email content
  social_posts.md   # Social media copy
```

Move to `campaigns/completed/` when done.

## Beta Features

Some features are gated behind a `woodmont_beta` localStorage flag:
- `/gallery` — Community photo gallery
- `/history` — History Hub

Do not link to these publicly until they are production-ready.

## Key Files

- `content/1.index.md` — Home page
- `content/posts/` — All posts and newsletters
- `app.config.ts` — Site title, social links, cover image
- `nuxt.config.ts` — Nuxt modules and GA config
- `tokens.config.ts` — Design tokens (primary color: teal)
- `public/neighborhood-covenant.pdf` — Community covenant document

## Agent Workflows

Detailed guides for common tasks are in `.agent/workflows/`:
- `how_to_create_post.md` — Adding posts and newsletters
- `president_agent.md` — Presidential role and communication guidelines
- `architecture_agent.md` — Architecture decisions
- `google_drive_manager.md` — Google Drive integration
