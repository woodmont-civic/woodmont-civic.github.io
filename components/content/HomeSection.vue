<script setup lang="ts">
defineProps({
  id: { type: String, default: undefined },
  title: { type: String, default: '' },
  // paper (default) or cream for alternating bands
  tone: { type: String, default: 'paper' },
})
</script>

<template>
  <section :id="id" class="band not-prose" :class="`tone-${tone}`">
    <div class="wrap band-inner" :class="{ 'has-aside': $slots.aside }">
      <div class="band-main">
        <h2 v-if="title" class="band-title">{{ title }}</h2>
        <div class="band-body"><slot /></div>
      </div>
      <aside v-if="$slots.aside" class="band-aside"><slot name="aside" /></aside>
    </div>
  </section>
</template>

<style scoped>
.band { padding-block: clamp(2.75rem, 6vw, 4.5rem); }
.tone-paper { background: var(--color-paper); }
.tone-cream { background: var(--color-cream); }
.band-inner { display: grid; gap: 2rem; }
@media (min-width: 860px) {
  .band-inner.has-aside { grid-template-columns: 1.6fr 1fr; align-items: start; gap: 3.5rem; }
}
.band-main { min-width: 0; }
.band-title {
  font-family: var(--font-brand-serif);
  font-weight: 700;
  font-size: clamp(1.6rem, 1.2rem + 1.4vw, 2.2rem);
  line-height: 1.15;
  color: var(--color-brand);
  margin: 0 0 1rem;
  text-wrap: balance;
}
.band-body :deep(p) { margin: 0 0 1rem; max-width: 40rem; }
.band-body :deep(p:last-child) { margin-bottom: 0; }
.band-body :deep(a), .band-aside :deep(a) { color: var(--color-brand); font-weight: 600; text-underline-offset: 3px; }
.band-body :deep(strong) { color: var(--color-brand-strong); }
.band-body :deep(ul:not([class])) { margin: 0 0 1rem; padding-left: 1.2rem; }
.band-body :deep(li) { margin: 0.25rem 0; }
</style>
