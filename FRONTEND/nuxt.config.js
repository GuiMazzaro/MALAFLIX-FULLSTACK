export default {
  ssr: false,

  head: {
    title: 'malaflix',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  css: [
      'primeflex/primeflex.css',
      "@/layouts/scss/reset.scss",
      "@/layouts/scss/home.scss",
      "@/layouts/scss/register.scss",
      "@/layouts/scss/index.scss",
  ],

  plugins: [
  ],

  components: true,

  buildModules: [
  ],

  modules: [
    'primevue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/auth',
  ],

  axios: {
    baseURL: '/',
  },

  auth:{
    strategies:{
      local:{
        endpoints:{
          login:{
            url: "http://localhost:8000/api/version/authentication/token/login/",
            method: "post",
            propertyName: "auth_token"
          },
          logout:{
            url: "http://localhost:8000/api/version/authentication/token/logout/",
            method: "post",
            propertyName: "auth_token"
          },
          user:{
            url: "http://localhost:8000/api/version/users/me/",
            method: "get",
            propertyName: false
          }
        },
        tokenType: "Token",
        tokenName: "Authorization",
      }
    },
    redirect:{
      login: "/",
      home: "/home"
    }
  },

  build: {
    transpile: ['primevue'],
  },

  primevue:{
    theme: "saga-blue",
    ripple: true,
    components:[
      'Dropdown', 'Avatar', 'Sidebar', 'Carousel', 'Dialog',
    ],
  }
}
