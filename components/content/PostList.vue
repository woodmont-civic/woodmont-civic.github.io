<script setup lang="ts">
type Post = {
  _path: string
  title?: string
  description?: string
  navigation?: { title?: string }
  type?: 'newsletter' | 'minutes' | 'social'
  date?: string
  featured?: boolean
}

type Layout = 'list' | 'grid' | 'table'

const LAYOUT_KEY = 'warbler:layout'
const LAYOUTS: Layout[] = ['list', 'grid', 'table']

const { data: posts } = await useAsyncData('posts-list', () => {
  return queryContent('/posts')
    .where({ _path: { $regex: '^/posts/\\d{4}' } })
    .sort({ _file: -1 })
    .find()
})

const MONTHS = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

function inferFromPath(path: string) {
  const m = path.match(/\/posts\/(\d{4})(?:[_-](\d{2}))?/)
  if (!m) return { year: 'Archive', label: '' }
  const year = m[1]
  const month = m[2]
  if (month) {
    const idx = parseInt(month, 10) - 1
    return { year, label: `${MONTHS[idx] ?? ''} ${year}`.trim() }
  }
  return { year, label: year }
}

function inferType(post: Post): 'newsletter' | 'minutes' | 'social' {
  if (post.type) return post.type
  const hay = ((post.navigation?.title || '') + ' ' + (post.title || '')).toLowerCase()
  if (hay.includes('social') || hay.includes('meet') || hay.includes('greet')) return 'social'
  if (hay.includes('meeting') || hay.includes('minutes')) return 'minutes'
  return 'newsletter'
}

const TYPE_LABEL: Record<string, string> = {
  newsletter: 'Newsletter',
  minutes: 'Minutes',
  social: 'Social',
}

const sortedPosts = computed<Post[]>(() => {
  if (!posts.value) return []
  return [...posts.value].sort((a: any, b: any) => b._path.localeCompare(a._path)) as Post[]
})

const featured = computed<Post | null>(() => sortedPosts.value[0] ?? null)

const featuredMeta = computed(() => {
  if (!featured.value) return { label: '', type: 'newsletter' as const }
  const { label } = inferFromPath(featured.value._path)
  return { label, type: inferType(featured.value) }
})

const q = ref('')
const layout = ref<Layout>('list')

onMounted(() => {
  try {
    const saved = localStorage.getItem(LAYOUT_KEY)
    if (saved && (LAYOUTS as string[]).includes(saved)) {
      layout.value = saved as Layout
    }
  } catch {}
})

function setLayout(v: Layout) {
  layout.value = v
  try { localStorage.setItem(LAYOUT_KEY, v) } catch {}
}

const archivePosts = computed<Post[]>(() => {
  const list = sortedPosts.value.slice(1)
  const needle = q.value.trim().toLowerCase()
  if (!needle) return list
  return list.filter((p) => {
    const hay = [
      p.navigation?.title,
      p.title,
      p.description,
      inferFromPath(p._path).label,
    ].filter(Boolean).join(' ').toLowerCase()
    return hay.includes(needle)
  })
})

const allFiltered = computed<Post[]>(() => {
  const needle = q.value.trim().toLowerCase()
  if (!needle) return sortedPosts.value
  return sortedPosts.value.filter((p) => {
    const hay = [
      p.navigation?.title,
      p.title,
      p.description,
      inferFromPath(p._path).label,
    ].filter(Boolean).join(' ').toLowerCase()
    return hay.includes(needle)
  })
})

const postsByYear = computed(() => {
  const groups: Record<string, Post[]> = {}
  for (const p of archivePosts.value) {
    const { year } = inferFromPath(p._path)
    if (!groups[year]) groups[year] = []
    groups[year].push(p)
  }
  return Object.keys(groups)
    .sort((a, b) => b.localeCompare(a))
    .map((year) => ({ year, posts: groups[year] }))
})

const yearCounts = computed(() => {
  const counts: Record<string, number> = {}
  for (const p of sortedPosts.value) {
    const { year } = inferFromPath(p._path)
    counts[year] = (counts[year] || 0) + 1
  }
  return Object.keys(counts)
    .sort((a, b) => b.localeCompare(a))
    .map((year) => ({ year, count: counts[year] }))
})

