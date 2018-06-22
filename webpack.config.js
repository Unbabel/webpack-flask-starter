const path = require('path');
// const HtmlWebPackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
	entry: {
		// all the files that you want to process or watch need to be here
		// if this list gets too long, make a separate file and import it here
		'css/basic': './project/static/src/scss/all.scss',
		'js/home': './project/static/src/js/home.js',
		'html/home': './project/templates/home.html',
	},
	output: {
		path: path.resolve(__dirname, './project/static/dist'),
	},
	resolve: {
		alias: {
			vue$: 'vue/dist/vue.esm.js',
			'@': path.resolve(__dirname, 'project/static/src/'),
		},
		extensions: ['.js', '.vue'],
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
			// we don't actually do anything with this right now,
			// it's just so the livereload works when changing the templates
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
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [
					{
						loader: 'file-loader',
					},
				],
			},
		],
	},
	devServer: {
		// path to the static (or its parent folder, if you want to watch the templates also)
		// folder in relation to this file
		contentBase: path.join(__dirname, './project/'),
		// url to the folder used on the templates to get the static files
		// example: /static/dist/file.css
		publicPath: '/static/dist/',
		watchContentBase: true,
		// port where the dev server will start
		port: 9001,
		// only logs stuff on the console when there's an error or a new compilation
		stats: 'minimal',
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
			// you can also put 'css/[name].css' to send the file to a /dist/css folder
			filename: '[name].css',
			chunkFilename: '[id].css',
		}),
		new VueLoaderPlugin(),
	],
};
