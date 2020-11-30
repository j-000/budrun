<template>
  <div class="row">
    <div class="col-md-8 m-auto">
      <h1>Adverts</h1>
      <div v-if="spinner" class="spinner-border text-success" role="status">
        <span class="sr-only">Loading...</span>
      </div>
      <div v-else class="list-group">
        <Advert class="mb-2 border border-info" v-for="ad in adverts" :key="ad.id" :ad=ad />
      </div>
     </div>
  </div>
</template>

<script>
import axios from 'axios'
import Advert from '../components/Advert'

export default {
  name: 'Home',
  components:{
    Advert
  },
  data(){
    return {
      adverts: [],
      spinner: true
    }
  },
  methods: {

  },
  beforeCreate(){
    axios
      .get('http://localhost:5000/api/adverts')
      .then((response) => {
        this.adverts = response.data.adverts
      })
      .catch((error) => {alert(error)})
      .finally(() => {this.spinner = false})
  }
}
</script>