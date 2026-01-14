<script setup lang="ts">
const isBetaEnabled = ref(false)
const showGate = ref(false)

// Key for localStorage
const STORAGE_KEY = 'woodmont_beta'

const toggleBeta = () => {
  if (process.client) {
    if (isBetaEnabled.value) {
        // Disable
        localStorage.removeItem(STORAGE_KEY)
        isBetaEnabled.value = false
        showGate.value = true
        // Dispatch event for AppNavbar
        window.dispatchEvent(new Event('beta-changed'))
    } else {
        // Enable
        localStorage.setItem(STORAGE_KEY, 'true')
        isBetaEnabled.value = true
        showGate.value = false
        // Dispatch event for AppNavbar
        window.dispatchEvent(new Event('beta-changed'))
    }
  }
}

onMounted(() => {
  if (process.client) {
    const urlParams = new URLSearchParams(window.location.search)
    const betaParam = urlParams.get('beta')
    
    // Handle URL Params
    if (betaParam === 'true') {
      localStorage.setItem(STORAGE_KEY, 'true')
      isBetaEnabled.value = true
    } else if (betaParam === 'false') {
      localStorage.removeItem(STORAGE_KEY)
      isBetaEnabled.value = false
    } else {
      // Fallback to existing storage
      if (localStorage.getItem(STORAGE_KEY) === 'true') {
        isBetaEnabled.value = true
      }
    }

    if (!isBetaEnabled.value) {
        showGate.value = true
    } else {
        showGate.value = false
    }
  }
})
</script>


<template>
  <div>
    <div v-if="!showGate">
      <slot />
      
      <!-- Beta Exit Button (Visible when content is shown) -->
      <div class="my-8 text-center text-sm text-gray-400">
        <button @click="toggleBeta" class="underline hover:text-gray-600 dark:hover:text-gray-200">
            Exit Preview Mode
        </button>
      </div>
    </div>

    <!-- Gate UI -->
    <div v-else class="flex flex-col items-center justify-center min-h-[50vh] text-center p-8">
      <div class="bg-gray-100 dark:bg-gray-800 rounded-2xl p-8 max-w-md border border-gray-200 dark:border-gray-700">
          <span class="text-4xl mb-4 block">🚧</span>
          <h2 class="text-2xl font-bold mb-2">Coming Soon</h2>
          <p class="text-gray-600 dark:text-gray-400 mb-6">
              This feature is currently in development. Check back later!
          </p>
          <div class="flex flex-col gap-4">
            <NuxtLink to="/" class="text-primary-600 dark:text-primary-400 font-bold hover:underline">
                ← Return Home
            </NuxtLink>
            
            <!-- Secret/Admin Toggle -->
            <button @click="toggleBeta" class="text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 mt-4">
                (Enable Preview)
            </button>
          </div>
      </div>
    </div>
  </div>
</template>
