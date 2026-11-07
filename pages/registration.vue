<template>
  <div class="form-container">
    <div class="prose dark:prose-invert">
      <ContentDoc />
    </div>
    <div class="my-6 flex flex-wrap gap-3">
      <a
        href="https://admin.woodmontbonair.com/register"
        class="inline-flex items-center rounded-lg bg-primary-700 px-5 py-3 font-medium text-white no-underline hover:bg-primary-800 transition-colors"
      >
        Sign up
      </a>
      <a
        href="/pay/"
        class="inline-flex items-center rounded-lg border border-gray-300 dark:border-gray-600 px-5 py-3 font-medium text-gray-800 dark:text-gray-100 no-underline hover:border-primary-500 transition-colors"
      >
        Pay dues
      </a>
    </div>
    <p class="text-sm text-gray-600 dark:text-gray-300">
      Already a member? Check your dues status and update your address on
      <a href="https://members.woodmontbonair.com/portal" class="underline">your member page</a>.
    </p>
  </div>
</template>

<style scoped>
.form-container {
  max-width: 40rem;
  margin: 0 auto;
  padding: 1.5rem 1rem;
}
</style>
