<template>
	<div class="here">
		Hello Home, {{ message }}....
	</div>
</template>
<script>
export default {
	name: 'HomeApp',
	data() {
		return {
			message: 'are you cool?',
		};
	},
};
</script>

<style lang="scss" scoped>
.here {
	text-decoration: underline;
}
</style>


