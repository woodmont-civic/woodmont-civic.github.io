<script setup lang="ts">
const { page } = useContent()

const images = computed(() => page.value.gallery || [])
const isLightboxOpen = ref(false)
const selectedImage = ref<any>(null)

function openLightbox(image: any) {
  selectedImage.value = image
  isLightboxOpen.value = true
}

function closeLightbox() {
  isLightboxOpen.value = false
  selectedImage.value = null
}
</script>

<template>
  <div class="not-prose">
    <div v-if="images.length === 0" class="p-8 text-center text-gray-500 bg-gray-100 dark:bg-gray-800 rounded-xl border-2 border-dashed border-gray-300 dark:border-gray-700">
      <p>No images found in gallery frontmatter.</p>
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 md:gap-6">
      <div 
        v-for="(image, index) in images" 
        :key="index"
        class="group relative aspect-square overflow-hidden rounded-xl bg-gray-100 dark:bg-gray-800 cursor-zoom-in shadow-md hover:shadow-xl transition-all duration-300 border-4 border-white dark:border-gray-700"
        @click="openLightbox(image)"
      >
        <img 
          :src="image.src" 
          :alt="image.alt || image.caption || 'Gallery image'"
          loading="lazy"
          class="h-full w-full object-cover transition-transform duration-500 group-hover:scale-110"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-4">
          <p class="text-white text-sm font-medium line-clamp-2">
            {{ image.caption }}
          </p>
        </div>
      </div>
    </div>

    <!-- Simple Lightbox Modal -->
    <Teleport to="body">
      <div 
        v-if="isLightboxOpen" 
        class="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 backdrop-blur-sm p-4 transition-all duration-300"
        @click="closeLightbox"
      >
        <button 
          class="absolute top-4 right-4 text-white/50 hover:text-white p-2"
          @click.stop="closeLightbox"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
        
        <div class="max-w-5xl max-h-screen w-full flex flex-col items-center" @click.stop>
            <img 
              :src="selectedImage.src" 
              :alt="selectedImage.alt || selectedImage.caption"
              class="max-h-[80vh] w-auto object-contain rounded-lg shadow-2xl mb-4"
            />
            <p v-if="selectedImage.caption" class="text-white text-center text-lg font-medium">
                {{ selectedImage.caption }}
            </p>
        </div>
      </div>
    </Teleport>
  </div>
</template>
