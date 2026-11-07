<script setup lang="ts">
// PayPal hosted links. Any option with a blank url shows a disabled
// "Coming soon" button instead of a broken link.
const options = [
  {
    key: 'dues',
    title: 'Annual dues',
    price: '$20',
    priceNote: 'per household, per year',
    blurb:
      'Keeps the entrances lit, the grass cut, and the signs standing. Please pay with the email address you signed up with so we can match your payment.',
    cta: 'Pay dues',
    url: 'https://www.paypal.com/ncp/links/3X4HQ7H6ATYGQ',
  },
  {
    key: 'donate',
    title: 'Donation',
    price: 'Any amount',
    priceNote: 'you choose',
    blurb:
      'Want to give a little more than dues? Every bit goes toward the entrances and neighborhood projects.',
    cta: 'Donate',
    url: 'https://www.paypal.com/donate/?hosted_button_id=RGMTLS95QNHHU',
  },
  {
    key: 'tea-towel',
    title: 'Woodmont tea towel',
    price: '$40',
    priceNote: 'each',
    blurb: 'A Woodmont keepsake for your kitchen.',
    cta: 'Buy a tea towel',
    url: 'https://www.paypal.com/ncp/payment/YWA2ZWNXV7CDJ',
  },
]

useHead({
  title: 'Pay Dues, Donate, or Buy a Tea Towel',
  meta: [
    {
      name: 'description',
      content:
        'Pay your Woodmont Civic Association dues, make a donation, or buy a Woodmont tea towel.',
    },
  ],
})
</script>

<template>
  <div class="pay-page">
    <div class="prose dark:prose-invert">
      <h1>Support Woodmont</h1>
      <p>Choose an option below. Payments are handled securely by PayPal.</p>
    </div>

    <ul class="pay-list">
      <li v-for="o in options" :key="o.key" class="pay-item">
        <div class="pay-info">
          <h2>{{ o.title }}</h2>
          <p class="price">
            <span class="amount">{{ o.price }}</span>
            <span class="note">{{ o.priceNote }}</span>
          </p>
          <p class="blurb">{{ o.blurb }}</p>
        </div>
        <a v-if="o.url" :href="o.url" class="pay-button" rel="noopener">
          {{ o.cta }}
        </a>
        <span v-else class="pay-button pay-button--soon" aria-disabled="true">
          Coming soon
        </span>
      </li>
    </ul>

    <p class="fine-print">
      Payments go to the Woodmont Civic Association, which is separate from the
      Woodmont Recreation Association and Friends of Woodmont Park. Payments to
      WCA aren't tax-deductible. Not a member yet?
      <NuxtLink to="/registration/">Sign up here</NuxtLink>. Questions? Email
      <a href="mailto:board@woodmontbonair.com">board@woodmontbonair.com</a>.
    </p>
  </div>
</template>

<style scoped>
.pay-page {
  max-width: 40rem;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}
.pay-list {
  list-style: none;
  margin: 1.5rem 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}
.pay-item {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 1.25rem 1.5rem;
  background: var(--color-paper);
  border: 1px solid var(--color-rule);
  border-radius: 4px;
}
.pay-info {
  flex: 1;
  min-width: 0;
}
.pay-info h2 {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--color-ink);
}
.price {
  margin: 0.25rem 0 0.5rem;
}
.amount {
  font-size: 1.375rem;
  font-weight: 700;
  color: var(--color-brand);
}
.note {
  margin-left: 0.4rem;
  font-size: 0.875rem;
  color: var(--color-ink-mute);
}
.blurb {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.5;
  color: var(--color-ink-soft);
}
.pay-button {
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 9.5rem;
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
.pay-button--soon,
.pay-button--soon:hover {
  background: var(--color-rule);
  color: var(--color-ink-mute);
  cursor: not-allowed;
}
.fine-print {
  font-size: 0.875rem;
  line-height: 1.5;
  color: var(--color-ink-mute);
}
.fine-print a {
  color: inherit;
  text-decoration: underline;
}

@media (max-width: 560px) {
  .pay-item {
    flex-direction: column;
    align-items: stretch;
  }
  .pay-button {
    width: 100%;
  }
}
</style>
