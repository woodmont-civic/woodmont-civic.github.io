<script setup lang="ts">
// Home page hero. Photos come from `heroPhotos` in app.config.ts; until there are some,
// the hero shows the association badge instead.
const props = defineProps({
  primaryLabel: { type: String, default: '' },
  primaryHref: { type: String, default: '' },
  secondaryLabel: { type: String, default: '' },
  secondaryHref: { type: String, default: '' },
})

interface HeroPhoto { src: string; alt: string; caption?: string }
const { heroPhotos } = useAppConfig() as { heroPhotos?: HeroPhoto[] }
const photos = computed(() => (heroPhotos ?? []).slice(0, 3))
const isExternal = (href: string) => /^https?:/.test(href)
</script>

<template>
  <section class="hero not-prose" :class="{ 'has-photos': photos.length }">
    <div class="wrap hero-inner">
      <div class="hero-copy">
        <p class="kicker">Bon Air · North Chesterfield, Virginia</p>
        <h1 class="hero-title">Woodmont Civic Association</h1>
        <div class="hero-tagline"><slot /></div>
        <div class="hero-actions">
          <a v-if="props.primaryLabel" class="btn btn-primary" :href="props.primaryHref"
             :target="isExternal(props.primaryHref) ? '_blank' : undefined" rel="noopener">{{ props.primaryLabel }}</a>
          <a v-if="props.secondaryLabel" class="btn btn-quiet" :href="props.secondaryHref"
             :target="isExternal(props.secondaryHref) ? '_blank' : undefined" rel="noopener">{{ props.secondaryLabel }}</a>
        </div>
      </div>

      <div v-if="photos.length" class="snapshots" :data-count="photos.length">
        <figure v-for="(p, i) in photos" :key="p.src" class="snapshot" :class="`snap-${i + 1}`">
          <img :src="p.src" :alt="p.alt" loading="eager" />
          <figcaption v-if="p.caption">{{ p.caption }}</figcaption>
        </figure>
      </div>
      <div v-else class="badge-panel" aria-hidden="true">
        <img src="/logo-inverse.svg" alt="" width="200" height="200" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  background: var(--color-forest-800);
  color: #eef4ec;
  padding-block: clamp(2.5rem, 6vw, 4.5rem);
}
.hero-inner {
  display: grid;
  gap: 2.5rem;
  align-items: center;
}
@media (min-width: 860px) {
  .hero-inner { grid-template-columns: 1.1fr 1fr; }
}
.kicker {
  margin: 0 0 0.75rem;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--color-forest-200);
}
.hero-title {
  font-family: var(--font-brand-serif);
  font-weight: 700;
  font-size: clamp(2.2rem, 1.4rem + 3.2vw, 3.6rem);
  line-height: 1.05;
  letter-spacing: -0.015em;
  margin: 0 0 1rem;
  color: #fff;
  text-wrap: balance;
}
.hero-tagline :deep(p) {
  margin: 0;
  font-size: 1.2rem;
  line-height: 1.55;
  max-width: 34rem;
  color: #dfe9dd;
}
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1.75rem;
}
.btn {
  display: inline-flex;
  align-items: center;
  min-height: 2.75rem;
  padding: 0 1.25rem;
  border-radius: 999px;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.15s, color 0.15s;
}
.btn-primary { background: #f4e9c8; color: var(--color-forest-900); }
.btn-primary:hover { background: #fff; }
.btn-quiet { border: 1.5px solid rgba(255, 255, 255, 0.55); color: #fff; }
.btn-quiet:hover { background: rgba(255, 255, 255, 0.1); }
.btn:focus-visible { outline: 3px solid #f4e9c8; outline-offset: 3px; }

/* Snapshots: scanned prints, slightly scattered like photos on a table */
.snapshots {
  position: relative;
  min-height: 21rem;
}
.snapshot {
  position: absolute;
  margin: 0;
  background: #fbf8f1;
  padding: 0.6rem 0.6rem 0.4rem;
  box-shadow: 0 14px 30px -12px rgba(0, 0, 0, 0.55);
  width: min(62%, 17rem);
}
.snapshot img { display: block; width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.snapshot figcaption {
  font-size: 0.8rem;
  color: #3d4a3f;
  padding-top: 0.35rem;
  line-height: 1.3;
}
.snap-1 { left: 0; top: 1.5rem; transform: rotate(-4deg); z-index: 1; }
.snap-2 { right: 0; top: 0; transform: rotate(3deg); z-index: 2; }
.snap-3 { left: 22%; bottom: 0; transform: rotate(-1deg); z-index: 3; }
.snapshots[data-count="1"] .snap-1 { position: relative; width: 100%; top: 0; transform: rotate(-1.5deg); }
.snapshots[data-count="1"] { min-height: 0; }
@media (max-width: 520px) {
  .snapshots { min-height: 17rem; }
}

.badge-panel { display: none; }
@media (min-width: 860px) {
  .badge-panel { display: flex; justify-content: center; }
  .badge-panel img { width: 12rem; height: auto; opacity: 0.9; }
}
</style>
