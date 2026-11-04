<template>
  <div class="home-shell">
    <slot />
  </div>
</template>

<style scoped>
.home-shell {
  background: var(--color-paper);
  color: var(--color-ink);
  font-family: var(--font-brand-sans);
  font-size: 17px;
  line-height: 1.65;
}
</style>
