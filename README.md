# Unbabel Front-end Starter

[![CircleCI](https://circleci.com/gh/Unbabel/frontend-starter/tree/master.svg?style=svg&circle-token=97edd512a945d1412a5a0ff0ba51de509bd837db)](https://circleci.com/gh/Unbabel/frontend-starter/tree/master)

The starting point for front-end projects at Unbabel

This repo's goal is to get your front-end buildsystems up and running faster. It's based on the [Vue.js Webpack boilerplate](https://github.com/vuejs-templates/webpack) and was modified to play nice with a Flask project.

## Quick start
1. copy everything except this README
2. search for "coolest_app" and change that to match your project
3. add your entry points on the webpack.base.config.js file
4. edit the proxy table on the config/index.js file
5. edit the port number to match your project's (default is 5000)

If you want to know more about each file, read the [#Not-so-quick start](Not-so-quick start).

## Features:
- compiles Vue.js single file components
- processes .scss files
- is ready to test the frontend using Jest
- has a dev mode that launches a server with livereload
- has a production mode that compresses the files
- lints the .vue and .js files
- adds polyfills using Babel

## Folder structure
We kept the folder structure as flexible as possible, with some quick find and replaces to fix the paths you should be able to move stuff around.
The `/coolest_app/static/` which emulates your project's static folder will be populated with a `dist` folder with the files ready to be served by Flask.

### Vue
The `/coolest_app/static/vue/` folder has 2 folders:
- `/apps/` — for _big-ish_ applications, that are used in one place
- `/components/` — for vue components that are used in multiple places, the LoadingSpinner is a good example, as it might be used in a UserSettings.vue app _and_ in a UserSignup.vue app

This separation might seem overkill, and it might be, depending on the size of your project, but you can always scale it down. This is the structure used on the Core.

#### Importing stuff on your .vue components
You might need to import components from a UI Library, to do that you should add it to the `package.json`:
```
"@unbabel/ui": "git+ssh://git@gitlab.com/Unbabel/ui.git",
```

And then import it on your Vue component using:
```
import { Modal, Button } from '@unbabel/ui';
```
for javascript, or for the styles:
```
@import '~@unbabel/ui/src/colors';
```

### Sass
Inside the `/coolest_app/static/src/scss/` folder is a possible structure that scales nicely. Put the elements/components that you use frequently inside the `/components/`, add the base styles to the `/base/` folder and the page-specific styles to the `/views/`.
For very small projects you can just compile the `/coolest_app/static/src/scss/all.scss` file and use that on all pages, but as soon as you get some complexity (for example if you have a user facing views and admin views), you probably should separate that, or compile each view .scss file.


### Linking to the assets
You can use
```
<script type="text/javascript" src="{{ url_for('static', filename='dist/app.js') }}"></script>
```
to link to the dist files.

Don't forget the `manifest.js`!
```
<script type="text/javascript" src="{{ url_for('static', filename='dist/js/manifest.bundle.js') }}"></script>
```

## Testing
We are using Jest for all tests, with the help of the @vue/test-utils library to test Vue.js components more easily.

## Not-so-quick start
In case you're curious regarding what each file does. Assuming `/` is your project's root folder, and your Flask app is inside the `/coolest_app`:

1. Copy the package.json file to `/` and edit it to match your project
2. Copy the `.babelrc` file to `/` — these are the settings for Babel
3. Copy the `.eslintrc.js` file to `/` — these are our linter rules, based off AirBnB's rules, with some modifications to make it more readable, the biggest change is the use of Tabs instead of Spaces
4. (If you need Bower) Copy the `.bowerrc` file to `/` — this is the Bower config, that places the bower_components inside your projects' static folder
5. (If you need Bower) Copy the `bower.json` file to `/` and add your Bower dependencies
6. Add the contents of the `.gitignore` file to your `.gitignore` — we suggest not commiting the `/coolest_app/static/dist/` folder, as your deploy process should take care of the generating the final dist files, but remove that line if you need it
7. Copy the `jest.config.js` file to `/` — this is the Jest config file, which includes minimum thresholds :)
8. Copy the `/coolest_app/static/build/` folder to `/coolest_app/static/` — this is the config for building/serving
9. Change the path on `/coolest_app/static/build/webpack.dev.conf.js:12` to match your project
10. Add your entry files on `/coolest_app/static/build/webpack.base.conf.js:17` — the property name is the filename that you'll end up with, the string is the path
11. Copy the `/coolest_app/static/config/` folder to `/coolest_app/static/`
12. Change the list of proxies on `/coolest_app/static/config/index.js` with your entries — this lets the dev server inject the styles on the page instead of using the dist css files
13. Run `npm install` — this will install the dependencies, install the bower components and build all the files for production






### Module approach

Your project starts at `src/js/main.js`, you may write your code using ES6 modules and all is compiled using Webpack.

### Unit Testing

We use [`jasmine`](https://jasmine.github.io/2.0/introduction.html) to create unit tests.

Create a file inside `spec/` named `[something].spec.js`, do your imports, write your validations and it's done.

Execute `npm test` to run all tests.

## Quickstart

### Requirements

- `npm` (included with node. v6.8.1 or higher) - [https://nodejs.org/en/](https://nodejs.org/en/)
- `gulp-cli` (v1.2.2 or higher) - Run `npm install -g gulp-cli` to install. [http://gulpjs.com/](http://gulpjs.com/)

### How to use

To start using `cd` into the project folder, run `npm install`.

Running `npm install` will install all dependencies and compile the assets once.

It's a good idea to run `npm install` when changing branches to make sure everything is updated.

You may run `npm install && gulp serve` to install all requirements and open the browser to see something working.

**While developing**

Run `gulp serve`. This will compile all assets once, launch browsersync in the browser. It then watches for css and javascript changes. When css changes, it gets injected. When JavaScript changes, the page reloads.

## Generating production-ready assets

Run `gulp --target=prod` to generate minified assets ready to production

## Managing Front-end Dependencies using Bower

`bower` is recommended to manage front-end dependencies. `bower` allows you to specify the directory where the dependencies will be installed. **This is important when working with a `flask` server, which stores all public assets inside `static`.**

**Bower is bundled as a devDependency.** You can run it with the following command.

	// Install something and saving to dependencies list
	$ npm run bower -- install -S normalize-css

	/*
	Npm is running local bower for us without the need for a global install
	Anything added after the first -- is sent directly to bower binary
	Under the hood, npm is running the following: bower install -S normalize-css
	*/

Optionally you can install `bower` globally.

**Example of how to install and include `normalize-css`**

Run `npm run bower -- install -S normalize-css` to install [normalize-css](https://necolas.github.io/normalize.css/)

Then add `@import 'bower_components/normalize-css/normalize';` to `src/scss/_dependencies.scss`

## Adding Bootstrap

**Bootstrap 4.0.0-alpha.6 is included by default.**

Explanation on how to add **just for reference**

Run `npm run bower -- install -S bootstrap@4.0.0-alpha.6`

Add `@import 'bower_components/bootstrap/scss/bootstrap';` to `src/scss/_dependencies.scss`

All bootstrap css elements are now available

## Integrate with Flask Template Project

[flask-template-project by andreffs18](https://github.com/andreffs18/flask-template-project)

You need to change the following:

1. Move `src` dir to `project/static/`
2. Edit `gulpfile.js`, search for `rootDir` and change to `./project/static`
3. Edit `webpack.config.js`, search for `node_modules` and change to `../../node_modules`
4. Edit `.bowerrc`, search for `directory` and change to `./project/static/bower_components`

**You also need to change BrowserSync options**

In `gulpfile.js`, look for:

	const browserSyncOptions = {
	  server: {
	    baseDir: `${rootDir}/`,
	  },
	};

And replace with

	const browserSyncOptions = {
	  proxy: 'localhost:5000'
	};