<template>
  <div>
    <div v-if="spinner" class="spinner-border text-success" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <div v-else>
      <div class="row">
        <div class="col-md-8 m-auto">
          <div class="jumbotron p-0 pb-5">
            <div class="alert alert-info">
              <strong>
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-shield-fill-check" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M8 .5c-.662 0-1.77.249-2.813.525a61.11 61.11 0 0 0-2.772.815 1.454 1.454 0 0 0-1.003 1.184c-.573 4.197.756 7.307 2.368 9.365a11.192 11.192 0 0 0 2.417 2.3c.371.256.715.451 1.007.586.27.124.558.225.796.225s.527-.101.796-.225c.292-.135.636-.33 1.007-.586a11.191 11.191 0 0 0 2.418-2.3c1.611-2.058 2.94-5.168 2.367-9.365a1.454 1.454 0 0 0-1.003-1.184 61.09 61.09 0 0 0-2.772-.815C9.77.749 8.663.5 8 .5zm2.854 6.354a.5.5 0 0 0-.708-.708L7.5 8.793 6.354 7.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/>
                </svg>
                Stay safe
              </strong><br>Always meet in public spaces and inform a family member or a friend.
              Read more on <a href="#">how to stay safe</a>.
            </div>
            <h1 class="display-5">{{ad.title}}</h1>
            <p class="lead">{{ad.text}}</p>
            <p>
              <a href="https://www.google.com/maps" target="_blank">
                <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-geo-alt" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M12.166 8.94C12.696 7.867 13 6.862 13 6A5 5 0 0 0 3 6c0 .862.305 1.867.834 2.94.524 1.062 1.234 2.12 1.96 3.07A31.481 31.481 0 0 0 8 14.58l.208-.22a31.493 31.493 0 0 0 1.998-2.35c.726-.95 1.436-2.008 1.96-3.07zM8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10z"/>
                  <path fill-rule="evenodd" d="M8 8a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
                </svg>
                {{ ad.location }}
              </a>
            </p>
            <p>Posted by <strong><a href="#">{{ ad.owner }}</a></strong> on {{ad.timestamp}}</p>
          </div>
          <hr>
          <div class="list-group mb-3">
            <a v-for="resp in responses" :key="resp.id" 
              href="javascript:void(0)" class="list-group-item list-group-item-action">
              <div class="d-flex w-100 justify-content-between">
                <h5 class="mb-1">{{resp.user}}</h5>
                <small>{{resp.timestamp}}</small>
              </div>
              <p class="mb-1">{{resp.text}}</p>
            </a>
          </div>
          <hr>
          <input v-model="email" class="form-control mb-2" type="text" name="email" id="email" placeholder="Email">
          <textarea v-model="reply" class="form-control" rows="10"></textarea>
          <a @click="send_reply" class="btn btn-info mt-3">Send</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Advert',
  data(){
    return {
      ad: '',
      responses: [],
      spinner: true,
      reply: '',
      email: ''
    }
  },
  beforeCreate(){
    axios
      .get('http://localhost:5000/api/adverts/' + this.$route.params.advert_id)
      .then((response) => {
        if(response.data.error){
          this.$router.push('/')
        }
        this.ad = response.data
      })
      .catch((error) => {alert(error)});
    axios
      .get('http://localhost:5000/api/adverts/' + this.$route.params.advert_id + '/responses')
      .then((response) => {
        this.responses = response.data.responses
      })
      .catch((error) => {alert(error)})
      .finally(() => {
        this.spinner = false;
      })
  },
  methods:{
    send_reply(){
      axios
        .post('http://localhost:5000/api/adverts/' + this.$route.params.advert_id + '/responses', JSON.stringify({
          email: this.email,
          reply: this.reply
        }), {headers:{'Content-Type':'application/json'}})
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          alert(error);
        })
    }
  }
}
</script>

<style>

</style>