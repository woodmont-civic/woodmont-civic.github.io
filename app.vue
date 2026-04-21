<template>
  <VitePwaManifest />
  <AppLayout>
    <div class="pb-24 md:pb-0">
      <NuxtPage />
    </div>
    <StickyAction />
    <BetaStatus />
  </AppLayout>
  <PwaInstallBanner />
</template>
