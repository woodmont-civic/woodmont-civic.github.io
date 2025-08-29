# Woodmont Civic Association

The website is hosted on github pages and built with Nuxt.js with the Content Wind theme.

## Run locally

```shell
yarn install
yarn dev
```

## Build

```shell
yarn install
yarn generate
```

# Contributor Documentation

Thank you for your interest in contributing to the Woodmont Civic Association website! We welcome contributions from developers of all skill levels and backgrounds.

The Woodmont Civic Association website is built using the static site generator Nuxtjs, and hosted on GitHub Pages. Our newsletters are written in markdown files and will be automatically deployed when Pull Requests are merged to the main branch.

Here are the steps to contribute:

1. Fork the repository: Click the "Fork" button on the Woodmont Civic Association repository page to create your own copy of the repository.

2. Clone your fork: Use Git to clone the repository to your local machine.

```
git clone https://github.com/woodmont-civic/woodmont-civic.github.io.git
```

3. Create a new branch: Create a new branch for your changes.

```
git checkout -b my-new-branch
```

4. Make your changes: Make the changes you want to contribute. For example, you can add a new page, update an existing page, or fix a bug.

5. Test your changes: Test your changes locally to make sure they work as intended.

```
yarn install
yarn dev
```

6. Commit your changes: Once you're satisfied with your changes, commit them with a descriptive commit message.

```
git add .
git commit -m "Add new page"
```

7. Push your changes: Push your changes to your fork on GitHub.

```
git push origin my-new-branch
```

8. Create a Pull Request: Go to the Woodmont Civic Association repository page on GitHub and create a Pull Request from your fork. Be sure to include a clear description of your changes and any relevant information.

Once your Pull Request is reviewed and merged, your changes will be automatically deployed to the website.

## Deployment Information

**Production Deployment**: The website automatically deploys to GitHub Pages when changes are merged to the `main` branch.

**Preview Deployments**: Currently, there are no automatic preview deployments for Pull Requests. To test changes:
- Run the site locally using `yarn dev`
- Or manually deploy to a staging environment for testing

**Adding Files**: To add documents like PDFs:
1. Place files in the `public/` directory
2. Reference them directly in your markdown: `/filename.pdf`
3. Files in `public/` are served directly from the site root

If you have any questions or need help with contributing, please feel free to open an issue. We appreciate your contributions and look forward to working with you!

---

# Detailed instructions

## Content Wind (Nuxtjs theme)

