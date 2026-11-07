<script setup lang="ts">
// Paste the links PayPal gives you (see the setup steps) into the `url` fields.
// Any option left blank shows a "coming soon" button instead of a broken link.
const options = [
  {
    key: 'dues',
    title: 'Annual dues',
    price: '$20',
    priceNote: 'per household, per year',
    blurb:
      'Keeps the entrances lit, the grass cut, and the signs standing. Please pay with the same email address you signed up with so we can match your payment.',
    cta: 'Pay dues',
    url: 'https://www.paypal.com/ncp/links/3X4HQ7H6ATYGQ',
  },
  {
    key: 'donate',
    title: 'Donate',
    price: 'Any amount',
    priceNote: 'you choose',
    blurb:
      'Want to do a little more? A gift goes toward entrance plantings, signage, and neighborhood gatherings.',
    cta: 'Give a gift',
    url: 'https://www.paypal.com/donate/?hosted_button_id=RGMTLS95QNHHU',
  },
  {
    key: 'tea-towel',
    title: 'Woodmont tea towel',
    price: '$40',
    priceNote: 'each',
    blurb:
      'A keepsake for the kitchen. Pick yours up at a neighborhood event, or email us to arrange delivery.',
    cta: 'Buy a tea towel',
    url: 'https://www.paypal.com/ncp/payment/YWA2ZWNXV7CDJ',
  },
]

useHead({
  title: 'Pay Dues, Donate, or Shop',
  meta: [
    {
      name: 'description',
      content:
        'Pay your Woodmont Civic Association dues, make a donation, or buy a tea towel.',
    },
  ],
})
</script>

<template>
  <div class="pay-page">
    <h1>Support Woodmont</h1>
    <p class="lead">
      Choose an option below. Payments are handled securely by PayPal, and you
      don't need a PayPal account to pay by card.
    </p>

    <div class="pay-grid">
      <section v-for="o in options" :key="o.key" class="pay-card">
        <h2>{{ o.title }}</h2>
        <p class="price">
          <span class="amount">{{ o.price }}</span>
          <span class="note">{{ o.priceNote }}</span>
        </p>
        <p class="blurb">{{ o.blurb }}</p>
        <a
          v-if="o.url"
          :href="o.url"
          class="pay-button"
          rel="noopener"
        >
          {{ o.cta }}
        </a>
        <span v-else class="pay-button pay-button--soon" aria-disabled="true">
          Coming soon
        </span>
      </section>
    </div>

    <p class="fine-print">
      Dues and donations go to the Woodmont Civic Association, which is separate
      from the Woodmont Recreation Association and Friends of Woodmont Park.
      Payments to WCA aren't tax-deductible. Not a member yet?
      <NuxtLink to="/registration/">Sign up here</NuxtLink>. Questions? Email
      <a href="mailto:board@woodmontbonair.com">board@woodmontbonair.com</a>.
    </p>
  </div>
</template>

<style scoped>
.pay-page {
  max-width: 56rem;
  margin: 0 auto;
}
.lead {
  color: var(--color-ink-soft);
}
.pay-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 1.25rem;
  margin: 2rem 0;
}
.pay-card {
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
  background: var(--color-paper);
  border: 1px solid var(--color-rule);
  border-radius: 4px;
}
.pay-card h2 {
  margin: 0 0 0.5rem;
  font-size: 1.25rem;
}
.price {
  margin: 0 0 0.75rem;
}
.amount {
  display: block;
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--color-brand);
}
.note {
  font-size: 0.875rem;
  color: var(--color-ink-mute);
}
.blurb {
  flex: 1;
  margin: 0 0 1.25rem;
  font-size: 0.95rem;
  color: var(--color-ink-soft);
}
.pay-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.75rem 1.25rem;
  border-radius: 0.5rem;
  background: var(--color-forest-700);
  color: #fff;
  font-weight: 600;
  text-decoration: none;
  transition: background-color 0.15s;
}
.pay-button:hover {
  background: var(--color-forest-800);
}
.pay-button--soon {
  background: var(--color-rule);
  color: var(--color-ink-mute);
  cursor: not-allowed;
}
.pay-button--soon:hover {
  background: var(--color-rule);
}
.fine-print {
  font-size: 0.875rem;
  color: var(--color-ink-mute);
}
</style>
