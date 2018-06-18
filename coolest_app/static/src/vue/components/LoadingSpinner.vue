<template>
	<div class="c-LoadingSpinner sk-fading-circle">
		<div class="sk-circle1 sk-circle"></div>
		<div class="sk-circle2 sk-circle"></div>
		<div class="sk-circle3 sk-circle"></div>
		<div class="sk-circle4 sk-circle"></div>
		<div class="sk-circle5 sk-circle"></div>
		<div class="sk-circle6 sk-circle"></div>
		<div class="sk-circle7 sk-circle"></div>
		<div class="sk-circle8 sk-circle"></div>
		<div class="sk-circle9 sk-circle"></div>
		<div class="sk-circle10 sk-circle"></div>
		<div class="sk-circle11 sk-circle"></div>
		<div class="sk-circle12 sk-circle"></div>
	</div>
</template>

<script>
export default {
	name: 'LoadingSpinner',
};
</script>


<style lang="scss" scoped>
// @import '~@unbabel/ui/src/_colors';
// @import '~spinkit/scss/spinners/10-fading-circle';

.c-LoadingSpinner {
	margin: 0;

	.sk-circle::before {
		background-color: white;
	}
}
</style>
