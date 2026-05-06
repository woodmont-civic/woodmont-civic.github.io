<script setup lang="ts">
useHead({
  title: 'Post a Poem — The Woodmont Warbler',
  meta: [
    {
      name: 'description',
      content: 'Submit a poem to The Woodmont Warbler. Verse from the neighborhood, reviewed by the board.',
    },
  ],
})
</script>

<template>
  <div class="warbler-submit">
    <header class="masthead">
      <div class="kicker">
        <span>THE WARBLER</span>·<span>SUBMISSIONS DESK</span>
      </div>
      <h1>Post a Poem</h1>
      <div class="tag">
        Verses from the neighborhood — odes to the dogwoods, sonnets for the sidewalk,
        a haiku from your front porch. The Warbler would love to print it.
      </div>
    </header>

    <div class="page">
      <div class="main-col">
        <PoemSubmitForm />
      </div>

      <aside class="sidebar">
        <div class="side-card steps">
          <h3>What happens next</h3>
          <ol>
            <li>
              <span class="num">1</span>
              <span>You'll be sent to GitHub with your poem already filled in.</span>
            </li>
            <li>
              <span class="num">2</span>
              <span>GitHub will ask you to sign in (free) and fork the site repo.</span>
            </li>
            <li>
              <span class="num">3</span>
              <span>Click <em>Propose new file</em> to open a pull request.</span>
            </li>
            <li>
              <span class="num">4</span>
              <span>A board editor reviews and merges. Your poem appears on the site.</span>
            </li>
          </ol>
        </div>

        <div class="side-card">
          <h3>No GitHub account?</h3>
          <p>
            That's all right. Email your poem to
            <a href="mailto:board@woodmontbonair.com?subject=Poem%20submission">board@woodmontbonair.com</a>
            and we'll post it on your behalf.
          </p>
        </div>

        <div class="side-card">
          <h3>Have a story instead?</h3>
          <p>The Warbler also welcomes news, photos, and notes from the neighborhood.</p>
          <NuxtLink to="/posts" class="back-link">
            <span>Read The Warbler →</span>
          </NuxtLink>
        </div>
      </aside>
    </div>

    <footer class="foot">
      <NuxtLink to="/posts" class="back">← Back to The Warbler</NuxtLink>
    </footer>
  </div>
</template>

<style scoped>
.warbler-submit {
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
  --font-sans: var(--font-brand-sans);
  --font-mono: var(--font-brand-mono);

  max-width: 1100px;
  margin: 0 auto;
  padding: 40px 28px 0;
  font-family: var(--font-sans);
  color: var(--ink);
  -webkit-font-smoothing: antialiased;
}

.warbler-submit a { color: inherit; text-decoration: none; }

.masthead {
  text-align: center;
  padding: 12px 0 24px;
  border-bottom: 3px double var(--forest);
  margin-bottom: 36px;
}
.masthead .kicker {
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--ink-fade);
  margin-bottom: 8px;
}
.masthead .kicker span { display: inline-block; padding: 0 10px; }
.masthead h1 {
  font-family: var(--font-serif);
  font-size: 52px;
  font-weight: 700;
  color: var(--forest);
  line-height: 1;
  letter-spacing: -0.015em;
  margin: 0;
}
.masthead .tag {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 16px;
  color: var(--ink-mute);
  margin: 14px auto 0;
  max-width: 620px;
  line-height: 1.5;
}

@media (max-width: 640px) {
  .masthead h1 { font-size: 38px; }
  .masthead .kicker span { padding: 0 6px; font-size: 9px; letter-spacing: 0.2em; }
  .masthead .tag { font-size: 14.5px; }
}

.page {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 48px;
}
@media (max-width: 880px) {
  .page { grid-template-columns: 1fr; gap: 32px; }
}

.sidebar {
  display: flex;
  flex-direction: column;
  gap: 22px;
  padding-top: 4px;
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
  margin: 0 0 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--rule);
}
.side-card p {
  font-size: 13px;
  color: var(--ink-soft);
  line-height: 1.6;
  margin: 0 0 8px;
}
.side-card p a {
  color: var(--forest);
  border-bottom: 1px solid var(--forest);
}
.side-card p a:hover { color: var(--forest-soft); border-color: var(--forest-soft); }

.side-card.steps ol {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.side-card.steps li {
  display: grid;
  grid-template-columns: 24px 1fr;
  gap: 10px;
  font-size: 13px;
  color: var(--ink-soft);
  line-height: 1.55;
}
.side-card.steps .num {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  color: var(--cream);
  background: var(--forest);
  border-radius: 99px;
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  letter-spacing: 0;
  flex-shrink: 0;
}
.side-card.steps em {
  font-style: italic;
  color: var(--ink);
  font-weight: 600;
}

.back-link {
  display: inline-block;
  margin-top: 6px;
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ink-mute);
  border-bottom: 1px solid var(--rule);
  padding-bottom: 2px;
}
.back-link:hover { color: var(--forest); border-color: var(--forest); }

.foot {
  margin-top: 56px;
  padding: 28px 0 32px;
  border-top: 1px solid var(--rule);
  text-align: center;
}
.back {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--ink-mute);
}
.back:hover { color: var(--forest); }
</style>
