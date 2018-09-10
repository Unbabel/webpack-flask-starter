const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const WebpackShellPlugin = require('webpack-shell-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');

const prod = process.env.NODE_ENV === 'production';

module.exports = {
	entry: {
		// all the files that you want to process or watch need to be here
		// if this list gets too long, make a separate file and import it here
		basic: './project/static/src/scss/all.scss',
		home: './project/static/src/js/home.js',
		// 'html/home': './project/templates/home.html',
	},
	output: {
		path: path.resolve(__dirname, './project/static/dist'),
		publicPath: '/static/dist/',
		filename: 'js/[name].bundle.js',
	},
	resolve: {
		alias: {
			vue$: 'vue/dist/vue.esm.js',
			'@': path.resolve(__dirname, 'project/static/src/'),
		},
		extensions: ['.js', '.vue'],
	},
	devtool: prod ? 'none' : 'source-map',
	optimization: {
		minimizer: [
			new UglifyJsPlugin({
				cache: true,
				parallel: true,
				sourceMap: !prod,
			}),
			new OptimizeCSSAssetsPlugin({}),
		],
		splitChunks: {
			chunks: 'all',
			name: 'common',
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
			// we don't actually do anything with this right now,
			// it's just so the livereload works when changing the templates
			{
				test: /\.html$/,
				use: [
					{
						loader: 'html-loader',
						options: {
							minimize: true,
						},
					},
				],
			},
			{
				test: /\.scss$/,
				oneOf: [
					// config for scss inside .vue files
					{
						resourceQuery: /^\?vue/,
						use: ['vue-style-loader', MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
					},
					// config for stand-alone .scss files
					{
						use: ['css-hot-loader', MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader', 'sass-loader'],
					},
				],
			},
			{
				test: /\.(png|svg|jpg|gif)$/,
				use: [
					{
						loader: 'url-loader',
						options: {
							name: 'img/[name].[ext]',
							limit: 10000,
						},
					},
				],
			},
		],
	},
	devServer: {
		contentBase: path.join(__dirname, './project/'),
		// url used on the templates to get the static files
		// example: /static/dist/file.css
		publicPath: '/static/dist/',

		// port where the dev server will start
		port: 8081, // Internal port
		host: '0.0.0.0', // Docker-specific, allows being accessed by host

		// Public url accessed by the host. Allows sockjs to work - localhost:7001
		public: process.env.DEVELOPMENT_HOST_PORT,

		// only logs stuff on the console when there's an error or a new compilation
		stats: 'minimal',
		proxy: {
			// all the requests that are not /static/dist/ files go to flask
			// server:8080 is the docker-network address for the flask server
			'!(/static/dist/**/**.*)': {
				target: 'http://server:8080', // Matches internal docker network
			},
		},
	},
	plugins: [
		new MiniCssExtractPlugin({
			// you can also put 'css/[name].css' to send the file to a /dist/css folder
			filename: 'css/[name].css',
			chunkFilename: 'css/[name].css',
		}),
		new WebpackShellPlugin({
			// removes the /dist/html/ folder (that is not being used) after building
			onBuildEnd: ['rm -rf project/static/dist/html && echo "Removed the /dist/html/ folder"'],
		}),
		new VueLoaderPlugin(),
	],
};
