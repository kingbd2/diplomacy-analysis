<template>
  <div>
    <img :src="panelData.url" alt="Descripion" class="mw-100 db outline black-10" />
    <dl class="mt2 f6 lh-copy">
      <dt class="clip">{{ panelData.title }}</dt>
      <dd class="ml0 black truncate w-100">{{ panelData.title }}</dd>
      <dt class="clip">Plot Description</dt>
      <dd class="ml0 gray w-100">{{ panelData.description }}</dd>
    </dl>
    <!-- {{ panelData }} -->
  </div>
</template>

<script>
  export default {
    props: ['panelData']
  }
</script>

<style>

</style>