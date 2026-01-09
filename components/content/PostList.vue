<script setup lang="ts">
const { data: posts } = await useAsyncData('posts-list', () => {
  return queryContent('/posts')
    .where({ _path: { $ne: '/posts' } }) // Exclude the index page itself if it's in the same dir and has same prefix, though usually index is /posts
    .sort({ _file: -1 })
    .find()
})

// Helper to extract year from path or filename
const postsByYear = computed(() => {
  const groups: Record<string, any[]> = {}
  if (!posts.value) return groups

  // Explicitly sort posts by path descending (creates date-descending effect for YYYY_MM files)
  const sortedPosts = [...posts.value].sort((a, b) => b._path.localeCompare(a._path))

  for (const post of sortedPosts) {
    let year = 'Recent'
    const match = post._path.match(/\/posts\/(\d{4})/)
    if (match) {
      year = match[1]
    }
    
    if (!groups[year]) groups[year] = []
    groups[year].push(post)
  }
  
  // Sort years descending
  // Return an array to guarantee sort order in v-for
  return Object.keys(groups)
    .sort((a, b) => b.localeCompare(a)) // Sort years descending
    .map(year => ({
      year,
      posts: groups[year].sort((a, b) => b._path.localeCompare(a._path))
    }))
    // Filter out the 'Recent' group if it contains the index page or other non-yeared posts
    .filter(group => group.year !== 'Recent')
})
</script>

<template>
  <div class="space-y-6 md:space-y-8">
    <div v-for="group in postsByYear" :key="group.year" class="flex flex-row gap-3 md:gap-8 relative">
      
      <!-- Left: Year Label (Timeline style) -->
      <!-- Mobile: Rotated year or stacked vertical characters to save width? 
           Simple rotation is cleanest for "timeline" feel. -->
      <div class="w-8 md:w-24 flex-shrink-0 pt-4 md:pt-2 relative">
        <h3 class="sticky top-24 -ml-2 md:ml-0 text-lg md:text-3xl font-bold text-gray-300 dark:text-gray-700 
                   transform -rotate-90 md:rotate-0 origin-center md:origin-top-left whitespace-nowrap">
          {{ group.year }}
        </h3>
      </div>

      <!-- Right: Grid of Cards -->
      <div class="flex-1 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 md:gap-4">
        <div v-for="post in group.posts" :key="post._path" 
             class="group relative flex flex-col p-4 bg-white dark:bg-gray-800 rounded-lg shadow-sm hover:shadow-md transition-all border border-gray-100 dark:border-gray-700">
          
          <NuxtLink :to="post._path" class="absolute inset-0 z-10">
            <span class="sr-only">View post</span>
          </NuxtLink>

          <h4 class="text-base font-semibold text-gray-900 dark:text-gray-100 group-hover:text-primary-600 transition-colors mb-1 line-clamp-1">
            {{ post.navigation?.title || post.title || 'Untitled Post' }}
          </h4>
          
          <p v-if="post.description" class="text-xs text-gray-500 dark:text-gray-400 line-clamp-2">
            {{ post.description }}
          </p>
          <p v-else class="text-xs text-gray-400 italic">
            No description available.
          </p>

          <div class="mt-auto pt-2 flex items-center text-[10px] font-medium text-primary-600 dark:text-primary-400 uppercase tracking-wider">
            Read more <span class="ml-1 transition-transform group-hover:translate-x-1">→</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
