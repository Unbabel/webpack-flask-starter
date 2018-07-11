<template>
	<div class="here">
		This Vue.js app has the following message to you:
		<br>
		<span>{{ message }}</span>
		<br>
		<img class="detective" src="../img/poirot.png" alt="The worlds' greatest detective">
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
	margin-top: 2rem;
	font-size: 0.7rem;
}
span {
	text-decoration: underline;
}
.detective {
	margin-top: 1rem;
	width: 100%;
	max-width: 200px;
	height: auto;
}
</style>
