<script setup lang="ts">
const REPO_NEW_FILE_BASE = 'https://github.com/woodmont-civic/woodmont-civic.github.io/new/main/content/poems'
const FALLBACK_EMAIL = 'board@woodmontbonair.com'

const URL_WARN_THRESHOLD = 6000
const URL_HARD_THRESHOLD = 7500

const MAX_TITLE = 120
const MAX_AUTHOR = 80
const MAX_DEDICATION = 200
const MAX_BODY = 5000

const title = ref('')
const author = ref('')
const dedication = ref('')
const body = ref('')

const submitAttempted = ref(false)

function escapeYaml(value: string): string {
  return value.replace(/\r?\n/g, ' ').replace(/'/g, "''").trim()
}

function slugify(value: string): string {
  const base = value
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/-+/g, '-')

  if (!base) return 'untitled'
  if (base.length <= 50) return base

  const truncated = base.slice(0, 50)
  const lastDash = truncated.lastIndexOf('-')
  if (lastDash > 20) return truncated.slice(0, lastDash)
  return truncated
}

function todayLocal(): string {
  const d = new Date()
  const yyyy = d.getFullYear()
  const mm = String(d.getMonth() + 1).padStart(2, '0')
  const dd = String(d.getDate()).padStart(2, '0')
  return `${yyyy}-${mm}-${dd}`
}

function bodyAsBlockquote(text: string): string {
  return text
    .replace(/\r\n/g, '\n')
    .split('\n')
    .map((line) => (line.trim() === '' ? '>' : `> ${line}`))
    .join('\n')
}

const trimmedTitle = computed(() => title.value.trim())
const trimmedAuthor = computed(() => author.value.trim())
const trimmedDedication = computed(() => dedication.value.trim())
const trimmedBody = computed(() => body.value.trim())

const date = computed(() => todayLocal())
const slug = computed(() => slugify(trimmedTitle.value))
const filename = computed(() => `${date.value}-${slug.value}.md`)

const generatedMarkdown = computed(() => {
  const t = escapeYaml(trimmedTitle.value || 'Untitled Poem')
  const a = escapeYaml(trimmedAuthor.value || 'Anonymous')
  const d = trimmedDedication.value ? escapeYaml(trimmedDedication.value) : ''

  const dedicationFrontmatter = d ? `dedication: '${d}'\n` : ''
  const dedicationBody = d ? `*Dedicated to ${trimmedDedication.value}.*\n\n` : ''

  const lines = [
    '---',
    `navigation.title: '${t} — ${a}'`,
    `layout: 'default'`,
    `title: '${t}'`,
    `author: '${a}'`,
    `date: '${date.value}'`,
    dedicationFrontmatter ? dedicationFrontmatter.trimEnd() : null,
    `type: 'poem'`,
    '---',
    '',
    `# ${trimmedTitle.value || 'Untitled Poem'}`,
    '',
    `*by ${trimmedAuthor.value || 'Anonymous'}*`,
    '',
    dedicationBody ? dedicationBody.trimEnd() : null,
    dedicationBody ? '' : null,
    bodyAsBlockquote(trimmedBody.value || '> '),
    '',
  ].filter((line) => line !== null)

  return lines.join('\n')
})

const encodedLength = computed(() => encodeURIComponent(generatedMarkdown.value).length)

const lengthState = computed(() => {
  if (encodedLength.value > URL_HARD_THRESHOLD) return 'hard'
  if (encodedLength.value > URL_WARN_THRESHOLD) return 'warn'
  return 'ok'
})

const errors = computed(() => {
  const e: Record<string, string> = {}
  if (!trimmedTitle.value) e.title = 'A title is required.'
  else if (trimmedTitle.value.length > MAX_TITLE) e.title = `Keep the title under ${MAX_TITLE} characters.`

  if (!trimmedAuthor.value) e.author = 'Please add a name to credit (a pen name is fine).'
  else if (trimmedAuthor.value.length > MAX_AUTHOR) e.author = `Keep the name under ${MAX_AUTHOR} characters.`

  if (trimmedDedication.value.length > MAX_DEDICATION) e.dedication = `Dedications cap at ${MAX_DEDICATION} characters.`

  if (!trimmedBody.value) e.body = 'Your poem is missing — please add it below.'
  else if (trimmedBody.value.length < 4) e.body = 'Just a few more words?'
  else if (trimmedBody.value.length > MAX_BODY) e.body = `Poems cap at ${MAX_BODY} characters in this form.`

  if (lengthState.value === 'hard') {
    e.body = e.body || 'This poem is too long to send through GitHub. Try trimming, or email it to the board.'
  }

  return e
})