const totalIssues = computed(() => sortedPosts.value.length)

const currentMonthYear = computed(() => {
  const d = new Date()
  return `${d.toLocaleString('en-US', { month: 'long' })} ${d.getFullYear()}`
})

function scrollToYear(year: string) {
  if (typeof document === 'undefined') return
  const el = document.getElementById(`year-${year}`)
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
}

function title(p: Post) {
  return p.navigation?.title || p.title || 'Untitled'
}
</script>

<template>
  <div class="warbler">
    <!-- Masthead -->
    <header class="masthead">
      <div class="kicker"><span>EST. 1963</span>·<span>A NEIGHBORLY DISPATCH</span></div>
      <h1><span class="the">The</span>Woodmont Warbler</h1>
      <div class="tag">News, notes &amp; nature from The Woodmont Bon Air civic association</div>
      <div class="meta">
        <span>Vol. I · No. 1 (New Series)</span>
        <span>{{ currentMonthYear }}</span>
        <span>{{ totalIssues }} {{ totalIssues === 1 ? 'issue' : 'issues' }} archived</span>
      </div>
    </header>

    <div class="page">
      <div class="main-col">
        <!-- Featured (only on list layout) -->
        <article v-if="featured && layout === 'list'" class="featured">
          <div class="issue">Vol. I · No. 1<br>New Series</div>
          <div class="flag">From the Board</div>
          <h2>
            <NuxtLink :to="featured._path">{{ title(featured) }}</NuxtLink>
          </h2>
          <div class="dateline">
            {{ featuredMeta.label }} · {{ TYPE_LABEL[featuredMeta.type] }}
          </div>
          <p v-if="featured.description">&ldquo;{{ featured.description }}&rdquo;</p>
          <NuxtLink :to="featured._path" class="read">Read the full issue →</NuxtLink>
        </article>

        <!-- Filter bar -->
        <div class="filterbar">
          <div class="label">Archive</div>
          <div class="right">
            <div class="layout-switch" role="group" aria-label="Archive layout">
              <button
                type="button"
                :class="{ on: layout === 'list' }"
                :aria-pressed="layout === 'list'"
                @click="setLayout('list')"
              >
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/></svg>
                <span>List</span>
              </button>
              <button
                type="button"
                :class="{ on: layout === 'grid' }"
                :aria-pressed="layout === 'grid'"
                @click="setLayout('grid')"
              >
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
                <span>Covers</span>
              </button>
              <button
                type="button"
                :class="{ on: layout === 'table' }"
                :aria-pressed="layout === 'table'"
                @click="setLayout('table')"
              >
                <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="8" y1="6" x2="20" y2="6"/><line x1="8" y1="12" x2="20" y2="12"/><line x1="8" y1="18" x2="20" y2="18"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/></svg>
                <span>Compact</span>
              </button>
            </div>
            <div class="search">
              <input v-model="q" placeholder="Search issues…" aria-label="Search issues" />
            </div>
          </div>
        </div>

        <!-- Empty state -->
        <div v-if="layout === 'list' ? archivePosts.length === 0 : allFiltered.length === 0" class="empty">
          <p v-if="q">No issues match &ldquo;{{ q }}&rdquo;.</p>
          <p v-else>The archive is empty for now — new issues of The Warbler will appear here.</p>
        </div>

        <!-- Variant A — List (year-grouped) -->
        <template v-if="layout === 'list'">
          <section
            v-for="group in postsByYear"
            :key="group.year"
            :id="`year-${group.year}`"
            class="year-section"
          >
            <div class="year-header">
              <span class="num">{{ group.year }}</span>
              <span class="count">{{ group.posts.length }} issue{{ group.posts.length > 1 ? 's' : '' }}</span>
              <span class="line"></span>
            </div>
            <div class="issue-list">
              <NuxtLink
                v-for="post in group.posts"
                :key="post._path"
                :to="post._path"
                class="issue-row"
              >
                <div class="date">{{ inferFromPath(post._path).label }}</div>
                <div class="body">
                  <div class="title">{{ title(post) }}</div>
                  <div v-if="post.description" class="desc">{{ post.description }}</div>
                  <div class="badges">
                    <span class="badge" :class="inferType(post)">{{ TYPE_LABEL[inferType(post)] }}</span>
                  </div>
                </div>
                <div class="arrow">→</div>
              </NuxtLink>
            </div>
          </section>
        </template>

        <!-- Variant B — Cover grid -->
        <div v-else-if="layout === 'grid'" class="cover-grid">
          <NuxtLink
            v-for="post in allFiltered"
            :key="post._path"
            :to="post._path"
            class="cover"
          >
            <div class="sheet">
              <div class="tiny">{{ inferFromPath(post._path).label }} · {{ TYPE_LABEL[inferType(post)] }}</div>
              <div class="wm"><em>The</em>Warbler</div>
              <div class="rule"></div>
              <div class="t">{{ title(post) }}</div>
              <div v-if="post.description" class="d">{{ post.description }}</div>
            </div>
            <div class="foot">
              <span>{{ inferFromPath(post._path).label }}</span>
              <span class="read">Read →</span>
            </div>
          </NuxtLink>
        </div>

        <!-- Variant C — Compact table -->
        <div v-else-if="layout === 'table'" class="table-v">
          <div class="head">
            <span>Date</span><span>Title</span><span>Type</span><span></span>
          </div>
          <NuxtLink
            v-for="post in allFiltered"
            :key="post._path"
            :to="post._path"
            class="trow"
          >
            <div class="d">{{ inferFromPath(post._path).label }}</div>
            <div class="t">{{ title(post) }}</div>
            <div><span class="type">{{ TYPE_LABEL[inferType(post)] }}</span></div>
            <div class="a">→</div>
          </NuxtLink>
        </div>
      </div>

      <!-- Sidebar -->
      <aside class="sidebar">
        <div class="side-card archive">
          <h3>Browse the Archive</h3>
          <div class="jump">
            <button
              v-for="y in yearCounts"
              :key="y.year"
              type="button"
              @click="scrollToYear(y.year)"
            >
              <span>{{ y.year }}</span>
              <span class="c">{{ y.count }}</span>
            </button>
          </div>
        </div>
        <div class="side-card upload">
          <h3>Have a story?</h3>
          <p>Board members can publish a new issue by opening a pull request against the site repo. A quick how-to is linked below.</p>
          <a
            class="pr"
            href="https://github.com/woodmont-civic/woodmont-civic.github.io/blob/main/.agent/workflows/how_to_create_post.md"
            target="_blank"
            rel="noopener"
          >
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M6 9v6"/><path d="M13 6h3a2 2 0 0 1 2 2v7"/><circle cx="18" cy="18" r="3"/></svg>
            <span>How to publish →</span>
          </a>
        </div>
        <div class="side-card poem">
          <h3>Have a poem?</h3>
          <p>The Warbler prints verse from the neighborhood — odes, sonnets, haiku, anything. Send us yours.</p>
          <NuxtLink to="/post-a-poem" class="pr">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg>
            <span>Post a poem →</span>
          </NuxtLink>
        </div>
      </aside>
    </div>
  </div>
