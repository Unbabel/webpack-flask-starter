/*
 *
 * Gulp toolset for Unbabel
 *
 */


// Common dependencies
const gulp = require('gulp');
const debug = require('gulp-debug');
const path = require('path');
const pump = require('pump');
const options = require('gulp-options');
const fs = require('fs');
const util = require('gulp-util');
const browserSync = require('browser-sync').create();

// Aliases
const empty = util.noop;


/*
 * Target Mode
 *
 * Development or Production
 *
 * development || prod
 * --freshstart means that files are compiled regardless if they have or not changed
 */

const defaultTarget = 'development';
const targetMode = options.has('target') && ['development', 'production'].indexOf(options.get('target')) !== -1 ? options.get('target') : defaultTarget;
const targetIsDevelopment = targetMode === 'development';
const targetIsProd = targetMode === 'production';

const freshStart = (targetIsProd || options.has('freshstart'));


/*
 * Global vars
 */

const rootDir = '.';
const srcDir = rootDir + '/src';
const distDir = rootDir + '/dist';
const templatesDir = rootDir;


/*
 * Paths
 */

const scssPathForWatch = [
  '/scss/**/*.scss',
].map(file => `${srcDir}${file}`);

const stylesPathForWatch = [].concat(scssPathForWatch);

const templatesPathForWatch = [
  '/**/*.html',
].map(file => `${templatesDir}${file}`);


/*
 * Style processing
 */

const sass = require('gulp-sass');

const styleSourcePath = [
  '/scss/**/!(_*).scss',
].map(file => `${srcDir}${file}`);

const styleLookupPaths = [
  path.join(__dirname, 'scss'),
  path.join(__dirname, 'bower_components'),
];

const stylePipeOptions = {
  paths: styleLookupPaths,
};

const styleSourceDir = `${srcDir}/scss`;
const styleDestination = `${distDir}/css`;

// clean-css options https://github.com/jakubpawlowicz/clean-css
const cleanCSSOptions = {
  debug: true,
  compatibility: 'ie8',
  processImport: true,
  processImportFrom: ['local'],
};

const cleanCSSCallback = (details) => {
  console.log(
    'CleanCSS took %s seconds to save %s% from %s',
    (details.stats.timeSpent / 1000),
    Math.round(details.stats.efficiency * 100),
    details.name);
};

// Post processing
const sourcemaps = require('gulp-sourcemaps');
const autoprefixer = require('gulp-autoprefixer');
const cleanCSS = require('gulp-clean-css');

gulp.task('compile-css', (cb) => {
  pump([
    gulp.src(styleSourcePath),

    // Init sourcemaps
    sourcemaps.init(),

    // Know which files are flowing down the pipe
    debug(),

    // Compile less files using specified options
    sass(stylePipeOptions),

    // Run autoprefixer
    autoprefixer(),

    // Cleanup css result
    targetIsProd ? cleanCSS(cleanCSSOptions, cleanCSSCallback) : empty(),

    // Write the sourcemaps
    sourcemaps.write('.'),

    // Save files
    gulp.dest(styleDestination),

    // Stream changed files to browsersync
    browserSync.stream({
      match: '**/*.css',
    }),
  ], cb);
});

gulp.task('watch-css', ['compile-css'], () => {
  gulp.watch(stylesPathForWatch, ['compile-css']);
});


/*
 * Webpack
 */

const webpack = require('webpack');

const webpackConfig = require('./webpack.config.js');

const webpackConfigExists = Object.keys(webpackConfig.entry).length > 0;

if (webpackConfigExists) {
  if (targetIsProd) {
    const webpackUglifyJsPlugin = new webpack.optimize.UglifyJsPlugin({
      compress: {
        screw_ie8: true,
        warnings: false,
      },
    });
    webpackConfig.plugins.push(webpackUglifyJsPlugin);
  }

  // This sets node_env to production or development
  // It is relevant for vue compilation
  webpackConfig.plugins.push(new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify(targetMode),
    },
  }));

  // Webpack
  gulp.task('build-webpack', (cb) => {
    webpack(webpackConfig, (err, stats) => {
      if (err) throw new util.PluginError('webpack', err);
      stats.toString({
        colors: true,
        chunks: false,
      }).split('\n').map(line => util.log(util.colors.blue('[webpack]'), line));
      cb();
    });
  });

  gulp.task('watch-webpack', ['build-webpack'], (done) => {
    browserSync.reload();
    done();
  });
}


/*
 * BrowserSync
 */

const browserSyncOptions = {
  server: {
    baseDir: `${rootDir}`,
  },
};

// Serve the project using browserSync
gulp.task('serve', ['default'], () => {
  // Start browserSync
  browserSync.init(browserSyncOptions);

  // Watch less for changes
  gulp.watch(stylesPathForWatch, ['compile-css']);

  // Watch webpack for changes
  if (webpackConfigExists) {
    gulp.watch(`${webpackConfig.context}/**/*.js`, ['watch-webpack']);
  } else {
    gulp.watch(`${webpackConfig.context}/**/*.js`).on('change', browserSync.reload);
  }

  // Watch files for changes
  gulp.watch(templatesPathForWatch).on('change', browserSync.reload);
});


/*
 * Gulp Default
 */

const defaultTasks = ['compile-css'];

if (webpackConfigExists) {
  defaultTasks.push('build-webpack');
}

gulp.task('default', defaultTasks);
