<template>
  <footer class="app-footer">
    <img
      class="seal"
      src="/images/archive/wca-seal-1961.png"
      alt="Woodmont Civic Association seal, 1961"
      width="56"
      height="91"
      loading="lazy"
    >
    <p class="name">Woodmont Civic Association</p>
    <p class="since">Neighbors working together since 1961</p>
  </footer>
</template>

<style scoped>
.app-footer {
  padding: 36px 20px 44px;
  text-align: center;
  background: var(--color-app-bg);
  border-top: 1px solid var(--color-rule);
}
.seal {
  display: block;
  width: 56px;
  height: auto;
  margin: 0 auto 12px;
}
.name {
  margin: 0;
  font-family: var(--font-serif, serif);
  font-size: 16px;
  font-weight: 600;
  color: var(--color-ink);
}
.since {
  margin: 4px 0 0;
  font-size: 13px;
  color: var(--color-ink-soft);
}
/* The seal is black ink on transparency; flip it so it reads on dark surfaces. */
:global(.dark .seal) {
  filter: invert(1);
}
</style>
