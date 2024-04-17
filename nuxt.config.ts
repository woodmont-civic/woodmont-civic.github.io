import { defineNuxtConfig } from 'nuxt3'

export default defineNuxtConfig({
  nitro: {
    prerender: {
      failOnError: false,
    }
  },
  vue: {
    meta: {
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { charset: 'utf-8' },
      ],
    },
  },
  extends: 'content-wind',
})
