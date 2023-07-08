
<template>
  <!-- <main>
  </main> -->
  <div class="form-container" >
    <ContentDoc />
  </div>

  <div v-html="formHTML" class="form-container"></div>
</template>

<script>
export default {
  data() {
    return {
      formHTML: '<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScJrB_a_jYypj_mwhksILpFXPCk_7Tzb72PuEe-Q382SDke3Q/viewform?embedded=true" width="640" height="1500" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>', // The embed code from Google Forms goes here
    };
  },
};
</script>

<style scoped>
.form-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%; /* Adjust this as needed */
}
</style>
