<script setup lang="ts">
interface FactItem {
  label: string
  value: string
}

defineProps<{
  items: FactItem[]
}>()
</script>

<template>
  <dl class="fact-sheet not-prose">
    <template v-for="(item, i) in items" :key="i">
      <dt>{{ item.label }}</dt>
      <dd>{{ item.value }}</dd>
    </template>
  </dl>
</template>

<style scoped>
.fact-sheet {
  display: grid;
  grid-template-columns: max-content 1fr;
  gap: 6px 24px;
  margin: 1.6em 0 2em;
  padding: 18px 22px;
  background: var(--color-cream);
  border-left: 3px solid var(--color-forest-700);
  border-radius: 2px;
  font-family: var(--font-brand-sans);
  font-size: 0.95rem;
  line-height: 1.55;
}

.fact-sheet dt {
  font-family: var(--font-brand-mono);
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--color-forest-500);
  padding-top: 0.25em;
  align-self: start;
}

.fact-sheet dd {
  margin: 0;
  color: var(--color-ink);
}

@media (max-width: 520px) {
  .fact-sheet {
    grid-template-columns: 1fr;
    gap: 2px 0;
    padding: 14px 16px;
  }
  .fact-sheet dt { padding-top: 0.6em; }
  .fact-sheet dt:first-child { padding-top: 0; }
}

:global(.dark) .fact-sheet {
  background: rgba(46, 122, 52, 0.08);
  border-left-color: #7cb87f;
}
:global(.dark) .fact-sheet dt { color: #7cb87f; }
:global(.dark) .fact-sheet dd { color: #e8eae7; }
</style>
