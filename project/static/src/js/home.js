import Vue from 'vue';
import HomeApp from '../vue/apps/HomeApp.vue';

console.log('hello home!');

const app = new Vue({
	el: '.app-mount',
	components: {
		homeApp: HomeApp,
	},
});

export default app;
