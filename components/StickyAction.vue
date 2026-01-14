<script setup lang="ts">
const isVisible = ref(false)
const isDismissed = ref(false)
let lastScrollY = 0

// Key for localStorage
const STORAGE_KEY = 'woodmont_dues_paid_year'

const handleScroll = () => {
  if (process.client && !isDismissed.value) {
    const currentScrollY = window.scrollY
    // Show if scrolling up or at top, hide if scrolling down
    // Also ensure we've scrolled a bit initially so it doesn't pop up immediately on load if at top 
    // (optional, but "scrolling up" logic handles most cases).
    // Let's keep it simple: Hide on scroll down, show on scroll up.
    if (currentScrollY > lastScrollY && currentScrollY > 100) {
      isVisible.value = false
    } else {
      isVisible.value = true
    }
    lastScrollY = currentScrollY
  }
}

const checkDismissal = () => {
  if (process.client) {
    const storedYear = localStorage.getItem(STORAGE_KEY)
    const currentYear = new Date().getFullYear().toString()
    if (storedYear === currentYear) {
      isDismissed.value = true
      isVisible.value = false
    } else {
      isVisible.value = true
    }
  }
}

const dismiss = () => {
  if (process.client) {
    const currentYear = new Date().getFullYear().toString()
    localStorage.setItem(STORAGE_KEY, currentYear)
    isDismissed.value = true
    isVisible.value = false
  }
}

onMounted(() => {
  if (process.client) {
    checkDismissal()
    window.addEventListener('scroll', handleScroll)
  }
})

onUnmounted(() => {
  if (process.client) {
    window.removeEventListener('scroll', handleScroll)
  }
})
</script>

<template>
  <div 
    v-if="!isDismissed"
    class="fixed bottom-0 left-0 right-0 p-4 z-50 transition-transform duration-300 transform"
    :class="isVisible ? 'translate-y-0' : 'translate-y-[150%]'"
  >
    <div class="relative bg-white/90 dark:bg-gray-900/90 backdrop-blur-md border border-gray-200 dark:border-gray-700 shadow-2xl rounded-2xl p-4 flex items-center justify-between gap-4">
      
      <!-- Dismiss Button -->
      <button 
        @click="dismiss"
        class="absolute -top-3 -right-3 bg-gray-200 dark:bg-gray-700 text-gray-500 dark:text-gray-300 rounded-full p-1 shadow-md hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
        aria-label="Dismiss payment reminder"
      >
        <span class="i-heroicons-x-mark-20-solid w-4 h-4 block" />
      </button>

      <div class="flex-1">
        <p class="text-xs text-gray-500 dark:text-gray-400 font-medium uppercase tracking-wide">
          Membership
        </p>
        <p class="text-sm font-bold text-gray-900 dark:text-white">
          Join for $20/yr
        </p>
      </div>
      <a 
        href="https://pay.woodmontbonair.com" 
        target="_blank" 
        rel="noopener noreferrer"
        class="bg-primary-600 hover:bg-primary-700 text-white font-bold py-2.5 px-6 rounded-xl shadow-lg shadow-primary-500/30 transition-all active:scale-95"
      >
        Pay Dues
      </a>
    </div>
  </div>
</template>
