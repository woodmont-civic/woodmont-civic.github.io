<template>
  <div class="page-shell">
    <main class="page-card prose dark:prose-invert">
      <slot />
    </main>
  </div>
</template>

<style scoped>
.page-shell {
  background: var(--color-app-bg);
  min-height: 100vh;
  padding: 36px 20px 96px;
}

.page-card {
  max-width: 1040px;
  margin: 0 auto;
  background: var(--color-paper);
  border: 1px solid var(--color-rule);
  border-radius: 4px;
  padding: 56px 72px 72px;
  position: relative;
  box-shadow:
    0 1px 0 rgba(27, 77, 31, 0.04),
    0 12px 32px -20px rgba(15, 44, 18, 0.18);
}
.page-card::before {
  content: '';
  position: absolute;
  inset: 6px;
  border: 1px solid var(--color-paper-inner);
  border-radius: 2px;
  pointer-events: none;
}

@media (max-width: 880px) {
  .page-shell { padding: 24px 14px 80px; }
  .page-card { padding: 32px 28px 48px; border-radius: 2px; }
  .page-card::before { inset: 4px; }
}

@media (max-width: 520px) {
  .page-shell { padding: 16px 10px 64px; }
  .page-card { padding: 22px 18px 40px; }
}

/* Dark mode card shadow: replace warm shadow with a deeper one */
:global(.dark) .page-card {
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.02),
    0 12px 32px -20px rgba(0, 0, 0, 0.6);
}
</style>
