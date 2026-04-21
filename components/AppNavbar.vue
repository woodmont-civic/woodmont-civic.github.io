<script lang="ts" setup>
const { navigation } = useContent()
const appConfig = useAppConfig()

// Beta Logic
const isBetaEnabled = ref(false)
const STORAGE_KEY = 'woodmont_beta'

// Filter navigation based on Beta status
const filteredNavigation = computed(() => {
  if (isBetaEnabled.value) {
    return navigation.value
  }
  
  // List of beta paths to hide
  const betaPaths = ['/gallery', '/history']
  
  return navigation.value.filter(link => !betaPaths.includes(link._path))
})

onMounted(() => {
    if (process.client) {
        // Sync with local storage
        if (localStorage.getItem(STORAGE_KEY) === 'true') {
            isBetaEnabled.value = true
        }

        // Listen for storage changes if multiple tabs or just to be reactive? 
        // Or maybe just polling? 
        // Simpler: The toggle in BetaGate reloads the page? 
        // No, toggle in BetaGate relies on reactivity. 
        // But AppNavbar is a separate component.
        // We might need a shared state (useState) or just accept that 
        // opt-in requires a refresh or hydration update.
        // Let's use `useState` for beta state to share across components if possible,
        // but for now, simple mount check + assuming user interactions might reload or we can add a listener.
        
        // Actually, the user toggles it on the *page*.
        // If they toggle it ON, they are ON that page.
        // If they toggle it OFF, they hide it.
        // `BetaGate` handles the content visibility.
        // Navbar visibility is a global concern.
        
        // Let's add a window event listener for storage/custom event 'beta-toggle'
        window.addEventListener('beta-changed', () => {
             isBetaEnabled.value = localStorage.getItem(STORAGE_KEY) === 'true'
        })
    }
})
</script>

<template>
  <div class="flex items-center justify-between max-w-2xl px-4 py-4 mx-auto sm:px-8 gap-4">
    <!-- Brand lockup -->
    <NuxtLink to="/" class="flex items-center gap-2.5 shrink-0" title="Woodmont Civic Association">
      <img src="/logo.svg" alt="" class="w-8 h-8 block dark:hidden" width="32" height="32" />
      <img src="/logo-inverse.svg" alt="" class="w-8 h-8 hidden dark:block" width="32" height="32" />
      <span class="hidden sm:block leading-none">
        <span class="wca-wordmark block text-sm">Woodmont</span>
        <span class="wca-wordmark-sub block text-[9px] mt-0.5">Civic Association</span>
      </span>
    </NuxtLink>
    <!-- Navigation -->
    <div class="text-gray-700 dark:text-gray-200 flex-1 flex flex-wrap justify-end gap-x-5 gap-y-1">
      <NuxtLink
        v-for="link of filteredNavigation"
        :key="link._path"
        :to="link._path"
        active-class="font-bold"
        :class="{ 'hidden sm:inline': link._path === '/covenant' }"
      >
        {{ link.title }}
      </NuxtLink>
    </div>
    <!-- Social icons & Color Mode -->
    <div class="space-x-3 transition text-gray-500 flex items-center shrink-0">
      <a v-if="appConfig.socials?.twitter" :href="`https://twitter.com/${appConfig.socials?.twitter}`" title="Twitter" class="dark:text-gray-100 hover:text-gray-700 dark:hover:text-gray-300"><Icon name="fa-brands:twitter" class="w-5 h-5" /></a>
      <a v-if="appConfig.socials?.mastodon" :href="`https://elk.zone/${appConfig.socials?.mastodon}`" title="Mastodon" class="dark:text-gray-100 hover:text-gray-700 dark:hover:text-gray-300"><Icon name="fa-brands:mastodon" class="w-5 h-5" /></a>
      <ColorModeSwitch class="dark:text-gray-100 hover:text-gray-700 dark:hover:text-gray-300" />
    </div>
  </div>
</template>
