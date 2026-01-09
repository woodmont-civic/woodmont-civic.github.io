---
description: How to create a new blog post for the Woodmont Civic Association website
---

# Creating a New Post

This workflow describes how to add a new event, newsletter, or update to the website.

## 1. File Location & Naming
*   All posts live in `content/posts/`.
*   **Naming Convention**: `YYYY_MM_slug.md` (e.g., `2026_01_social_event.md`).
    *   The `YYYY_MM` prefix is crucial for sorting purposes.
    *   Do NOT rely on the `date` frontmatter field alone; the filename is the primary sort key.

## 2. Frontmatter Requirements
Every post must start with a YAML frontmatter block:

```yaml
---
navigation.title: 'Title for the Link'  # e.g., "January 2026 Social"
layout: 'default'
title: 'Page Title'                     # e.g., "Join us for the Jan Social!"
description: 'Brief summary for SEO'    # Optional but recommended
---
```

**Crucial Rules**:
*   **DO NOT** set `navigation.path`. Let Nuxt Content generate it automatically.
*   `navigation.title` is what appears in the list on the `/posts` page. Make it descriptive (e.g., "June 2023 Board Meeting" not "Minutes").

## 3. Dynamic Listing
*   There is NO need to update `content/posts/index.md` or any manual list.
*   The `PostList.vue` component automatically fetches the new file, sorts it by filename (descending), and groups it by year.
*   Simply create the file, and it will appear on the site.

## 4. Content Structure
*   Use standard Markdown.
*   Images should be placed in `public/images/posts/` and referenced as `/images/posts/filename.jpg`.
