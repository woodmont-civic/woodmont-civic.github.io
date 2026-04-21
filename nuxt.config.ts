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
    },
  },
  css: [
    '~/assets/css/brand.css',
  ],
  modules: [
    'nuxt-gtag'
  ],
  gtag: {
    // The Google Analytics 4 measurement ID
    id: 'G-HYRQZ2BGTP'
  },
  extends: 'content-wind',
})
