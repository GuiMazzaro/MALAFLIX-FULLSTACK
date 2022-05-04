export default {

    SET_USER(context, payload){
        console.log("vuex:" + payload);
        context.commit("USER", payload);
    },

    SET_PLAN(context, payload){
        console.log("vuex:" + payload);
        context.commit("PLAN", payload);
    },

    SET_FILMES(context, payload){
        console.log("vuex:" + payload);
        context.commit("FILMES", payload);
    }


}