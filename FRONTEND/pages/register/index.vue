<template> 

    <div class="container"> 

      <div class="body-content"> 

        <div class="form">
        
          <div class="content-form"> 

          <h1 class="title-form">Registrar</h1>

          <input type="text" required class="input-form" placeholder="Nome de Usuário" v-model="dataUser.nameUser">

          <input type="text" required class="input-form" placeholder="Email" v-model="dataUser.email">

          <input type="password" required class="input-form" placeholder="Senha" v-model="dataUser.password">

          <input type="password" required class="input-form" placeholder="Confirme sua senha" v-model="dataUser.confirmedPassword">

          <input type="text" required class="input-form" placeholder="Telefone" v-model="dataUser.phone">

          <input type="text" required class="input-form" placeholder="Data de Nascimento" v-model="dataUser.dateBorn">

          <Dropdown v-model="selectedPlan" :options="planArray" optionLabel="nomeAssinatura" placeholder="Select a Plan" class="input-form-plan"/>
          
          <button class="btn-form" v-on:click="verifyLogin()">Cadastrar</button>

          </div>
        
        </div>

      </div>
    
    </div>

</template>

<script>

export default {
  
  name: 'RegisterPage',

  data(){

    return{

      selectedPlan: null,
      planArray: [],

      dataUser:{
        nameUser: "",
        email: "",
        password: "",
        confirmedPassword: "",
        phone: "",
        dateBorn: "",
        plan: 0,
        idUser: 0,
        photo: null,
      },

    }

  },

  methods:{

    verifyLogin: function(){
      
      if(this.dataUser.password === this.dataUser.confirmedPassword){

          this.registerUserDjango();

      
      } else {

        alert("As senhas estão diferentes!");

      }

    },

    registerUserDjango: async function(){

      console.log(this.dataUser);

      const body = {
        username: this.dataUser.nameUser,
        password: this.dataUser.password,
        email: this.dataUser.email
      };

      this.$axios.post(this.$store.state.BASE_URL + "/api/version/users/", body).then((response) => {
        
        alert("Usuário cadastrado com sucesso!");
      
        this.dataUser.idUser = response.data.id;
        this.dataUser.plan = this.selectedPlan.id;

        this.registerUser();

      }).catch((error) => {
          alert("Atenção, usuário não cadastrado!");
          console.log(error);
          this.user = null;
        });

    },

    registerUser: async function(){

      const body = [{
        nome: this.dataUser.nameUser,
        email: this.dataUser.email,
        fone: this.dataUser.phone,
        dataNascimento: this.dataUser.dateBorn,
        senha: this.dataUser.password,
        plano: this.dataUser.plan,
        idUser: this.dataUser.idUser,
        foto: null
      }];

      this.$axios.post(this.$store.state.BASE_URL + "/usuarios/", body).then((response) => {

        alert("Usuário Cadastrado com sucesso")
      
      }).catch((error) => {
          alert("Usuário Não cadastrado")
          console.log(error);
        });

    }

  },

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/planos").then((response) =>{

      this.planArray = response.data;
    
    }).catch((error) => {
        console.log("Vish, deu ruim!");
        console.log(error);
    });

  }




}

</script>

<style lang="scss" scoped>

  @import "@/layouts/scss/reset.scss";
  @import "@/layouts/scss/register.scss";

</style>