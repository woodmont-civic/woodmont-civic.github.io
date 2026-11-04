<template>
  <div class="orgs">
    <h3 class="title">Three neighborhood groups</h3>
    <dl>
      <div>
        <dt>Woodmont Civic Association</dt>
        <dd>That's us: gatherings, entrances, and neighborhood news.</dd>
      </div>
      <div>
        <dt><a href="https://woodmont4fun.org" target="_blank" rel="noopener">Woodmont Recreation Association</a></dt>
        <dd>Owns and runs the pool and recreation building on Traymore Road.</dd>
      </div>
      <div>
        <dt><a href="https://woodmontfriends.org" target="_blank" rel="noopener">Friends of Woodmont Park</a></dt>
        <dd>A nonprofit restoring the courts, field, and trails behind the pool.</dd>
      </div>
    </dl>
    <p class="note">They're separate organizations that work together.</p>
  </div>
</template>

<style scoped>
.orgs { border-left: 3px solid var(--color-brand-soft); padding-left: 1.25rem; }
.title { font-family: var(--font-brand-serif); font-size: 1.15rem; font-weight: 700; margin: 0 0 0.75rem; color: var(--color-brand-strong); }
dl { margin: 0; display: grid; gap: 0.8rem; }
dt { font-weight: 600; color: var(--color-ink); }
dt a { color: var(--color-brand); text-underline-offset: 3px; }
dd { margin: 0.1rem 0 0; font-size: 0.95rem; color: var(--color-ink-soft); }
.note { margin: 0.9rem 0 0; font-size: 0.9rem; color: var(--color-ink-mute); }
</style>
