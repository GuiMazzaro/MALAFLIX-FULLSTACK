<template> 

  <div class="black">

    <div class="header-home"> 

    <button
        class="btn"
        v-on:click="showSidebar = showSidebar ? false : true"
    > 

      <Avatar
          class="avatarUser"
          :image="$store.state.BASE_URL + $store.state.usuario.foto"
          size="xlarge"
          shape="circle"
          v-if="$store.state.usuario.foto"      
      />

      <Avatar
          class="avatarUser"
          image="error404.jpg"
          size="xlarge"
          shape="circle"
          v-else
      />

      </button>

    </div>

    <Sidebar
      :visible.sync="showSidebar"
      :dismissable="true"
      :baseZIndex="1000"
      :showCloseIcon="false"
      class="customSidebar"
    >   

      <p class="label-title">Informações do Usuário: </p>

      <div class="infomations">
        <p class="label-data">Nome de Usuário: {{$store.state.usuario.nome}}</p>
        <p class="label-data">Email: {{$store.state.usuario.email}}</p>
        <p class="label-data">Telefone: {{$store.state.usuario.fone}}</p>
        <p class="label-data">Data de Nascimento: {{$store.state.usuario.dataNascimento}}</p>
        <p class="label-data">ID User: {{$store.state.usuario.idUser}}</p>
        <p class="label-data">Plano: {{$store.state.usuario.plano}}</p>
      </div>

      <button v-on:click="$auth.logout()" class="btn-left"> 
        Fazer Logout
      </button>

    </Sidebar>

    <Nuxt />

    <footer></footer>

    <div class="content-infos">

      Banner! terá atualizações.
  
    </div>

    <div class="align-center">

      <p class="title-films">Filmes</p>

      <Carousel :value="dataMovies" :numVisible="3" :numScroll="3" :responsiveOptions="responsiveOptions">

        <template #item="slotProps">

          <div class="movie-item">

                  <div class="movie-content">

                    <button
                      class="btn"
                      v-on:click="showMovie(slotProps.data)"
                    > 

                      <img :src="$store.state.BASE_URL + slotProps.data.capa" class="movie-image"/>

                    </button>

                  </div>

          </div>

        </template>

      </Carousel>

      <Sidebar
      :visible.sync="showSideFilme"
      :dismissable="true"
      :baseZIndex="1000"
      :showCloseIcon="false"
      class="customSidebar"
      >   

      <p class="label-title">Informações do Filme: </p>

      <div class="infomations">
      
        <p class="label-data">Nome: {{nomeFilme}}</p> <br>
        <p class="label-data">Descricao: {{descricao}}</p>

      </div>

      <button v-on:click="favoritar()" class="btn-left"> 
        Favoritar
      </button>

    </Sidebar>

      <p class="title-films">Favoritos</p>

    </div>

  </div>

</template>

<script>

export default {

  middleware: "auth",
  
   data() {
    return {
      showSidebar: false,
      showSideFilme: false,
      nomeFilme: "", 
      descricao: "",
      dataMovies: [],

      responsiveOptions: [
			{
				breakpoint: '1024px',
				numVisible: 3,
				numScroll: 3
			},
			{
				breakpoint: '600px',
				numVisible: 2,
				numScroll: 2
			},
			{
				breakpoint: '480px',
				numVisible: 1,
				numScroll: 1
			}
		]
    };
  },

  methods:{

    showMovie: function(data){

      this.nomeFilme = data.nome;
      this.descricao = data.descricao;

      this.showSideFilme = this.showSideFilme ? false : true
      
    },

    favoritar: function(){

      alert("Em desenvolmento")

    }

  },

  created(){

    this.$axios.get(this.$store.state.BASE_URL + "/usuarios?user=" + this.$auth.$state.user.id).then((response) => {

      this.$store.dispatch("SET_USER", response.data[0]);

    }).catch((error) => {

        console.log("Da uma olha no código ai irmão");
        console.log(error);

    });

    this.$axios.get(this.$store.state.BASE_URL + "/filmes").then((response) =>{

      this.dataMovies = response.data; 
      this.$store.dispatch("SET_FILMES", response.data);

      console.log(this.dataMovies)

    }).catch((error) => {

        console.log("Da uma olha no código ai irmão -- FILMES");
        console.log(error);

    });

  }

}

</script>

<style lang="scss" scoped>

  @import "@/layouts/scss/reset.scss";
  @import "@/layouts/scss/index.scss";

</style>