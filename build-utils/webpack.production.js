const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = () => {
	return {
		optimization: {
			minimizer: [
				new UglifyJsPlugin({
					cache: true,
					parallel: true,
				}),
				new OptimizeCSSAssetsPlugin({}),
			],
			splitChunks: {
				chunks: 'all',
				name: 'common',
			},
		},
	};
};
