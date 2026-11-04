<script setup lang="ts">
defineProps({
  title: { type: String, required: true },
  primaryLabel: { type: String, default: '' },
  primaryHref: { type: String, default: '' },
  secondaryLabel: { type: String, default: '' },
  secondaryHref: { type: String, default: '' },
})
const email = 'board@woodmontbonair.com'
const copied = ref(false)
async function copy() {
  try { await navigator.clipboard.writeText(email); copied.value = true; setTimeout(() => (copied.value = false), 2000) } catch { /* selectable text is the fallback */ }
}
const isExternal = (href: string) => /^https?:/.test(href)
</script>

<template>
  <section class="contact not-prose">
    <div class="wrap"><div class="contact-inner">
      <h2 class="contact-title">{{ title }}</h2>
      <div class="contact-body"><slot /></div>
      <div class="contact-actions">
        <a v-if="primaryLabel" class="btn btn-primary" :href="primaryHref" :target="isExternal(primaryHref) ? '_blank' : undefined" rel="noopener">{{ primaryLabel }}</a>
        <a v-if="secondaryLabel" class="btn btn-quiet" :href="secondaryHref" :target="isExternal(secondaryHref) ? '_blank' : undefined" rel="noopener">{{ secondaryLabel }}</a>
      </div>
      <p class="email">
        Or write to us at <a :href="`mailto:${email}`">{{ email }}</a>
        <button type="button" class="copy" @click="copy">{{ copied ? 'Copied' : 'Copy' }}</button>
      </p>
    </div></div>
  </section>
</template>

<style scoped>
.contact { background: var(--color-forest-800); color: #dfe9dd; padding-block: clamp(2.75rem, 6vw, 4rem); }
.contact-inner { max-width: 44rem; }
.contact-title { font-family: var(--font-brand-serif); font-weight: 700; font-size: clamp(1.6rem, 1.2rem + 1.4vw, 2.2rem); color: #fff; margin: 0 0 0.75rem; line-height: 1.15; text-wrap: balance; }
.contact-body :deep(p) { margin: 0; }
.contact-actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1.5rem; }
.btn { display: inline-flex; align-items: center; min-height: 2.75rem; padding: 0 1.25rem; border-radius: 999px; font-weight: 600; text-decoration: none; }
.btn-primary { background: #f4e9c8; color: var(--color-forest-900); }
.btn-primary:hover { background: #fff; }
.btn-quiet { border: 1.5px solid rgba(255, 255, 255, 0.55); color: #fff; }
.btn-quiet:hover { background: rgba(255, 255, 255, 0.1); }
.btn:focus-visible, .copy:focus-visible { outline: 3px solid #f4e9c8; outline-offset: 3px; }
.email { margin: 1.5rem 0 0; font-size: 0.95rem; display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem; }
.email a { color: #fff; font-weight: 600; }
.copy { font: inherit; font-size: 0.8rem; font-weight: 600; color: #fff; background: transparent; border: 1px solid rgba(255,255,255,0.5); border-radius: 999px; padding: 0.15rem 0.7rem; cursor: pointer; }
</style>
