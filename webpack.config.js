const path = require('path');
const webpackMerge = require('webpack-merge');

const modeConfig = env => require(`./build-utils/webpack.${env}.js`)(env);

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const WebpackShellPlugin = require('webpack-shell-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = ({ mode } = { mode: 'production' }) => {
	return webpackMerge(
		{
			mode,
			entry: {
				// all the files that you want to process or watch need to be here
				// if this list gets too long, make a separate file and import it here
				basic: './project/static/src/scss/all.scss',
				home: './project/static/src/js/home.js',
			},
			output: {
				path: path.resolve(__dirname, './project/static/dist'),
				publicPath: '/static/dist/',
				filename: 'js/[name].bundle.js',
			},
			resolve: {
				alias: {
					vue$: 'vue/dist/vue.esm.js',
					vuex$: 'vuex/dist/vuex.esm.js',
					'@': path.resolve(__dirname, 'project/static/src/'),
				},
				extensions: ['.js', '.vue'],
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
								use: [
									MiniCssExtractPlugin.loader,
									'css-loader',
									{
										loader: 'postcss-loader',
										options: {
											plugins: () => [
												require('autoprefixer'),
											],
										},
									},
									{
										loader: 'sass-loader',
										options: {
											includePaths: ['node_modules'],
										},
									},
								],
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
		},
		modeConfig(mode),
	);
};
