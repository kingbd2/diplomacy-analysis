<template>
  <div class="container">
    <article class="fl pa3 pa4-ns bg-white black-70 f3 ">
      <header class="bb b--black-70 pv4">
        <h3 class="f2 fw7 ttu tracked lh-title mt0 mb3 avenir">Diplomacy Game Analysis</h3>
        <h4 class="f3 fw4 i lh-title mt0">War On Drugs</h4>
      </header>
      <div class="mw9 center ph3-ns times" >
        <div class="cf ph2-ns">
          <div class="fl w-100 w-10-ns pa2" v-for="item in panelData" :key="item.id">
            {{item.id}}
            <analysis-panel :panelData="item"></analysis-panel>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
  import analysisPanel from '~/components/analysisPanel.vue'

  export default {
    components: {
      analysisPanel
    },
    data() {
      return {
        panelData: [{
            id: 0,
            title: 'Game map',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/map_background.svg',
            description: 'This is the game map.'
          },
          {
            id: 1,
            title: 'Sample Orders',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/merged2.svg',
            description: 'A sample of orders.'
          },
          {
            id: 2,
            title: 'Units by Country Over Time',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/unitsByCountry.png',
            description: 'This is a summary of units held by each country over the years.'
          },
          {
            id: 3,
            title: 'Proportion of Order Types by Country',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/orderProportionByCountry_wDestroyed.png',
            description: 'Every season, a player representing a country plans and commits orders for each unit. This plot shows the types of moves that each player has made during the game, normalized by the time spent in the game.'
          },
          {
            id: 4,
            title: 'Order Success Rate by Country',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/successRatioByCountry.png',
            description: 'Successful orders normalized by time in the game.'
          },
          {
            id: 5,
            title: 'Or, Order Failure Rate by Country',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/failureRatioByCountry.png',
            description: 'Failed orders normalized by time in the game.'
          },
          {
            id: 6,
            title: 'Which Country was the Biggest Bitch?',
            url: 'https://websiteassetsstorage.blob.core.windows.net/images/destroyedByCountry.png',
            description: 'The number of units destroyed by country.'
          },

        ],
      };
    },
  }
</script>

<style>
  .container {
    margin: 0 auto;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
  }

  .title {
    font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
      'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    display: block;
    font-weight: 300;
    font-size: 100px;
    color: #35495e;
    letter-spacing: 1px;
  }

  .subtitle {
    font-weight: 300;
    font-size: 42px;
    color: #526488;
    word-spacing: 5px;
    padding-bottom: 15px;
  }

  .links {
    padding-top: 15px;
  }
</style>