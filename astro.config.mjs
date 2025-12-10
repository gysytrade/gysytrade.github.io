import { defineConfig } from 'astro/config'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  output: 'static',
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en', 'es', 'ja', 'ko', 'fr', 'de', 'ru', 'pt'],
    routing: {
      prefixDefaultLocale: true
    }
  },
  vite: {
    plugins: [
      tailwindcss()
    ]
  }
})
