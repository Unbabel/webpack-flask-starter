const path = require('path');
const webpack = require('webpack');

module.exports = {
  context: path.join(__dirname, 'src', 'js'),
  resolve: {
    modulesDirectories: ['bower_components'],
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
    loaders: [{
      test: /\.js$/,
      exclude: /(node_modules|bower_components)/,
      loader: 'babel',
      query: {
        presets: ['es2015'],
      },
    }],
  },
  plugins: [
    new webpack.ResolverPlugin(
        new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin('.bower.json', ['main']),
    ),
  ],
};
