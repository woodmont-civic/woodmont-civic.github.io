<script setup lang="ts">
const { data: posts } = await useAsyncData('posts-list', () => {
  return queryContent('/posts')
    .where({ _path: { $ne: '/posts' } }) // Exclude the index page itself if it's in the same dir and has same prefix, though usually index is /posts
    .sort({ _file: -1 })
    .find()
})

// Helper to extract year from path or filename
const latestPost = computed(() => {
  if (!posts.value || posts.value.length === 0) return null
  // data is already sorted by _file desc, but let's be safe and use our sorted logic
  const sorted = [...posts.value].sort((a, b) => b._path.localeCompare(a._path))
  return sorted[0]
})

const postsByYear = computed(() => {
  const groups: Record<string, any[]> = {}
  if (!posts.value) return groups

  // Explicitly sort posts by path descending
  const sortedPosts = [...posts.value].sort((a, b) => b._path.localeCompare(a._path))
  
  // Exclude the first post as it's the "Featured" one
  const remainingPosts = sortedPosts.slice(1)

  for (const post of remainingPosts) {
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
    
    <!-- Most Recent / Featured Post -->
    <div v-if="latestPost" class="relative group">
      <div class="flex flex-col md:flex-row bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all overflow-hidden border border-gray-100 dark:border-gray-700">
        <!-- Image placeholder or actual image if available -->
        <div class="h-40 md:h-auto md:w-1/4 bg-gray-100 dark:bg-gray-700 flex items-center justify-center">
            <span class="text-3xl">📰</span>
        </div>
        
        <div class="p-5 md:p-6 flex flex-col justify-center flex-1">
          <div class="uppercase tracking-wide text-xs text-primary-600 dark:text-primary-400 font-semibold mb-1">
            Most Recent
          </div>
          <h2 class="text-xl md:text-2xl font-bold text-gray-900 dark:text-white mb-2 group-hover:text-primary-600 transition-colors">
            <NuxtLink :to="latestPost._path">
              {{ latestPost.navigation?.title || latestPost.title || 'Untitled Post' }}
            </NuxtLink>
          </h2>
          <p v-if="latestPost.description" class="text-gray-600 dark:text-gray-300 mb-4 text-sm md:text-base line-clamp-2">
            {{ latestPost.description }}
          </p>
          <div class="mt-auto">
             <NuxtLink :to="latestPost._path" class="inline-flex items-center text-sm text-primary-600 dark:text-primary-400 font-medium hover:underline">
               Read full article <span class="ml-1 transition-transform group-hover:translate-x-1">→</span>
             </NuxtLink>
          </div>
        </div>
      </div>
    </div>

    <!-- Timeline of Previous Posts -->
    <div v-for="group in postsByYear" :key="group.year" class="flex flex-col md:flex-row gap-2 md:gap-8 relative">
      
      <!-- Left: Year Label (Timeline style) -->
      <div class="w-full md:w-24 flex-shrink-0 pt-0 md:pt-2 relative mb-2 md:mb-0">
        <h3 class="static md:sticky top-24 -ml-0 md:-ml-2 text-xl md:text-3xl font-bold text-gray-400 dark:text-gray-600 
                   md:transform md:-rotate-90 md:origin-top-left whitespace-nowrap">
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
