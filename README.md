# Unbabel Front-end Starter

[![CircleCI](https://circleci.com/gh/Unbabel/frontend-starter/tree/master.svg?style=svg&circle-token=97edd512a945d1412a5a0ff0ba51de509bd837db)](https://circleci.com/gh/Unbabel/frontend-starter/tree/master)

This repo's goal is to get your front-end buildsystems up and running faster. It's based on the [Vue.js Webpack boilerplate](https://github.com/vuejs-templates/webpack) and was modified to play nice with a Flask project.

## Quick start
1. Copy everything except this README
2. Search for "coolest_app" and change it to match your project's name
3. Add your entry points on the `webpack.base.config.js` file
4. Edit the proxy table on the `config/index.js` file
5. Edit the port number to match your project's (default is 5000)

If you want to know more about each file, read the [Not-so-quick start](Not-so-quick start).

## Features:
- Compiles Vue.js single file components
- Processes .scss files
- Is ready to test the frontend using Jest
- Has a dev mode that launches a server with livereload
- Has a production mode that compresses the files
- Lints the .vue and .js files
- Adds polyfills using Babel

## Folder structure
We kept the folder structure as flexible as possible, with some quick find and replaces to fix the paths you should be able to move stuff around.
The `/coolest_app/static/` will be populated with a `dist` folder with the files ready to be served by Flask.

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
We are using Jest for all tests, with the help of the @vue/test-utils library to test Vue.js components more easily. There is an example file on the `/coolest_app/static/tests/unit/js/` folder, that is ready to test Vuex store, if you have that in your apps.

## Linting
There is really no reason why you shouldn't lint your files: it prevents bugs, makes projects inside the same organization consistent and mantains the overall sanity of the other humans who look at your code.

We use a slightly modified version of [AirBnb's congif](https://www.npmjs.com/package/eslint-config-airbnb-base), the biggest difference being the use of Tabs instead of Spaces. The livereload server that starts when you use `npm run dev` lints your files automatically and will show an annoying overlay if there are errors (and show the warnings on the console) that prevents you from seeing the page.

## Not-so-quick start
In case you're curious regarding what each file does. Assuming `/` is your project's root folder, and your Flask app is inside the `/coolest_app`:

1. Copy the package.json file to `/` and edit it to match your project
2. Copy the `.babelrc` file to `/` — these are the settings for Babel
3. Copy the `.eslintrc.js` file to `/` — these are our linter rules
4. (If you need Bower) Copy the `.bowerrc` file to `/` — this is the Bower config, that places the bower_components inside your projects' static folder
5. (If you need Bower) Copy the `bower.json` file to `/` and add your Bower dependencies
6. Add the contents of the `.gitignore` file to your `.gitignore` — we suggest not commiting the `/coolest_app/static/dist/` folder, as your deploy process should take care of the generating the final dist files, but remove that line if you need it
7. Copy the `jest.config.js` file to `/` — this is the Jest config file, which includes minimum thresholds :)
8. Copy the `/coolest_app/static/build/` folder to `/coolest_app/static/` — this is the config for building/serving
9. (Optional) Copy the `/coolest_app/static/build/merged_files.js` file to `/coolest_app/static/build/` — if you need to merge non-module files into one (or more), also check the bottom of the `webpack.base.conf.js` file if that's the case
10. Change the path on `/coolest_app/static/build/webpack.dev.conf.js:12` to match your project
11. Add your entry files on `/coolest_app/static/build/webpack.base.conf.js:17` — the property name is the filename that you'll end up with, the string is the path
12. Copy the `/coolest_app/static/config/` folder to `/coolest_app/static/`
13. Change the list of proxies on `/coolest_app/static/config/index.js` with your entries — this lets the dev server inject the styles on the page instead of using the dist css files
14. Run `npm install` — this will install the dependencies, install the bower components and build all the files for production