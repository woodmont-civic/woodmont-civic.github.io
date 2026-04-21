<script setup lang="ts">
interface Link {
  label: string
  href: string
}

const links: Link[] = [
  { label: 'Events', href: '#events' },
  { label: 'Get Involved', href: '#get-involved' },
  { label: 'Pay Dues', href: '#dues' },
  { label: 'Purpose', href: '#purpose' },
  { label: 'Membership', href: '#membership' },
]
</script>

<template>
  <nav
    aria-label="Quick links"
    class="not-prose my-6 flex flex-wrap gap-2"
  >
    <a
      v-for="link in links"
      :key="link.href"
      :href="link.href"
      class="inline-flex items-center rounded-full border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 px-3.5 py-1.5 text-sm font-medium text-gray-700 dark:text-gray-200 hover:border-primary-500 hover:text-primary-600 dark:hover:text-primary-400 transition-colors no-underline"
    >
      {{ link.label }}
    </a>
  </nav>
</template>
