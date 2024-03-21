<template>
  <div>
    <h1>User List</h1>
    <ul>
      <li v-for="user in users" :key="user.id">{{ user.name }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    };
  },
  created() {
    axios.get('http://127.0.0.1:5000/community')
      .then(response => {
        this.users = response.data;
        console.log(this.users)
      })
      .catch(error => {
        console.error('Error fetching users', error);
      });
  },
};
</script>
     