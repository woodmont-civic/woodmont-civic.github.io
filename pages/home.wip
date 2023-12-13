<!-- <template>
  <pre>
    {{ data }}
  </pre>
  <div v-for="title in data" :key="title.slug">
    <pre>
      {{ title }}
    </pre>
    <NuxtLink :to="{ name: 'blog-slug', params: { slug: title.slug } }">
      {{ title.title }}
    </NuxtLink>
  </div>
</template> -->

<template>
  <main>
    <ContentQuery path="/" :only="['body']" :find="'one'">
      <template #default="{ data }"> 
        <pre>
          {{ data.body.toc }}
        </pre>
        <ul>
          <!-- <li v-for="author of data" :key="author.name">
            {{ author.name }}
          </li> -->
        </ul>
      </template>
      <!-- <template #not-found>
        <p>No authors found.</p>
      </template> -->
    </ContentQuery>
  </main>
</template>

<!-- <script setup>
const { data } = await useAsyncData('home', () => queryContent('/').only(['body']).findOne())
</script> -->
