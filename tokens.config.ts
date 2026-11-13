import { defineTheme } from 'pinceau'

// Tailwind `primary-*` is the WCA forest scale, the same values as
// --color-forest-* in assets/css/brand.css and --forest-* in wca-crm.
// Change all three together.
export default defineTheme({
  color: {
    primary: {
      50: '#f0f7f0',
      100: '#d6ead7',
      200: '#aed4b0',
      300: '#7cb87f',
      400: '#4e9653',
      500: '#2e7a34',
      600: '#1e5e25',
      700: '#1b4d1f',
      800: '#163d1a',
      900: '#0f2c12',
    }
  }
})
