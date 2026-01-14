<script setup lang="ts">
defineProps<{
  to: string
  text?: string
}>()
</script>

<template>
  <a 
    :href="to" 
    target="_blank" 
    rel="noopener noreferrer"
    class="inline-flex items-center gap-1 hover:underline text-primary-600 dark:text-primary-400 font-medium transition-colors"
  >
    <slot>{{ text }}</slot>
    <span class="i-heroicons-arrow-top-right-on-square-20-solid w-4 h-4 opacity-70" />
  </a>
</template>
