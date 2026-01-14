<script setup lang="ts">
interface Props {
  title: string
  description?: string
  url: string
  date?: string
  type: 'newsletter' | 'notebook' | 'article'
  tags?: string[]
}

const props = defineProps<Props>()

const icon = computed(() => {
  switch (props.type) {
    case 'newsletter': return 'heroicons:document-text'
    case 'notebook': return 'heroicons:sparkles'
    default: return 'heroicons:link'
  }
})

const badgeColor = computed(() => {
  switch (props.type) {
    case 'newsletter': return 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300'
    case 'notebook': return 'bg-purple-100 text-purple-800 dark:bg-purple-900/30 dark:text-purple-300'
    default: return 'bg-blue-100 text-blue-800'
  }
})

const typeLabel = computed(() => {
  switch (props.type) {
    case 'newsletter': return 'PDF Archive'
    case 'notebook': return 'Audio Overview'
    default: return 'External Link'
  }
})
</script>

<template>
  <a 
    :href="url"
    target="_blank"
    rel="noopener noreferrer"
    class="block group relative bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-xl p-5 shadow-sm hover:shadow-md transition-all hover:-translate-y-1"
  >
    <div class="flex items-start justify-between mb-3">
        <div class="flex items-center gap-2">
            <span class="p-2 rounded-lg bg-gray-50 dark:bg-gray-700 group-hover:bg-primary-50 dark:group-hover:bg-primary-900/20 text-gray-500 group-hover:text-primary-600 transition-colors">
                <Icon :name="icon" class="w-6 h-6" />
            </span>
            <span v-if="date" class="text-xs font-mono text-gray-400 uppercase">{{ date }}</span>
        </div>
        <span :class="['text-[10px] font-bold px-2 py-1 rounded-full uppercase tracking-wider', badgeColor]">
            {{ typeLabel }}
        </span>
    </div>

    <h3 class="text-lg font-bold text-gray-900 dark:text-gray-100 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors mb-2">
        {{ title }}
    </h3>
    
    <p v-if="description" class="text-sm text-gray-500 dark:text-gray-400 line-clamp-2 mb-4">
        {{ description }}
    </p>

    <div class="flex items-center text-xs font-medium text-primary-600 dark:text-primary-400">
        <span v-if="type === 'notebook'">Listen & Chat</span>
        <span v-else>Download PDF</span>
        <Icon name="heroicons:arrow-right" class="w-4 h-4 ml-1 transition-transform group-hover:translate-x-1" />
    </div>

    <!-- Notebook specific visual flair -->
    <div v-if="type === 'notebook'" class="absolute -right-6 -top-6 w-24 h-24 bg-purple-500/10 rounded-full blur-2xl pointer-events-none group-hover:bg-purple-500/20 transition-all"></div>
  </a>
</template>
