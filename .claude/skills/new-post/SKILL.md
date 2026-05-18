---
name: new-post
description: Scaffold a new WCA post under content/posts/ with required frontmatter. Use when the user says "new post", "draft a newsletter", "add an announcement", or similar. The post is the archive step of the (eventual) newsletter pipeline — keep the frontmatter convention-clean so downstream cross-posting can reuse it.
disable-model-invocation: true
---

# /new-post

Scaffold a new post for the WCA site.

## Inputs (ask the user for anything missing)

- **Slug** — short kebab-case identifier (e.g. `spring-cleanup`, `board-meeting-recap`)
- **Month** — what month/year is this for? Default to the current month if unclear.
- **Title** — full page title
- **Listing title** — short title for the post list (default: same as title)
- **Description** — one-line SEO summary
- **Body** — what should the post say? If the user has a draft (in chat, a Google Doc, etc.), use it. Otherwise ask.

## Steps

1. **Compute filename**: `content/posts/YYYY-MM-slug.md` (e.g. `2026-05-spring-cleanup.md`). Confirm with the user if the month is ambiguous. Verify the file does not already exist before writing.

2. **Create the post** by copying `.claude/skills/new-post/template.md` and substituting the placeholders.

3. **Hard rules** (the PostToolUse hook also enforces these — the hook will tell you if you violate one):
   - `navigation.title`, `layout: 'default'`, `title`, `description` — all four required
   - **Never** set `navigation.path` — Nuxt generates it from the filename
   - **Never** edit `content/posts/index.md` — `PostList.vue` auto-discovers posts
   - Images go in `public/images/posts/`, referenced as `/images/posts/<file>`

4. **Offer the copy review**: ask the user whether to run the `wca-copy-reviewer` subagent on the new file before they commit. If yes, dispatch it via the Agent tool with `subagent_type: "wca-copy-reviewer"` and the new file path.

5. **Do not auto-commit.** Show the user the path and let them review in their editor first.

## Where this fits in the bigger picture

This skill is the **archive step** of the eventual WCA newsletter pipeline (research → draft → archive → cross-post). For now you are only handling the archive step. Do not build research or cross-posting flows here — those will become separate tools when the user signals they are ready.
