<template>
  <router-view />
</template>

<Modal visible="false"></Modal>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

}

.signup-container, .login-container, .admin-login-container{
  background-size: cover;
  min-height: 51vh;
  background-repeat: no-repeat;
  background-position: center center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.signup, .login {
  position: absolute;
  justify-content: center;
  max-width: 100%;
  background-color: transparent;
  border: 2px solid rgba(255,255,255); /*rgba(118, 118, 118, 0.35);*/
  backdrop-filter: blur(20px);
  box-shadow: 0px 00px 30px rgba(255, 255, 255, 0.45);
  color: black;
  border-radius: 15px;
  padding: 12px 40px;
  margin-left:0%; 
}

.signup input, .login input{
  width:288px;
  height:40px;
  display:flex;
  padding-left:20px;
  margin-top:10px;
  margin-bottom:30px;
  margin-left:auto;
  margin-right:auto;
  border-radius: 20px;
  border: 2px solid rgba(100, 100, 100, .3);
}

.signup button, .login button{
  width: 100%;
  height: 45px;
  background: black;
  border: none;
  outline: none;
  border-radius: 40px;
  box-shadow: 0 0 10px rgba(0, 0, 0, .1);
  cursor: pointer;
  font-size: 16px;
  color: white;
  font-weight: 600;
  margin-bottom:20px;
}

.signup h3, span {
  color:white;
}

</style>
