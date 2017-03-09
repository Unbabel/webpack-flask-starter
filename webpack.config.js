const path = require('path');

module.exports = {
  context: path.join(__dirname, 'src', 'js'),
  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js',
      jquery$: 'jquery/dist/jquery.js',
    },
    modules: [
      'node_modules',
      'bower_components',
    ],
  },
  entry: {
    main: './main.js',
  },
  devtool: 'source-map',
  output: {
    path: path.join(__dirname, 'dist/js'),
    filename: '[name].js',
    sourceMapFilename: '[name].js.map',
  },
  module: {
    rules: [{
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      loader: 'babel-loader',
      options: {
        presets: ['es2015'],
      },
    }],
  },
  plugins: [],
};
