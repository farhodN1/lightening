<template>
  <div>
    <div id="userList" v-for="(key, index) in Object.keys(data)" :key="index">
      <p>{{ data[key].username }}</p>

      <img :src="data[key].profilePicture" alt="Profile Picture" >
    </div>
  </div>
</template> 

<style>
#userList{
  background-color: grey;
  width:40%;
  height:auto;
  padding: 10px;
  margin: 10px; 
  display: block;
}
#userList img{
  width:50px;
  height:50px;
  border-radius: 50%;
  float: left;
}
#userList p{
  font-size: 30px;
}
h1{
  font-size:20px;

}

body{
  background:lime;
  padding: 0;
  margin: 0;
}
</style>

<script>
export default {
  data() {
    return {
      data: null,
    };
  },
  methods: {
    GetData() {
      fetch("http://127.0.0.1:5000/community")
        .then(response => response.json())
        .then(data => {
          this.data = data; 
          console.log(data)
        })
        .catch(error => console.error('Ошибка:', error));
      }
    },
  created(){
      this.GetData()
    }
};
</script>