</template>

<style scoped>
.warbler {
  --forest: var(--color-forest-700);
  --forest-ink: var(--color-forest-900);
  --forest-light: var(--color-forest-400);
  --forest-soft: var(--color-forest-500);
  --cream: var(--color-cream);
  --cream-deep: var(--color-cream-dark);
  --paper: #faf8f4;
  --ink: #1f2937;
  --ink-soft: #4b5563;
  --ink-mute: #6b7280;
  --ink-fade: #9ca3af;
  --rule: #e5dfd1;
  --rule-soft: #ede6d9;
  --font-serif: var(--font-brand-serif);
  --font-italic: var(--font-brand-italic);
  --font-sans: var(--font-brand-sans);
  --font-mono: var(--font-brand-mono);

  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 28px 0;
  font-family: var(--font-sans);
  color: var(--ink);
  -webkit-font-smoothing: antialiased;
}

.warbler a { color: inherit; text-decoration: none; }
.warbler button { border: 0; background: none; font: inherit; color: inherit; cursor: pointer; }

/* Masthead */
.masthead {
  text-align: center;
  padding: 12px 0 28px;
  border-bottom: 3px double var(--forest);
  margin-bottom: 36px;
}
.masthead .kicker {
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--ink-fade);
  margin-bottom: 8px;
}
.masthead .kicker span { display: inline-block; padding: 0 10px; }
.masthead h1 {
  font-family: var(--font-serif);
  font-size: 64px;
  font-weight: 700;
  color: var(--forest);
  line-height: 1;
  letter-spacing: -.005em;
  margin: 0;
}
.masthead h1 .the {
  display: block;
  font-family: var(--font-sans);
  font-size: 13px;
  font-style: normal;
  font-weight: 500;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--forest-light);
  margin-bottom: 10px;
}
.masthead .tag {
  font-family: var(--font-italic);
  font-style: italic;
  font-size: 17px;
  color: var(--ink-mute);
  margin-top: 14px;
  letter-spacing: .005em;
}
.masthead .meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 20px;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--ink-fade);
}
.masthead .meta span {
  padding: 0 14px;
  border-right: 1px solid var(--rule);
}
.masthead .meta span:last-child { border-right: none; }

