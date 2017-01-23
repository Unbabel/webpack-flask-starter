import Vue from 'vue/dist/vue';
import LoginValidator from './LoginValidator';

/*
 * Sample VueJS login form
 */

const app = new Vue({
  el: '#vue-demo-login',
  data: {
    username: '',
    password: '',
  },
  computed: {
    canSubmit() {
      return LoginValidator.usernameIsValid(this.username)
          && LoginValidator.passwordIsValid(this.password);
    },
  },
  methods: {
    applyDummyData() {
      this.username = 'johnsardine';
      this.password = 'myC00lPassword';
    },
    resetForm() {
      this.username = '';
      this.password = '';
    },
    didSubmitForm() {
      console.log('Login username %s with password %s', this.username, this.password);
      setTimeout(() => this.resetForm(), 1000);
    },
  },
});

export default app;
