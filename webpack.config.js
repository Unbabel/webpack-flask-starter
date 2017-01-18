const path = require('path');

module.exports = {
  context: path.join(__dirname, 'src', 'js'),
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
    loaders: [{
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      loader: 'babel',
      query: {
        presets: ['es2015'],
      },
    }],
  },
  plugins: [],
};
