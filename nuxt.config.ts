export default defineNuxtConfig({
  studio: {
    repository: {
      provider: 'github', // 'github' or 'gitlab'
      owner: 'woodmont-civic',
      repo: 'woodmont-civic.github.io',
      branch: 'main'
    }
  },
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
  extends: 'content-wind',
  modules: ['@nuxthq/studio']
})
