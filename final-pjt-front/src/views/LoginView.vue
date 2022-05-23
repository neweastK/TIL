<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>


    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input v-model="credentials.username" type="text" id="username" required />
      </div>
      <div>
        <label for="password">password: </label>
        <input v-model="credentials.password" type="password" id="password" required />
      </div>

      <button>Login</button>


    
    </form>
    <div v-on:click="GoogleLoginBtn">구글</div>
    <div id="my-signin2" style="display: none"></div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login']),
      GoogleLoginBtn:function(){
        var self = this;
        window.gapi.signin2.render( 'my-signin2', {
          scope: 'profile email',
          width: 240,
          height: 50,
          longtitle: true,
          theme: 'dark',
          onsuccess: this.GoogleLoginSuccess,
          onfailure: this.GoogleLoginFailure,
        });
        setTimeout(function (){
          if (!self.googleLoginCheck){
            const auth = window.gapi.auth2.getAuthInstance();
            auth.isSignedIn.get();
            document.querySelector('.abcRioButton').click();
          }
        }, 1500)
      },
      async GoogleLoginSuccess(googleUser){
        const googleEmail = googleUser.getBasicProfile().getEmail();
        if (googleEmail !== 'undefined') {
          console.log(googleEmail);
        }
      },
      GoogleLoginFailure(error) {
        console.log(error);
    },
  }
}
</script>

<style></style>