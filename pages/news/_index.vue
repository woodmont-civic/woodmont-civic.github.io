<template>
    <pre>{{ navigation }}</pre>
    <div>
      <h1 class="text-7xl font-black text-center">New on the blog</h1>
      <div v-for="post in posts" :key="post.title">
        <h2 class="mt-2 text-3xl font-semibold">{{ post.title }}</h2>
      </div>
    </div>
</template>

<script setup>
const { data: navigation } = await useAsyncData('navigation', () => fetchContentNavigation())
</script>
