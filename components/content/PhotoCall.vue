<template>
  <div class="photo-call">
    <p class="label">Woodmont then and now</p>
    <h3 class="title">Have old neighborhood photos?</h3>
    <p>We're collecting pictures from past parties, holidays, and gatherings to share online and at upcoming events. Bring prints to Fall Fest, or email scans to <a href="mailto:board@woodmontbonair.com">board@woodmontbonair.com</a>.</p>
  </div>
</template>

<style scoped>
.photo-call {
  background: var(--color-paper);
  border: 1px solid var(--color-rule);
  padding: 1.4rem 1.4rem 1.5rem;
  box-shadow: 0 10px 24px -18px rgba(15, 44, 18, 0.45);
  transform: rotate(-0.6deg);
}
.label { margin: 0 0 0.35rem; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--color-brand-soft); }
.title { font-family: var(--font-brand-serif); font-size: 1.25rem; font-weight: 700; margin: 0 0 0.5rem; color: var(--color-brand-strong); line-height: 1.25; }
p { margin: 0; font-size: 0.95rem; }
a { color: var(--color-brand); font-weight: 600; word-break: break-word; }
@media (prefers-reduced-motion: reduce) { .photo-call { transform: none; } }
</style>
