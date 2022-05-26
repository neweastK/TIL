<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <main class="form-signin w-100 m-auto">
      <form @submit.prevent="login(credentials)">
        <img class="mb-4" src="" alt="" width="72" height="57">
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

        <div class="form-floating">
          <input v-model="credentials.username" type="text" class="form-control" id="username" placeholder="name@example.com">
          <label for="username">Email address</label>
        </div>
        <div class="form-floating">
          <input v-model="credentials.password" type="password" class="form-control" id="password" placeholder="Password">
          <label for="password">Password</label>
        </div>

        <div class="checkbox mb-3">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        <p class="mt-5 mb-3 text-muted">&copy; 2017–2022</p>
      </form>
    </main>


    <!-- <form @submit.prevent="login(credentials)">
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
    <div id="my-signin2" style="display: none"></div> -->
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

<style>
  body {
    height: 100%;
  }

  /* body {
    display: flex;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
    background-color: #f5f5f5;
  } */

  .form-signin {
    max-width: 330px;
    padding: 15px;
  }

  .form-signin .form-floating:focus-within {
    z-index: 2;
  }

  .form-signin input[type="email"] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
  }

  .form-signin input[type="password"] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
  }

</style>