const hasErrors = computed(() => Object.keys(errors.value).length > 0)

const githubUrl = computed(() => {
  const params = new URLSearchParams()
  params.set('filename', filename.value)
  params.set('value', generatedMarkdown.value)
  return `${REPO_NEW_FILE_BASE}?${params.toString()}`
})

const mailtoFallback = computed(() => {
  const subject = encodeURIComponent(`Poem submission: ${trimmedTitle.value || '(untitled)'}`)
  const lines = [
    `Title: ${trimmedTitle.value}`,
    `Author: ${trimmedAuthor.value}`,
    trimmedDedication.value ? `Dedication: ${trimmedDedication.value}` : '',
    '',
    trimmedBody.value,
  ].filter(Boolean).join('\n')
  return `mailto:${FALLBACK_EMAIL}?subject=${subject}&body=${encodeURIComponent(lines)}`
})

const showPreview = ref(false)

function handleSubmit(event: Event) {
  event.preventDefault()
  submitAttempted.value = true
  if (hasErrors.value) {
    return
  }
  window.open(githubUrl.value, '_blank', 'noopener,noreferrer')
}

function fieldError(name: string) {
  if (!submitAttempted.value) return ''
  return errors.value[name] || ''
}
</script>

<template>
  <form class="poem-form" novalidate @submit="handleSubmit">
    <div class="kicker"><span>The Poem</span></div>

    <div class="field">
      <label for="poem-title">Title <span class="req">*</span></label>
      <input
        id="poem-title"
        v-model="title"
        type="text"
        :maxlength="MAX_TITLE + 10"
        placeholder="e.g. Ode to the Dogwoods on Dolfield"
        :aria-invalid="!!fieldError('title')"
        aria-describedby="poem-title-error"
      />
      <div v-if="fieldError('title')" id="poem-title-error" class="field-error">{{ fieldError('title') }}</div>
    </div>

    <div class="field">
      <label for="poem-author">Author display name <span class="req">*</span></label>
      <input
        id="poem-author"
        v-model="author"
        type="text"
        :maxlength="MAX_AUTHOR + 10"
        placeholder="A name to credit — pen names welcome"
        :aria-invalid="!!fieldError('author')"
        aria-describedby="poem-author-error"
      />
      <div v-if="fieldError('author')" id="poem-author-error" class="field-error">{{ fieldError('author') }}</div>
    </div>

    <div class="field">
      <label for="poem-dedication">Dedication <span class="opt">(optional)</span></label>
      <input
        id="poem-dedication"
        v-model="dedication"
        type="text"
        :maxlength="MAX_DEDICATION + 10"
        placeholder="Dedicated to…"
        :aria-invalid="!!fieldError('dedication')"
        aria-describedby="poem-dedication-error"
      />
      <div v-if="fieldError('dedication')" id="poem-dedication-error" class="field-error">{{ fieldError('dedication') }}</div>
    </div>

    <div class="field">
      <label for="poem-body">Your poem <span class="req">*</span></label>
      <textarea
        id="poem-body"
        v-model="body"
        rows="10"
        :maxlength="MAX_BODY + 100"
        placeholder="Stanzas welcome — line breaks will be preserved."
        :aria-invalid="!!fieldError('body')"
        aria-describedby="poem-body-error poem-body-counter"
      ></textarea>
      <div id="poem-body-counter" class="counter" :class="lengthState">
        <span>{{ trimmedBody.length }} / {{ MAX_BODY }} characters</span>
        <span v-if="lengthState === 'warn'" class="counter-note">Long — may be near GitHub's URL limit.</span>
        <span v-if="lengthState === 'hard'" class="counter-note">Too long for the GitHub link — please trim or email instead.</span>
      </div>
      <div v-if="fieldError('body')" id="poem-body-error" class="field-error">{{ fieldError('body') }}</div>
    </div>

    <div v-if="submitAttempted && hasErrors" class="form-summary-error" role="alert">
      Please fix the highlighted fields before sending.
    </div>

    <div class="actions">
      <button type="submit" class="primary" :disabled="submitAttempted && hasErrors">
        Send to GitHub →
      </button>
      <a :href="mailtoFallback" class="secondary">Email it instead</a>
    </div>

    <div class="preview-toggle">
      <button type="button" class="link-button" @click="showPreview = !showPreview">
        {{ showPreview ? '▾ Hide' : '▸ Preview' }} the Markdown that will be sent
      </button>
      <pre v-if="showPreview" class="preview"><code>{{ generatedMarkdown }}</code></pre>
    </div>

    <p class="finepoint">
      Submitting opens a pull request on the WCA site repo. You'll need a free GitHub account.
      A board member reviews every submission before it appears on the site.
    </p>
  </form>
