---
navigation.title: 'Poems'
layout: 'default'
title: 'The Poetry Corner'
description: 'Verses from the Woodmont neighborhood, collected by The Warbler.'
---

# The Poetry Corner

*Coming soon. The Warbler is opening its pages to verse from the neighborhood — odes to the dogwoods, sonnets for the sidewalk, haiku from the front porch.*

The first poems will appear here once neighbors send them in. Be among the first.

::div{class="poems-cta"}
  :::nuxt-link{to="/post-a-poem" class="poems-cta-link"}
  Post a poem →
  :::
::

<style>
.poems-cta {
  margin-top: 28px;
  padding: 24px;
  background: var(--color-cream);
  border: 1px solid var(--color-cream-dark);
  border-left: 4px solid var(--color-forest-700);
  border-radius: 4px;
}
.poems-cta-link {
  font-family: var(--font-brand-mono, ui-monospace, monospace);
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-forest-700);
  font-weight: 600;
  text-decoration: none;
  border-bottom: 2px solid var(--color-forest-700);
  padding-bottom: 2px;
}
.poems-cta-link:hover {
  color: var(--color-forest-500);
  border-color: var(--color-forest-500);
}
</style>
