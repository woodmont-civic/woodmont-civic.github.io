<script setup lang="ts">
const appConfig = useAppConfig()

useHead({
  title: 'Welcome to the Woodmont Civic Association',
  meta: [
    {
      name: 'description',
      content:
        'Thanks for paying your dues. Here is how to get started as a Woodmont Civic Association member.',
    },
  ],
})
</script>

<template>
  <div class="welcome-page">
    <div class="prose dark:prose-invert">
      <h1>Thanks for joining!</h1>
      <p>
        Your dues keep the entrances lit, the grass cut, and the signs standing.
        PayPal will email you a receipt. Once we've matched your payment, a
        board member will reach out to welcome you and confirm your membership.
      </p>

      <h2>Getting started</h2>
      <ol>
        <li>
          <strong>Check your member page.</strong> Sign in to
          <a href="https://members.woodmontbonair.com/portal">your member page</a>
          with the email you paid with to see your dues status and confirm your
          address.
        </li>
        <li>
          <strong>Pick a way to help.</strong> Committees like Grounds and
          Welcoming are always looking for hands. Let us know what interests you
          at <a href="mailto:board@woodmontbonair.com">board@woodmontbonair.com</a>.
        </li>
        <li>
          <strong>Stay in the loop.</strong> We post newsletters and event news
          on
          <a v-if="appConfig.socials?.facebook" :href="appConfig.socials.facebook" target="_blank" rel="noopener">Facebook</a><template v-else>Facebook</template>
          and Nextdoor, and in our
          <NuxtLink to="/news/">news section</NuxtLink>.
        </li>
        <li>
          <strong>Read the covenant.</strong> Our
          <a href="https://github.com/woodmont-civic/woodmont-civic.github.io/releases/latest/download/Woodmont-Neighborhood-Covenant.pdf">Neighborhood Covenant</a>
          covers the community guidelines.
        </li>
      </ol>

      <p>
        Haven't signed up yet? Please
        <NuxtLink to="/registration/">add your contact details</NuxtLink> so we
        can match your payment.
      </p>
    </div>
  </div>
</template>

<style scoped>
.welcome-page {
  max-width: 40rem;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}
</style>
