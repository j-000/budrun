<template>
  <div>
    <h1 class="mb-4 mt-4">Users</h1>
    <div v-if="spinner" class="spinner-border text-success" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <div v-else>
      <div class="card-columns">
        <div v-for="user in users" :key="user.id" class="card">
          <div @click="$router.push(`/users/${user.id}`)" class="card-body">
            <h5 class="card-title">{{user.username}}
              <svg v-if="user.verified" width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-bookmark-check-fill" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4 0a2 2 0 0 0-2 2v13.5a.5.5 0 0 0 .74.439L8 13.069l5.26 2.87A.5.5 0 0 0 14 15.5V2a2 2 0 0 0-2-2H4zm6.854 5.854a.5.5 0 0 0-.708-.708L7.5 7.793 6.354 6.646a.5.5 0 1 0-.708.708l1.5 1.5a.5.5 0 0 0 .708 0l3-3z"/>
              </svg>
              <svg v-else width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-bookmark-x" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M2 2a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v13.5a.5.5 0 0 1-.777.416L8 13.101l-5.223 2.815A.5.5 0 0 1 2 15.5V2zm2-1a1 1 0 0 0-1 1v12.566l4.723-2.482a.5.5 0 0 1 .554 0L13 14.566V2a1 1 0 0 0-1-1H4z"/>
                <path fill-rule="evenodd" d="M6.146 5.146a.5.5 0 0 1 .708 0L8 6.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 7l1.147 1.146a.5.5 0 0 1-.708.708L8 7.707 6.854 8.854a.5.5 0 1 1-.708-.708L7.293 7 6.146 5.854a.5.5 0 0 1 0-.708z"/>
              </svg>
            </h5>
            <ul class="list-group">
              <li class="list-group-item d-flex justify-content-between align-items-center">
                <strong>Adverts</strong> 
                <span class="badge badge-primary badge-pill">{{user.adverts.count}}</span>
              </li>
            </ul>
            <p class="card-text"></p>
            <p class="card-text"><small class="text-muted">{{user.joined}}</small></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Users',
  data(){
    return {
      users: [],
      spinner: true
    }
  },
  beforeCreate(){
    axios
      .get('http://localhost:5000/api/users')
      .then((response) => {
        this.users = response.data.users
      })
      .catch((error) => {alert(error)})
      .finally(() => {this.spinner = false})
  }
}
</script>

<style>
.card{
  max-width: 300px;

}
.card:hover{
  transform: scale(1.03);

}
.card-body:hover{
  cursor: pointer!important;
}
</style>