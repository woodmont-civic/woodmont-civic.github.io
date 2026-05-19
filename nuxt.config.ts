export default defineNuxtConfig({
  nitro: {
    prerender: {
      failOnError: false,
    }
  },
  app: {
    head: {
      htmlAttrs: {
        lang: 'en'
      },
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ],
      link: [
        { rel: 'icon', type: 'image/svg+xml', sizes: '32x32', href: '/favicon-32.svg' },
        { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' },
        { rel: 'alternate icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' },
        {
          rel: 'stylesheet',
          href: 'https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap'
        },
      ],
      script: [
        {
          type: 'application/ld+json',
          innerHTML: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'Organization',
            name: 'Woodmont Civic Association',
            alternateName: 'WCA',
            url: 'https://woodmontbonair.com',
            logo: 'https://woodmontbonair.com/logo.svg',
            description: 'Official site of the Woodmont Civic Association — news, events, and resources for the Woodmont neighborhood of Bon Air, VA.',
            email: 'woodmontbonair@gmail.com',
            areaServed: {
              '@type': 'Place',
              name: 'Woodmont, Bon Air, Chesterfield County, Virginia',
            },
            sameAs: [
              'https://www.facebook.com/search/top/?q=woodmont%20civic%20association',
            ],
          }),
        },
      ],
    },
  },
  css: [
    '~/assets/css/brand.css',
  ],
  modules: [
    'nuxt-gtag',
    '@vite-pwa/nuxt',
    // SEO stack — installed à la carte rather than via @nuxtjs/seo because the
    // bundle pulls in nuxt-og-image, which requires @nuxt/content v3 and would
    // break the content-wind theme. Organization JSON-LD is hand-rolled in
    // app.head.script below (the nuxt-schema-org module pulls in @nuxt/ui +
    // Tailwind v4 via its devtools layer, which conflicts with content-wind's
    // Tailwind v3).
    '@nuxtjs/sitemap',
    '@nuxtjs/robots',
    'nuxt-seo-utils',
  ],
  site: {
    url: 'https://woodmontbonair.com',
    name: 'Woodmont Civic Association',
    description: 'Official site of the Woodmont Civic Association — news, events, and resources for the Woodmont neighborhood of Bon Air, VA.',
    defaultLocale: 'en',
  },
  sitemap: {
    exclude: ['/gallery', '/history', '/news/**'],
  },
  gtag: {
    // The Google Analytics 4 measurement ID
    id: 'G-HYRQZ2BGTP'
  },
  pwa: {
    registerType: 'autoUpdate',
    manifest: {
      name: 'Woodmont Civic Association',
      short_name: 'Woodmont',
      description: 'Official site of the Woodmont Civic Association — news, events, and resources for the Woodmont neighborhood of Bon Air, VA.',
      theme_color: '#1b4d1f',
      background_color: '#ffffff',
      display: 'standalone',
      start_url: '/',
      scope: '/',
      icons: [
        { src: 'pwa-64x64.png', sizes: '64x64', type: 'image/png' },
        { src: 'pwa-192x192.png', sizes: '192x192', type: 'image/png' },
        { src: 'pwa-512x512.png', sizes: '512x512', type: 'image/png' },
        { src: 'maskable-icon-512x512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
      ],
    },
    workbox: {
      // Disable the navigation fallback. This is an SSG site with a precached
      // HTML file per route, so navigation requests should fall through to the
      // network (or matching precache entry) — not a single SPA shell. With a
      // fallback set, any URL not matching a precache entry exactly (e.g.
      // /posts/ with trailing slash) gets the home page instead of the right
      // page. Note: @vite-pwa/nuxt defaults this to '/' if the key is absent,
      // so we must set it explicitly (null cast — Workbox accepts no value).
      navigateFallback: null as unknown as string,
      globPatterns: ['**/*.{js,css,html,png,svg,ico,woff2,webmanifest}'],
    },
    client: {
      installPrompt: true,
    },
    devOptions: {
      enabled: false,
    },
  },
  extends: 'content-wind',
})
