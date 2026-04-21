<script setup lang="ts">
const { $pwa } = useNuxtApp() as any

const IOS_DISMISS_KEY = 'woodmont_pwa_ios_dismissed'
const iosHintVisible = ref(false)

const dismissIos = () => {
  if (process.client) {
    localStorage.setItem(IOS_DISMISS_KEY, 'true')
    iosHintVisible.value = false
  }
}

onMounted(() => {
  if (!process.client) return

  const ua = window.navigator.userAgent
  const isIos = /iPad|iPhone|iPod/.test(ua) && !(window as any).MSStream
  const isStandalone =
    window.matchMedia('(display-mode: standalone)').matches ||
    (window.navigator as any).standalone === true
  const dismissed = localStorage.getItem(IOS_DISMISS_KEY) === 'true'

  if (isIos && !isStandalone && !dismissed) {
    iosHintVisible.value = true
  }
})
</script>

<template>
  <Teleport to="body">
    <!-- Chrome / Edge / Android: native install prompt -->
    <div
      v-if="$pwa?.showInstallPrompt && !$pwa?.isPWAInstalled"
      class="fixed bottom-4 left-1/2 -translate-x-1/2 z-50 max-w-md w-[calc(100%-2rem)] rounded-lg shadow-lg bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-4"
    >
      <div class="flex items-start gap-3">
        <div class="flex-1">
          <p class="font-semibold text-sm text-gray-900 dark:text-gray-100">
            Install Woodmont app
          </p>
          <p class="text-xs text-gray-600 dark:text-gray-300 mt-1">
            Get quick access to neighborhood news from your home screen.
          </p>
        </div>
        <div class="flex items-center gap-2">
          <button
            class="text-xs px-3 py-1.5 rounded bg-teal-700 hover:bg-teal-800 text-white font-medium"
            @click="$pwa.install()"
          >
            Install
          </button>
          <button
            aria-label="Dismiss"
            class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 text-lg leading-none"
            @click="$pwa.cancelInstall()"
          >
            &times;
          </button>
        </div>
      </div>
    </div>

    <!-- iOS Safari: manual Add to Home Screen hint -->
    <div
      v-else-if="iosHintVisible"
      class="fixed bottom-4 left-1/2 -translate-x-1/2 z-50 max-w-md w-[calc(100%-2rem)] rounded-lg shadow-lg bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-4"
    >
      <div class="flex items-start gap-3">
        <div class="flex-1">
          <p class="font-semibold text-sm text-gray-900 dark:text-gray-100">
            Install Woodmont app
          </p>
          <p class="text-xs text-gray-600 dark:text-gray-300 mt-1">
            Tap <span aria-label="Share">&#x2BAD;</span> Share, then
            <strong>Add to Home Screen</strong>.
          </p>
        </div>
        <button
          aria-label="Dismiss"
          class="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 text-lg leading-none"
          @click="dismissIos"
        >
          &times;
        </button>
      </div>
    </div>
  </Teleport>
</template>
