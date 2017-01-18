# Unbabel Front-end Starter

Starting point front-end projects at Unbabel

This repo aims to provide a simple starting point, using Gulp to run several tasks, for example compile SASS, JavaScript module approach, serve files using BrowserSync providing CSS injection and auto browser reloading.

Read the [quickstart](#quickstart) instructions.

## Tooling

- **Gulp** - Run project tasks
- **SASS** - CSS pre-processor (SCSS syntax)
- **Autoprefixer** - Parse CSS and add vendor prefixes to rules using values from Can I Use.
- **CleanCSS** - Optimize and minify CSS
- **BrowserSync** - Serve static files, inject CSS changes and auto-reload browser when files change
- **Webpack** - Transpiles ES6 code to ES5

## Folder Structure

Describe the folder structure

### Styles

    scss/
    |
    |- base/
    |   |- _all.scss
    |   |- _base.scss
    |   ...
    |
    |- partials/
    |   |- _all.scss
    |   ...
    |
	|- typography/
    |   |- _all.scss
	|   |- _typography.less
	|   ...
    |
	|- utils/
    |   |- _all.scss
    |   |- _grid.scss
	|   ...
    |
    |- views/
    |   |- _all.scss
    |   ...

**Description**

- `/base` - Global project styles. Usually affect the global feel of the project.
- `/partials` - Anything from buttons, forms, lists, cards, etc.
- `/typography` - Typography related stuff. The overall typography of the project is defined here.
- `/utils` - Useful pieces of css such grids, media query breakpoints, alignment stuff, clears, etc.
- `/views` - Page/section specific styles.
- `_dependencies.scss` - Import your external dependencies here.
- `_settings.scss` - Contains variables used across the project.
- `main.scss` - The main app file that imports everything else.

Each folder usually has a `_all.scss` file that imports all files within the folder.

## CSS

Talk about less and file naming conventions. Files starting with underscore

## JavaScript

Talk about code style, filenames and tests

### Module approach

Your project starts at `src/js/main.js`, you may write your code using ES6 modules and all is compiled using Webpack.

## Quickstart

### Requirements

- `node` (v6.8.1 or higher) - [https://nodejs.org/en/](https://nodejs.org/en/)
- `yarn` (v0.18.1 or higher) - [https://yarnpkg.com/en/docs/install](https://yarnpkg.com/en/docs/install)
- `bower` (v1.8.0 or higher) - Run `npm install -g bower` to install. [https://bower.io/](https://bower.io/)
- `gulp-cli` (v1.2.2 or higher) - Run `npm install -g gulp-cli` to install. [http://gulpjs.com/](http://gulpjs.com/)

### How to use

To start using `cd` into the project folder, run `yarn`.

Running `yarn` will install all dependencies and compile the assets once.

It's a good idea to run `yarn` when changing branches to make sure everything is updated.

You may run `yarn && gulp serve` to install all requirements and open the browser to see something working.

**While developing**

Run `gulp serve`. This will compile all assets once, launch browsersync in the browser. It then watches for css and javascript changes. When css changes, it gets injected. When JavaScript changes, the page reloads.