@media (max-width: 640px) {
  .masthead h1 { font-size: 44px; }
  .masthead .kicker span { padding: 0 6px; font-size: 9px; letter-spacing: .2em; }
}

/* Page grid */
.page {
  display: grid;
  grid-template-columns: 1fr 260px;
  gap: 48px;
}
@media (max-width: 880px) {
  .page { grid-template-columns: 1fr; gap: 32px; }
}

/* Featured */
.featured {
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 32px 36px;
  margin-bottom: 40px;
  position: relative;
  overflow: hidden;
}
.featured::before {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 4px;
  background: var(--forest);
}
.featured .flag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--forest-soft);
  font-weight: 600;
  margin-bottom: 12px;
}
.featured .flag::before {
  content: '';
  width: 20px;
  height: 1px;
  background: var(--forest-soft);
}
.featured h2 {
  font-family: var(--font-serif);
  font-size: 34px;
  font-weight: 700;
  color: var(--forest);
  line-height: 1.2;
  margin: 0 0 10px;
  letter-spacing: -.005em;
}
.featured h2 a { color: inherit; }
.featured h2 a:hover { color: var(--forest-soft); }
.featured .dateline {
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink-fade);
  margin-bottom: 16px;
}
.featured p {
  font-family: var(--font-italic);
  font-size: 18px;
  font-style: italic;
  color: var(--ink-soft);
  line-height: 1.55;
  max-width: 640px;
  margin: 0;
  font-weight: 400;
}
.featured .read {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 20px;
  font-weight: 600;
  color: var(--forest);
  border-bottom: 2px solid var(--forest);
  padding-bottom: 2px;
  font-size: 14px;
}
.featured .read:hover {
  color: var(--forest-soft);
  border-color: var(--forest-soft);
}
.featured .issue {
  position: absolute;
  top: 24px; right: 32px;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--ink-fade);
  text-align: right;
  line-height: 1.6;
}
@media (max-width: 640px) {
  .featured { padding: 24px 22px; }
  .featured h2 { font-size: 26px; }
  .featured .issue { display: none; }
}

/* Filter bar */
.filterbar {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--forest);
  margin-bottom: 4px;
  gap: 16px;
  flex-wrap: wrap;
}
.filterbar .label {
  font-family: var(--font-serif);
  font-size: 22px;
  font-weight: 700;
  color: var(--forest);
}
.filterbar .right {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}
.filterbar .search { display: flex; align-items: center; gap: 14px; }
.filterbar input {
  background: transparent;
  border: 0;
  border-bottom: 1px solid var(--rule);
  padding: 6px 0 6px 22px;
  font-family: var(--font-sans);
  font-size: 13px;
  color: var(--ink);
  width: 180px;
  max-width: 100%;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%236b7280' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'/%3E%3Cpath d='m21 21-4.3-4.3'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: 0 center;
  outline: none;
}
.filterbar input:focus { border-bottom-color: var(--forest); }

/* Layout switcher */
.layout-switch {
  display: inline-flex;
  align-items: center;
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 6px;
  overflow: hidden;
}
.layout-switch button {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 7px 11px;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-mute);
  font-weight: 500;
  border-right: 1px solid var(--rule);
  transition: background 120ms, color 120ms;
}
.layout-switch button:last-child { border-right: 0; }
.layout-switch button:hover {
  color: var(--forest);
  background: var(--cream-deep);
}
.layout-switch button.on {
  background: var(--forest);
  color: var(--cream);
}
.layout-switch button.on:hover { background: var(--forest-soft); }
.layout-switch svg { flex-shrink: 0; }

