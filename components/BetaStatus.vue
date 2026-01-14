<script setup lang="ts">
const isBetaEnabled = ref(false)
const STORAGE_KEY = 'woodmont_beta'

const checkStatus = () => {
    if (process.client) {
        isBetaEnabled.value = localStorage.getItem(STORAGE_KEY) === 'true'
    }
}

const toggleBeta = () => {
  if (process.client) {
    if (isBetaEnabled.value) {
        localStorage.removeItem(STORAGE_KEY)
        isBetaEnabled.value = false
    } else {
        localStorage.setItem(STORAGE_KEY, 'true')
        isBetaEnabled.value = true
    }
    // Dispatch event for other components (Navbar, Gates)
    window.dispatchEvent(new Event('beta-changed'))
  }
}

onMounted(() => {
    checkStatus()
    if (process.client) {
        window.addEventListener('beta-changed', checkStatus)
    }
})

onUnmounted(() => {
    if (process.client) {
        window.removeEventListener('beta-changed', checkStatus)
    }
})
</script>

<template>
  <div class="py-4 text-center">
    <button 
        @click="toggleBeta"
        class="text-xs text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 transition-colors"
    >
        Preview Mode: {{ isBetaEnabled ? 'ON' : 'OFF' }}
    </button>
  </div>
</template>
