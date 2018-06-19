const path = require('path');
// const HtmlWebPackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
	entry: {
		basic: './project/static/src/scss/styles.scss',
		// this home.js file needs to be in the template so hot reload works
		'js/home': './project/static/src/js/home.js',
	},
	output: {
		path: path.resolve(__dirname, './project/static/dist'),
	},
	resolve: {
		alias: {
			vue$: 'vue/dist/vue.esm.js',
		},
	},
	module: {
		rules: [
			{
				test: /\.vue$/,
				loader: 'vue-loader',
			},
			{
				test: /\.js$/,
				exclude: /node_modules/,
				use: {
					loader: 'babel-loader',
				},
			},
			{
				test: /\.html$/,
				use: [
					{
						loader: 'html-loader',
						options: { minimize: true },
					},
				],
			},
			{
				test: /\.scss$/,
				oneOf: [
					// config for scss inside .vue files
					{
						resourceQuery: /^\?vue/,
						use: [
							'vue-style-loader',
							'css-loader',
							'sass-loader',
						],
					},
					// config for stand-alone .scss files
					{
						use: [
							'css-hot-loader',
							MiniCssExtractPlugin.loader,
							'css-loader',
							'postcss-loader',
							'sass-loader',
						],
					},
				],
			},
		],
	},
	devServer: {
		// path to the static folder in relation to this file
		contentBase: path.join(__dirname, './project/static/'),
		// url to the folder used on the templates to get the static files
		// example: /static/dist/file.css
		publicPath: '/static/dist/',
		watchContentBase: true,
		// port where the dev server will start
		port: 9001,
		proxy: {
			// all the requests that are not /static/dist/ files go to flask
			// 5000 is the default port for flask
			'!(/static/dist/**/**.*)': {
				target: 'http://127.0.0.1:5000',
			},
		},
	},
	plugins: [
		// new HtmlWebPackPlugin({
		// template: './src/index.html',
		// filename: './index.html',
		// inject: true,
		// }),
		new MiniCssExtractPlugin({
			// set the folder where the css files will go
			// the line below will cause /static/dist/css/basic.css
			filename: 'css/[name].css',
			chunkFilename: '[id].css',
		}),
		new VueLoaderPlugin(),
	],
};
