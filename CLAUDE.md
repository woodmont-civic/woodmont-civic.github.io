# Woodmont Civic Association — Claude Code Context

Official website for the **Woodmont Civic Association (WCA)**, a neighborhood civic organization in Chesterfield County, VA. Static Nuxt 3 site deployed to GitHub Pages.

- **Live**: woodmontbonair.com · **Dues**: https://www.paypal.com/ncp/payment/3X4HQ7H6ATYGQ ($20/household)
- **WCA email**: woodmontbonair@gmail.com · **Board**: board@woodmontbonair.com

## Who you're working with

The user is the **President of the WCA**. A companion **Claude Web project** holds longer-form WCA strategy and campaign history — reference it when relevant.

Apply the presidential lens to anything community-facing:

- **Tone**: welcoming, professional, optimistic — "presidential but neighborly"
- **North star**: "How does this help our neighbors?"
- **Don't over-engineer**: the association runs on volunteer time and $20 dues
- **Represent the Board**: spelling, grammar, and professionalism matter

**Campaign Review Checklist** — any public-facing copy:
1. Is it clear?
2. Is the CTA obvious?
3. Does it feel welcoming to new neighbors?
4. Is spelling/grammar perfect?

## Communication channels

- **Neighborhood Google Group**: woodmont-neighborhood@googlegroups.com (moderated, community-facing)
- **Board Google Group**: woodmontbonair@googlegroups.com (internal)
- **Neighborhood Watch**: monthly reports from Corporal Craig Eckrich, Chesterfield County
- **Social**: Facebook, Nextdoor

## Stack

Nuxt 3 + Content Wind · @nuxt/content v2 (Markdown + MDC) · TailwindCSS + Pinceau (primary: teal) · @vite-pwa/nuxt · nuxt-gtag (GA4: `G-HYRQZ2BGTP`) · Yarn. See `package.json` and `nuxt.config.ts` for specifics.

```bash
yarn install    # deps
yarn dev        # local dev server — see "long-running processes" below
yarn generate   # static build → ./dist
```

Merging to `main` auto-deploys to GitHub Pages and creates a GitHub Release with `neighborhood-covenant.pdf` attached.

## Adding a post

1. New file: `content/posts/YYYY-MM-slug.md` — filename is the primary sort key.
2. Required frontmatter:
   ```yaml
   ---
   navigation.title: 'Short title for listing'
   layout: 'default'
   title: 'Full page title'
   description: 'Brief SEO summary'
   ---
   ```
3. **Do not** set `navigation.path` — Nuxt generates it.
4. **Do not** edit `content/posts/index.md` — `PostList.vue` auto-discovers posts.
5. Images go in `public/images/posts/`, referenced as `/images/posts/<file>`.

Full walkthrough: `.agent/workflows/how_to_create_post.md`.

## Long-running processes

Persistent processes (`yarn dev`, watchers, ngrok, tunnels) never return on their own — a foreground Bash call will hang. Past `/loop` runs have burned wall-clock budget this way.

- **Start servers with `run_in_background: true`.** Never wait on the spawn.
- **Probe readiness with a counter loop**, not `timeout` (macOS lacks GNU `timeout`):
  ```bash
  for i in {1..45}; do curl -s --max-time 3 http://localhost:3000 > /dev/null && break; sleep 2; done
  ```
- **Cap foreground Bash with an explicit `timeout`** (e.g. 60000ms) — fail fast beats hanging.
- **Don't kill processes you didn't start.** The user runs parallel worktree dev servers. Check `git worktree list` and `ps -eo pid,etime,command | grep nuxi` first.
- `EMFILE: too many open files, watch` = multiple Nuxt instances on the same tree. Use exactly one dev server; don't bump ulimits.
- **Clean up your own background PIDs** before handing off.

## Multi-session work: GitHub issues are the state machine

For work that may span sessions (especially `/loop`), the tracking issue is the durable handoff — uncommitted working-tree changes are ephemeral.

1. Read the issue → find the latest `### STATE` comment → resume from there.
2. Do one chunk → commit to the feature branch.
3. Post a new `### STATE` comment: what was done, branch SHA, what's next, blockers.
4. Open a draft PR as soon as anything is committed; push screenshots there.

## Campaigns

Each campaign gets a folder under `campaigns/in-progress/YYYY-MM-slug/` containing `plan.md`, `email_draft.md`, `social_posts.md`. Move to `campaigns/completed/` when done.

## Beta features

Gated behind a `woodmont_beta` localStorage flag — **do not link publicly** until production-ready:
- `/gallery` — Community photo gallery
- `/history` — History Hub

## Key files

- `content/1.index.md` — home page
- `app.config.ts` — site title, social links, cover image
- `nuxt.config.ts` — modules, PWA, GA
- `tokens.config.ts` — design tokens
- `public/neighborhood-covenant.pdf` — community covenant

## Workflow guides

Per-task guides in `.agent/workflows/`: `how_to_create_post.md`, `president_agent.md`, `architecture_agent.md`, `google_drive_manager.md`.