/* Empty state */
.empty {
  padding: 40px 8px;
  text-align: center;
  color: var(--ink-mute);
  font-family: var(--font-italic);
  font-style: italic;
  font-size: 15px;
}

/* Year section */
.year-section {
  padding: 28px 0;
  border-bottom: 1px solid var(--rule);
}
.year-section:last-child { border-bottom: 0; }
.year-header {
  display: flex;
  align-items: baseline;
  gap: 20px;
  margin-bottom: 18px;
}
.year-header .num {
  font-family: var(--font-serif);
  font-size: 42px;
  font-weight: 700;
  color: var(--forest);
  line-height: 1;
  letter-spacing: -.02em;
}
.year-header .count {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--ink-fade);
}
.year-header .line { flex: 1; height: 1px; background: var(--rule); }

/* Issue row */
.issue-list { display: flex; flex-direction: column; }
.issue-row {
  display: grid;
  grid-template-columns: 90px 1fr auto;
  gap: 24px;
  padding: 18px 8px;
  border-radius: 4px;
  align-items: baseline;
  border-left: 3px solid transparent;
  transition: background 150ms, border-color 150ms, padding-left 150ms;
  color: inherit;
}
.issue-row:hover {
  background: var(--paper);
  border-left-color: var(--forest);
  padding-left: 16px;
}
.issue-row .date {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-mute);
  font-weight: 500;
}
.issue-row .body { min-width: 0; }
.issue-row .title {
  font-family: var(--font-serif);
  font-size: 19px;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 4px;
  line-height: 1.3;
}
.issue-row:hover .title { color: var(--forest); }
.issue-row .desc {
  font-size: 13.5px;
  color: var(--ink-mute);
  line-height: 1.5;
  max-width: 560px;
}
.issue-row .badges {
  display: flex;
  gap: 6px;
  margin-top: 8px;
  flex-wrap: wrap;
}
.issue-row .badge {
  font-family: var(--font-mono);
  font-size: 9px;
  letter-spacing: .12em;
  text-transform: uppercase;
  background: var(--cream-deep);
  color: var(--ink-soft);
  padding: 2px 8px;
  border-radius: 99px;
  font-weight: 500;
}
.issue-row .badge.minutes { background: #e8dfd0; color: #6b5d3f; }
.issue-row .badge.social { background: #dbe8dc; color: var(--forest-soft); }
.issue-row .arrow {
  font-family: var(--font-serif);
  font-size: 24px;
  color: var(--ink-fade);
  align-self: center;
  transition: transform 200ms, color 150ms;
}
.issue-row:hover .arrow { color: var(--forest); transform: translateX(4px); }

@media (max-width: 640px) {
  .issue-row { grid-template-columns: 76px 1fr; gap: 16px; }
  .issue-row .arrow { display: none; }
  .year-header .num { font-size: 32px; }
}

/* Variant B — Cover grid */
.cover-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-top: 24px;
}
@media (max-width: 880px) {
  .cover-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 480px) {
  .cover-grid { grid-template-columns: 1fr; }
}
.cover {
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 6px;
  overflow: hidden;
  cursor: pointer;
  transition: transform 200ms, box-shadow 200ms;
  display: flex;
  flex-direction: column;
  color: inherit;
}
.cover:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 25px -8px rgba(27, 77, 31, .18);
}
.cover .sheet {
  background: linear-gradient(180deg, var(--forest) 0%, var(--forest) 42%, var(--paper) 42%, var(--paper) 100%);
  padding: 22px 22px 18px;
  min-height: 300px;
  display: flex;
  flex-direction: column;
  color: var(--cream);
  position: relative;
}
.cover .sheet .tiny {
  font-family: var(--font-mono);
  font-size: 9px;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: rgba(245, 240, 232, .6);
  margin-bottom: 8px;
}
.cover .sheet .wm {
  font-family: var(--font-serif);
  font-size: 26px;
  font-weight: 700;
  line-height: 1;
  color: var(--cream);
  letter-spacing: -.005em;
}
.cover .sheet .wm em {
  display: block;
  font-family: var(--font-sans);
  font-size: 9px;
  font-style: normal;
  font-weight: 500;
  letter-spacing: .3em;
  text-transform: uppercase;
  opacity: .65;
  margin-bottom: 4px;
}
.cover .sheet .rule {
  height: 2px;
  background: var(--cream);
  margin: 12px 0 8px;
  width: 40%;
}
.cover .sheet .t {
  margin-top: 56px;
  color: var(--ink);
  font-family: var(--font-serif);
  font-size: 15px;
  font-weight: 700;
  line-height: 1.25;
}
.cover .sheet .d {
  color: var(--ink-mute);
  font-size: 11px;
  line-height: 1.4;
  margin-top: 4px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.cover .foot {
  padding: 12px 18px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--ink-mute);
  border-top: 1px solid var(--rule);
}
.cover .foot .read { color: var(--forest); font-weight: 600; }

