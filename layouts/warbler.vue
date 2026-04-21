<template>
  <div class="warbler-shell">
    <main>
      <slot />
    </main>
  </div>
</template>

<style scoped>
.warbler-shell {
  background: var(--color-cream);
  min-height: 100vh;
  padding: 0 0 80px;
}
.warbler-shell :deep(h1.page-hidden-title),
.warbler-shell :deep(h1.page-hidden-title + p) {
  display: none;
}
</style>
