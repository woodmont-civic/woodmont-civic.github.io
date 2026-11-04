<script setup lang="ts">
defineProps({
  month: { type: String, required: true },
  day: { type: String, required: true },
  weekday: { type: String, default: '' },
  title: { type: String, required: true },
})
</script>

<template>
  <li class="event">
    <div class="date" aria-hidden="true">
      <span class="month">{{ month }}</span>
      <span class="day">{{ day }}</span>
    </div>
    <div class="detail">
      <h3 class="event-title">{{ title }}</h3>
      <p v-if="weekday" class="when">{{ weekday }}, {{ month }} {{ day }}</p>
      <div class="event-body"><slot /></div>
    </div>
  </li>
</template>

<style scoped>
.event {
  display: grid;
  grid-template-columns: 4.25rem 1fr;
  gap: 1.1rem;
  align-items: start;
  background: var(--color-paper);
  border: 1px solid var(--color-rule);
  border-radius: 6px;
  padding: 1rem 1.1rem;
}
.date {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: var(--color-forest-700);
  color: #fff;
  border-radius: 4px;
  padding: 0.45rem 0 0.5rem;
  line-height: 1;
}
.month { font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; }
.day { font-family: var(--font-brand-serif); font-size: 1.8rem; font-weight: 700; margin-top: 0.2rem; }
.detail { min-width: 0; }
.event-title { font-family: var(--font-brand-serif); font-size: 1.2rem; font-weight: 700; margin: 0; color: var(--color-brand-strong); }
.when { margin: 0.1rem 0 0.4rem !important; font-size: 0.9rem; color: var(--color-ink-mute); }
.event-body :deep(p) { margin: 0; }
</style>
