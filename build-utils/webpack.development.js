const path = require('path');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');

module.exports = () => {
	return {
		devtool: 'eval-source-map', // This option controls if and how source maps are generated.
		plugins: [new BundleAnalyzerPlugin()],
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
	};
};