</template>

<style scoped>
.poem-form {
  --forest: var(--color-forest-700);
  --forest-soft: var(--color-forest-500);
  --forest-light: var(--color-forest-400);
  --cream: var(--color-cream);
  --cream-deep: var(--color-cream-dark);
  --paper: #faf8f4;
  --ink: #1f2937;
  --ink-soft: #4b5563;
  --ink-mute: #6b7280;
  --ink-fade: #9ca3af;
  --rule: #e5dfd1;
  --rule-soft: #ede6d9;
  --alert: #a04a3a;
  --alert-soft: #c97a6b;

  --font-serif: var(--font-brand-serif);
  --font-sans: var(--font-brand-sans);
  --font-mono: var(--font-brand-mono);

  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 28px 32px 24px;
  font-family: var(--font-sans);
  color: var(--ink);
  position: relative;
  overflow: hidden;
}

.poem-form::before {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 4px;
  background: var(--forest);
}

.kicker {
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--forest-soft);
  font-weight: 600;
  margin-bottom: 18px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.kicker::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--rule);
}

.field {
  margin-bottom: 18px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field label {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink-soft);
  font-weight: 600;
}

.field label .req { color: var(--alert); margin-left: 2px; }
.field label .opt {
  color: var(--ink-fade);
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0.02em;
  font-size: 10.5px;
  margin-left: 4px;
}

.field input,
.field textarea {
  font-family: var(--font-sans);
  font-size: 14px;
  color: var(--ink);
  background: #fff;
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 10px 12px;
  outline: none;
  transition: border-color 150ms, box-shadow 150ms;
  width: 100%;
}

.field textarea {
  font-family: var(--font-serif);
  font-size: 15px;
  line-height: 1.6;
  resize: vertical;
  min-height: 200px;
}

.field input:focus,
.field textarea:focus {
  border-color: var(--forest);
  box-shadow: 0 0 0 3px rgba(46, 122, 52, 0.12);
}

.field input[aria-invalid="true"],
.field textarea[aria-invalid="true"] {
  border-color: var(--alert-soft);
}

.field-error {
  color: var(--alert);
  font-size: 12px;
  font-style: italic;
  margin-top: 2px;
}

.counter {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  color: var(--ink-fade);
  margin-top: 4px;
}
.counter.warn { color: #a8782a; }
.counter.hard { color: var(--alert); }
.counter .counter-note { font-style: italic; text-align: right; }

.form-summary-error {
  background: #f7e9e4;
  color: var(--alert);
  border-left: 3px solid var(--alert);
  padding: 10px 14px;
  font-size: 13px;
  margin: 6px 0 16px;
  border-radius: 0 4px 4px 0;
}

.actions {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-top: 8px;
  flex-wrap: wrap;
}

.primary {
  background: var(--forest);
  color: var(--cream);
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-weight: 600;
  padding: 12px 22px;
  border-radius: 4px;
  border: 0;
  cursor: pointer;
  transition: background 150ms, transform 150ms;
}
.primary:hover { background: var(--forest-soft); }
.primary:active { transform: translateY(1px); }
.primary:disabled {
  background: var(--ink-fade);
  cursor: not-allowed;
}

.secondary {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-mute);
  text-decoration: none;
  border-bottom: 1px dashed var(--ink-fade);
  padding-bottom: 1px;
}
.secondary:hover { color: var(--forest); border-color: var(--forest); }

.preview-toggle { margin-top: 22px; }
.link-button {
  background: none;
  border: 0;
  font: inherit;
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ink-mute);
  cursor: pointer;
  padding: 0;
}
.link-button:hover { color: var(--forest); }

.preview {
  margin-top: 10px;
  background: var(--cream);
  border: 1px solid var(--rule);
  border-radius: 4px;
  padding: 14px 16px;
  font-family: var(--font-mono);
  font-size: 12px;
  line-height: 1.5;
  color: var(--ink-soft);
  white-space: pre-wrap;
  overflow-x: auto;
  max-height: 320px;
}

.finepoint {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 12.5px;
  color: var(--ink-mute);
  line-height: 1.55;
  margin-top: 22px;
  padding-top: 16px;
  border-top: 1px solid var(--rule-soft);
}

@media (max-width: 640px) {
  .poem-form { padding: 22px 20px; }
  .actions { gap: 12px; }
  .primary { width: 100%; text-align: center; }
}
</style>
