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
        {name: 'viewport', content: 'width=device-width, initial-scale=1'},
      ],
    },
  },
  extends: 'content-wind',
})
