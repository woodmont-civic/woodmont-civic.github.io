<script setup lang="ts">
const route = useRoute()

type ArticleDoc = {
  title?: string
  description?: string
  navigation?: { title?: string }
  type?: 'newsletter' | 'minutes' | 'social'
  date?: string
  _path?: string
}

const { data: page } = await useAsyncData(
  () => `article-meta-${route.path}`,
  () => queryContent<ArticleDoc>(route.path).findOne(),
)

const MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

function inferLabel(path: string | undefined): string {
  if (!path) return ''
  const m = path.match(/\/posts\/(\d{4})(?:[_-](\d{2}))?/)
  if (!m) return ''
  const year = m[1]
  const month = m[2]
  if (month) {
    const idx = parseInt(month, 10) - 1
    return `${MONTHS[idx] ?? ''} ${year}`.trim()
  }
  return year
}

function inferType(doc: ArticleDoc | null | undefined): 'newsletter' | 'minutes' | 'social' {
  if (doc?.type) return doc.type
  const hay = ((doc?.navigation?.title || '') + ' ' + (doc?.title || '')).toLowerCase()
  if (hay.includes('social') || hay.includes('meet') || hay.includes('greet')) return 'social'
  if (hay.includes('meeting') || hay.includes('minutes')) return 'minutes'
  return 'newsletter'
}

const TYPE_LABEL: Record<string, string> = {
  newsletter: 'Newsletter',
  minutes: 'Board Minutes',
  social: 'Social',
}

const articleType = computed(() => inferType(page.value))
const issueLabel = computed(() => inferLabel(page.value?._path ?? route.path))
const displayTitle = computed(
  () => page.value?.title || page.value?.navigation?.title || 'Untitled',
)
</script>

<template>
  <div class="article-shell">
    <article class="article">
      <nav class="topbar">
        <NuxtLink to="/posts" class="back">
          <span class="arrow">←</span>
          <span class="label">The Woodmont Warbler</span>
        </NuxtLink>
      </nav>

      <header class="article-head">
        <div class="kicker">
          <span class="badge" :class="articleType">
            {{ TYPE_LABEL[articleType] }}
          </span>
          <span v-if="issueLabel" class="dot">·</span>
          <span v-if="issueLabel" class="date">{{ issueLabel }}</span>
        </div>

        <h1 class="title">{{ displayTitle }}</h1>

        <p v-if="page?.description" class="standfirst">
          {{ page.description }}
        </p>

        <div class="byline">
          <span class="rule-piece"></span>
          <span class="org">Woodmont Civic Association</span>
          <span class="rule-piece"></span>
        </div>
      </header>

      <div class="article-body prose dark:prose-invert">
        <slot />
      </div>

      <footer class="article-foot">
        <div class="rule" aria-hidden="true"></div>
        <p class="end">— end of issue —</p>
        <NuxtLink to="/posts" class="back-link">
          ← Back to The Warbler
        </NuxtLink>
      </footer>
    </article>
  </div>
</template>

<style scoped>
.article-shell {
  background: var(--color-app-bg);
  min-height: 100vh;
  padding: 36px 20px 96px;
}

.article {
  max-width: 720px;
  margin: 0 auto;
  background: var(--color-paper);
  border: 1px solid var(--color-rule);
  border-radius: 4px;
  padding: 28px 44px 56px;
  position: relative;
  box-shadow:
    0 1px 0 rgba(27, 77, 31, 0.04),
    0 12px 32px -20px rgba(15, 44, 18, 0.18);
}
.article::before {
  content: '';
  position: absolute;
  inset: 6px;
  border: 1px solid var(--color-paper-inner);
  border-radius: 2px;
  pointer-events: none;
}

