<template>
	<div class="here">
		This Vue.js app has the following message to you:
		<br>
		<span>{{ message }}</span>
	</div>
</template>
<script>
export default {
	name: 'HomeApp',
	data() {
		return {
			message: 'Are you the coolest?',
		};
	},
};
</script>

<style lang="scss" scoped>
.here {
	margin-top: 1rem;
	font-size: 0.7rem;
}
span {
	text-decoration: underline;
}
</style>


