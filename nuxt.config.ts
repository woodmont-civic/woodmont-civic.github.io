import { defineNuxtConfig } from 'nuxt/config'

module.exports = {
    publicPath: '/woodmont-civic/'
}
export default defineNuxtConfig({
modules: [
    '@vite-pwa/nuxt',
    '@nuxt/content',

],
pwa: {
    manifest: {
        name: 'My Nuxt App',
        short_name: 'My Nuxt App',
        description: 'My Nuxt.js PWA App',
        lang: 'en',
    }, 
},

},
)
