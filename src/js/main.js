/* global document */
/*
 * Sample string reverse function
 */
import jQuery from 'jquery';
import Vue from 'vue/dist/vue';
import stringReverse from './string-reverse';
import LoginValidator from './LoginValidator';

// Make jQuery available for bootstrap
window.jQuery = jQuery;

/*
 * Sample jQuery usage
 */
const reversibleMessage = jQuery('.js-reversible-message');

jQuery(document).on('click', '.js-reverse-message', (e) => {
  e.preventDefault();
  const text = reversibleMessage.text();
  const reversedString = stringReverse(text);
  reversibleMessage.text(reversedString);
});

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
