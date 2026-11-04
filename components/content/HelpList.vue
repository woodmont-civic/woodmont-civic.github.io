<template>
  <div class="help-list"><slot /></div>
</template>

<style scoped>
.help-list { display: grid; gap: 1.75rem 2.5rem; margin-top: 1.75rem; }
@media (min-width: 720px) { .help-list { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
</style>
