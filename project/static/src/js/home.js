import Vue from 'vue';
import jQuery from 'jquery';
import HomeApp from '@Source/vue/apps/HomeApp';

window.jQuery = jQuery;

console.log('hello home!');

const app = new Vue({
	el: '.app-mount',
	components: {
		homeApp: HomeApp,
	},
});

export default app;
