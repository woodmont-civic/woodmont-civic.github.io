export default defineNuxtConfig({
  runtimeConfig: {
    env: {
      NUXT_PUBLIC_STUDIO_TOKENS: "203c4d14f929cd3af960d4de16fde209ecee957220f0204f354ea4b63066c10b",
    },
    modules: ['@nuxt/content', '@nuxtjs/tailwindcss'],
  },
  nitro: {
    prerender: {
      failOnError: false,
    }
  },
  extends: 'content-wind',
})