/* Variant C — Compact table */
.table-v {
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 6px;
  overflow: hidden;
  margin-top: 24px;
}
.table-v .head {
  display: grid;
  grid-template-columns: 110px 1fr 120px 60px;
  gap: 16px;
  padding: 12px 20px;
  background: var(--cream-deep);
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--ink-mute);
  font-weight: 600;
  border-bottom: 1px solid var(--rule);
}
.trow {
  display: grid;
  grid-template-columns: 110px 1fr 120px 60px;
  gap: 16px;
  padding: 14px 20px;
  border-bottom: 1px solid var(--rule-soft);
  cursor: pointer;
  align-items: center;
  transition: background 120ms;
  color: inherit;
}
.trow:hover { background: var(--cream-deep); }
.trow:last-child { border-bottom: 0; }
.trow .d {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: .1em;
  color: var(--ink-mute);
}
.trow .t {
  font-family: var(--font-serif);
  font-size: 15px;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.3;
}
.trow:hover .t { color: var(--forest); }
.trow .type {
  font-family: var(--font-mono);
  font-size: 9px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-soft);
  background: var(--cream-deep);
  padding: 3px 8px;
  border-radius: 99px;
  justify-self: start;
  font-weight: 500;
}
.trow:hover .type { background: #fff; }
.trow .a {
  font-family: var(--font-serif);
  color: var(--ink-fade);
  font-size: 18px;
  justify-self: end;
  transition: color 120ms, transform 200ms;
}
.trow:hover .a { color: var(--forest); transform: translateX(3px); }

@media (max-width: 640px) {
  .table-v .head,
  .trow {
    grid-template-columns: 90px 1fr 80px;
  }
  .table-v .head span:last-child,
  .trow .a { display: none; }
}

/* Sidebar */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 28px;
  padding-top: 12px;
}
.side-card {
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 6px;
  padding: 20px 22px;
}
.side-card h3 {
  font-family: var(--font-serif);
  font-size: 16px;
  font-weight: 700;
  color: var(--forest);
  margin: 0 0 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--rule);
}
.side-card p {
  font-size: 13px;
  color: var(--ink-soft);
  line-height: 1.6;
  margin: 0 0 10px;
}
.side-card.archive .jump {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.side-card.archive .jump button {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 0;
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-soft);
  border-bottom: 1px solid var(--rule-soft);
  text-align: left;
  width: 100%;
}
.side-card.archive .jump button:last-child { border-bottom: 0; }
.side-card.archive .jump button:hover { color: var(--forest); }
.side-card.archive .jump .c {
  background: var(--cream-deep);
  color: var(--ink-mute);
  padding: 1px 7px;
  border-radius: 99px;
  font-size: 10px;
  letter-spacing: .08em;
  font-weight: 600;
}
.side-card.upload p,
.side-card.poem p { font-size: 12px; line-height: 1.55; }
.side-card.upload .pr,
.side-card.poem .pr {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink-fade);
  padding: 10px 12px;
  background: var(--cream-deep);
  border-radius: 6px;
  margin-top: 4px;
  transition: color 150ms, background 150ms;
}
.side-card.upload .pr:hover,
.side-card.poem .pr:hover { color: var(--forest); background: #e3dcca; }
.side-card.upload .pr svg,
.side-card.poem .pr svg { flex-shrink: 0; }
</style>
