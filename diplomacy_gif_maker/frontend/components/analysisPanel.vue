<template>
  <div>
    <div @click="displayActive = !displayActive">
      <img :src="panelData.url" alt="Descripion" class="mw-100 db outline black-10" />
      <dl class="mt2 f6 lh-copy">
        <dt class="clip">{{ panelData.title }}</dt>
        <dd class="ml0 black truncate w-100">{{ panelData.title }}</dd>
        <dt class="clip">Plot Description</dt>
        <dd class="ml0 gray w-100">{{ panelData.description }}</dd>
      </dl>
      <!-- {{ panelData.id }} -->
    </div>
    <!-- The Modal -->
    <div id="myModal" class="modal" v-bind:class="{ active: displayActive }">

      <!-- The Close Button -->
      <span class="close" @click="displayActive = false">&times;</span>

      <!-- Modal Content (The Image) -->
      <img :src="panelData.url" alt="Descripion" class="" />

      <!-- Modal Caption (Image Text) -->
      <div id="caption">
        <dl class="mt2 f6 lh-copy">
          <dt class="clip">{{ panelData.title }}</dt>
          <h1 class="ml0 white w-100">{{ panelData.title }}</h1>
          <dt class="clip">Plot Description</dt>
          <dd class="ml0 white w-100">{{ panelData.description }}</dd>
        </dl>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['panelData'],
    data() {
      return {
        id: this.panelData.id,
        displayActive: false,
      }
    },
    methods: {
    }
  }
</script>

<style>
  /* The Modal (background) */
  .modal {
    display: none;
    /* Hidden by default */
    position: fixed;
    /* Stay in place */
    z-index: 1;
    /* Sit on top */
    padding-top: 100px;
    /* Location of the box */
    left: 0;
    top: 0;
    width: 100%;
    /* Full width */
    height: 100%;
    /* Full height */
    overflow: auto;
    /* Enable scroll if needed */
    background-color: rgb(0, 0, 0);
    /* Fallback color */
    background-color: rgba(0, 0, 0, 0.9);
    /* Black w/ opacity */
  }

  .active {
    display: block;
  }

  /* Modal Content (Image) */
  .modal-content {
    margin: auto;
    display: block;
    width: 80%;
    max-width: 700px;
  }

  /* Caption of Modal Image (Image Text) - Same Width as the Image */
  #caption {
    margin: auto;
    display: block;
    width: 80%;
    max-width: 700px;
    text-align: center;
    color: #ccc;
    padding: 10px 0;
    height: 150px;
  }

  /* Add Animation - Zoom in the Modal */
  .modal-content,
  #caption {
    animation-name: zoom;
    animation-duration: 0.6s;
  }

  @keyframes zoom {
    from {
      transform: scale(0)
    }

    to {
      transform: scale(1)
    }
  }

  /* The Close Button */
  .close {
    position: absolute;
    top: 15px;
    right: 35px;
    color: #f1f1f1;
    font-size: 40px;
    font-weight: bold;
    transition: 0.3s;
  }

  .close:hover,
  .close:focus {
    color: #bbb;
    text-decoration: none;
    cursor: pointer;
  }

  /* 100% Image Width on Smaller Screens */
  @media only screen and (max-width: 700px) {
    .modal-content {
      width: 100%;
    }
  }
</style>