<template>

  <div class="container"> 

    <div class="header">

      <img src="../static/logo.png" class="logo">
  
    </div>

    <div class="body-content">

      <div class="form">

        <div class="content-form">

          <h1 class="title-form">Entrar</h1>

          <input type="text" required class="input-form" placeholder="Email ou número de telefone" v-model="user.username">

          <input type="password" required class="input-form" placeholder="Senha" v-model="user.password">

          <button class="btn-form" v-on:click="login()">Entrar</button>

          <div class="help-form">

            <div class="left-form">

              <div class="checkbox">

                <input type="checkbox" class="check-style">

              </div>

              <div class="text-remember">
              
                <p class="remember-me">Lembre-se de mim?</p>

              </div>

            </div>

            <div class="right-form">

              <a href="#">Precisa de ajuda?</a> 

            </div>

          </div>

          <div class="connect-facebook"> 

            <a href="#" class="text-facebook">Conectar com o facebook</a>
          
          </div>

          <div class="new-user"> 

            <p class="text-user">Novo por aqui? <a class="a-newUser" v-on:click="$router.push('/register')">Assine agora.</a></p>
          
          </div>

          <div class="content-captcha">

            <p class="text-captcha"> 
            
              Esta página é protegida pelo Google reCAPTCHA para garantir que você não é um robô. <a href="#" class="link-captcha">Saiba mais.</a>

            </p>
          
          </div>

        </div>

      </div>


    </div>


  </div>

</template>

<script>
  
  export default {
    name: 'IndexPage',

    data(){
      
      return{

        path:{
          route: '/register'
        },

        user:{
          username: '',
          password: '',
        }

      }

    },

    methods:{

      login: function(){

        if(this.user.username && this.user.password){

          this.$auth.loginWith("local", {data: this.user}).then(() => {
          })

        } else {
          alert("Preencha todos os campos!")
        }


      }


    }
  }

</script>

<style lang="scss" scoped>

  @import "@/layouts/scss/reset.scss";
  @import "@/layouts/scss/home.scss";

</style>
