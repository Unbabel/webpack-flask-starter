/* eslint import/no-extraneous-dependencies: ["error", {"devDependencies": true}] */
/*
 * Run jasmine with ES6 modules
 */
import Jasmine from 'jasmine';

const jasmine = new Jasmine();
jasmine.loadConfigFile('spec/support/jasmine.json');
jasmine.execute();