A lightweight Nuxt theme to build a Markdown driven website, based on [Nuxt Content](https://content.nuxtjs.org), [TailwindCSS](https://tailwindcss.com) and [Iconify](https://iconify.design) :sparkles:

## Features

::list{icon=ph:check-circle-duotone}
- Write pages in Markdown
- Use [layouts](https://nuxt.com/docs/guide/directory-structure/layouts) in Markdown pages
- Enjoy meta tag generation
- Configurable [prose components](https://typography.nuxt.space)
- Generated navigation from pages
- Switch between light & dark mode
- Access 100,000 icons from 100+ icon sets
- Highlight code blocks with [Shiki](https://shiki.matsu.io)
- Create Vue components and use them in Markdown
- Deploy on any Node or Static hosting: GH Pages, Vercel, Netlify, Heroku, etc.
- Live edit on [Nuxt Studio](https://nuxt.studio)
::

## Setup

::button-link{icon="simple-icons:stackblitz" href="https://stackblitz.com/edit/nuxt-content-wind?file=content%2F1.index.md" blank}
Play online on Stackblitz
::

Open a terminal and run the following command:

```bash
npx nuxi init -t themes/content-wind my-website
```

Follow the instructions in the terminal and you are ready to go :rocket:

## Usage

This template has some built-in features to make it as easy as possible to create a content-driven website.

### Pages

Create your Markdown pages in the `content/` directory:

```md [content/index.md]
# My title

This first paragraph will be treated as the page meta description.
```

You can overwrite meta tags by using front-matter:

```md [content/index.md]
---
title: 'Custom title'
description: 'Custom meta description'
image: 'Custom image injected as `og:image`'
---

# My title

This first paragraph will be treated as the page meta description.
```

This is done thanks to Nuxt Content's [document-driven mode](https://content.nuxtjs.org/guide/writing/document-driven) of Nuxt Content.

### Navigation

The navigation is generated from your pages, you can take a look at the [`<Navbar>`](https://github.com/Atinux/content-wind/blob/main/theme/components/Navbar.vue) component to see how it works.

It uses the [`<ContentNavigation>`](https://content.nuxtjs.org/api/components/content-navigation) component from Nuxt Content to fetch the navigation object.

To customize the title displayed in the navigation, you can set the `navigation.title` property in the front-matter of your pages:

```md
---
navigation.title: 'Home'
---

# Welcome to my site

With a beautiful description
```

### Theme configuration

You can configure Content Wind global configuration in the `app.config.ts` file:

```ts [signature]
interface AppConfigInput {
  cover?: string, // default: '/cover.jpg'
  socials?: {
    twitter?: string
    github?: string
  }
}
```

Example of settings Twitter and GitHub icons in the navbar:

```ts [app.config.ts]
export default defineAppConfig({
  socials: {
    twitter: 'Atinux',
    github: 'Atinux/content-wind'
  }
})
```

### Icons

Use any icon from [icones.js.org](https://icones.js.org) with the `<Icon>` component:

```html
<Icon name="ph:music-notes-fill" />
```

You can also use it in your Markdown:

```md
:icon{name="ph:music-notes-fill"}
```

Will result in :icon{name="ph:music-notes-fill"}

Learn more on [nuxt-icon](https://github.com/Atinux/nuxt-icon) documentation.

### Code Highlight

It supports code highlighting with Shiki and as well as different [VS Code themes](https://github.com/shikijs/shiki/blob/main/docs/themes.md#all-themes).

::markdown-block
\```ts
export default () => 'Hello Content Wind'
\```
::

Will result in:

```ts
export default () => 'Hello Content Wind'
```

Updating the theme is as simple as editing your `nuxt.config`:

```ts
import { defineNuxtConfig } from 'nuxt'

export default defineNuxtConfig({
  content: {
    highlight: {
      theme: 'one-dark-pro',
    }
  }
})
```

Learn more in the [Content Code Highlight section](https://content.nuxtjs.org/api/configuration#highlight).

### Vue Components

Add Vue components into the `components/content/` directory and start using them in Markdown.

See the `<MarkdownBlock>` component in [`components/content/MarkdownBlock.vue`](https://github.com/Atinux/content-wind/blob/main/components/content/MarkdownBlock.vue).

By leveraging the [`<ContentSlot>`](https://content.nuxtjs.org/api/components/markdown) component from Nuxt Content, you can use both slots and props in Markdown thanks to the [MDC syntax](https://content.nuxtjs.org/guide/writing/mdc).


## Deployment

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FAtinux%2Fcontent-wind-template) [![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/Atinux/content-wind-template)


### Static Hosting

Pre-render the website to be deployed on any static hosting:

```bash
npm run generate
```

The `dist/` directory is ready to be deployed (symlink to `.output/public`), [learn more on Nuxt docs](https://nuxt.com/docs/getting-started/deployment#static-hosting).

### Node server

Build the application for production:

```bash
npm run build
```

Start the server in production:

```bash
node .output/server/index.mjs
```

Learn more on [Nuxt docs](https://nuxt.com/docs/getting-started/deployment) for more information.

---

You are at the end of the page, you can checkout the [about page](/about) or the [GitHub repository](https://github.com/Atinux/content-wind) and give a :icon{name="ph:star-duotone"}

Thanks for reading and happy writing, [Atinux](https://twitter.com/Atinux).
