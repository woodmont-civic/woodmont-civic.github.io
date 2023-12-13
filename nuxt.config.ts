export default defineNuxtConfig({
  nitro: {
    prerender: {
      failOnError: false,
    }
  },
  extends: 'content-wind',
})
