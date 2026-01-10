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
    },
  },
  modules: [
    'nuxt-gtag'
  ],
  gtag: {
    // The Google Analytics 4 measurement ID
    id: 'G-HYRQZ2BGTP'
  },
  extends: 'content-wind',
})
