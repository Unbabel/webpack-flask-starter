
'use strict'
// Template version: 1.1.3
// see http://vuejs-templates.github.io/webpack for documentation.

const path = require('path')

console.log(path.resolve(__dirname, '../dist/index.html'));

module.exports = {
  build: {
    env: require('./prod.env'),
    index: path.resolve(__dirname, '../dist/index.html'),
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: '',
    assetsPublicPath: '/static/dist/',
    productionSourceMap: true,
    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],
    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report
  },
  dev: {
    env: require('./dev.env'),
    port: 8080,
    autoOpenBrowser: false,
    assetsSubDirectory: '',
    assetsPublicPath: '/static/dist/',
    proxyTable: {
      '/static/dist/js/manifest.bundle.js': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true
      },
      '/static/dist/css/app.css': {
        target: 'http://127.0.0.1:5000/static/dist/css/empty.css',
        ignorePath: true,
        changeOrigin: true
      },
      '!(/static/dist/*.hot-update.json|/static/dist/js/(sample_javascript|interface).bundle.js|/static/dist/*.hot-update.js|/__webpack_hmr)': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true
      },
    },
    // CSS Sourcemaps off by default because relative paths are "buggy"
    // with this option, according to the CSS-Loader README
    // (https://github.com/webpack/css-loader#sourcemaps)
    // In our experience, they generally work as expected,
    // just be aware of this issue when enabling this option.
    cssSourceMap: false
  }
}