/* Top bar with "back to Warbler" link */
.topbar {
  display: flex;
  justify-content: flex-start;
  margin-bottom: 28px;
}
.topbar .back {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-brand-mono);
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--color-ink-mute);
  text-decoration: none;
  padding: 4px 0;
  transition: color 150ms, transform 200ms;
}
.topbar .back:hover {
  color: var(--color-brand);
}
.topbar .back:hover .arrow { transform: translateX(-2px); }
.topbar .back .arrow {
  font-family: var(--font-brand-serif);
  font-size: 14px;
  transition: transform 200ms;
}

/* Editorial head */
.article-head {
  text-align: center;
  padding: 0 0 28px;
  margin-bottom: 32px;
  border-bottom: 3px double var(--color-brand);
}

.kicker {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 18px;
}
.kicker .badge {
  font-family: var(--font-brand-mono);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  background: var(--color-cream-dark);
  color: var(--color-ink-soft);
  padding: 4px 10px;
  border-radius: 99px;
}
.kicker .badge.minutes,
.kicker .badge.social,
.kicker .badge.newsletter {
  background: var(--color-cream-dark);
  color: var(--color-brand);
}
.kicker .dot {
  color: var(--color-ink-fade);
  font-size: 12px;
}
.kicker .date {
  font-family: var(--font-brand-mono);
  font-size: 11px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--color-ink-fade);
}

.title {
  font-family: var(--font-brand-serif);
  font-weight: 700;
  font-size: clamp(2rem, 1.4rem + 2.8vw, 3rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--color-brand);
  margin: 0 auto 18px;
  max-width: 22ch;
}

.standfirst {
  font-family: var(--font-brand-serif);
  font-style: italic;
  font-size: 1.15rem;
  line-height: 1.55;
  color: var(--color-ink-soft);
  max-width: 52ch;
  margin: 0 auto 22px;
}

.byline {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  font-family: var(--font-brand-mono);
  font-size: 10px;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--color-ink-fade);
}
.byline .rule-piece {
  flex: 0 0 36px;
  height: 1px;
  background: var(--color-rule);
}

/* Body — the prose styles do the heavy lifting; we just shape the column. */
.article-body {
  max-width: 62ch;
  margin: 0 auto;
}
/* Inside the editorial wrapper, our content's H1 (if author left one)
   would duplicate the masthead title — collapse it. The standfirst above
   already serves the role of description. */
.article-body :deep(> h1:first-child) {
  display: none;
}
/* Tighten the first H2/H3 so it sits flush below the masthead. */
.article-body :deep(> h2:first-child),
.article-body :deep(> h3:first-child) {
  margin-top: 0;
}

/* Foot */
.article-foot {
  margin-top: 56px;
  text-align: center;
}
.article-foot .rule {
  width: 80px;
  height: 1px;
  background: var(--color-brand);
  margin: 0 auto 18px;
}
.article-foot .end {
  font-family: var(--font-brand-serif);
  font-style: italic;
  font-size: 0.95rem;
  color: var(--color-ink-fade);
  margin: 0 0 20px;
}
.article-foot .back-link {
  display: inline-block;
  font-family: var(--font-brand-mono);
  font-size: 11px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--color-brand);
  text-decoration: none;
  border-bottom: 2px solid var(--color-brand);
  padding-bottom: 2px;
  transition: color 150ms, border-color 150ms;
}
.article-foot .back-link:hover {
  color: var(--color-brand-soft);
  border-color: var(--color-brand-soft);
}

@media (max-width: 720px) {
  .article-shell { padding: 18px 12px 64px; }
  .article {
    padding: 22px 22px 40px;
    border-radius: 2px;
  }
  .article::before { inset: 4px; }
  .article-head { padding-bottom: 22px; margin-bottom: 24px; }
  .standfirst { font-size: 1.05rem; }
  .byline { gap: 10px; font-size: 9px; letter-spacing: 0.2em; }
  .byline .rule-piece { flex-basis: 24px; }
}

/* Dark mode: deeper shadow only — colors are token-driven and flip automatically */
:global(.dark) .article {
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.02),
    0 12px 32px -20px rgba(0, 0, 0, 0.6);
}
</style>
