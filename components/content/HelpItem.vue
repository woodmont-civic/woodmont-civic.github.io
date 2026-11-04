<script setup lang="ts">
defineProps({ title: { type: String, required: true } })
</script>

<template>
  <div class="help-item">
    <h3 class="help-title">{{ title }}</h3>
    <div class="help-body"><slot /></div>
  </div>
</template>

<style scoped>
.help-item { border-top: 3px solid var(--color-brand-soft); padding-top: 0.9rem; min-width: 0; }
.help-title { font-family: var(--font-brand-serif); font-size: 1.2rem; font-weight: 700; margin: 0 0 0.4rem; color: var(--color-brand-strong); }
.help-body :deep(p) { margin: 0; }
</style>
