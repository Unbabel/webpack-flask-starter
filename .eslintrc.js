// https://eslint.org/docs/user-guide/configuring

module.exports = {
    root: true,
    parser: 'babel-eslint',
    parserOptions: {
        sourceType: 'module'
    },
    env: {
        browser: true,
    },
    extends: 'airbnb-base',
    // required to lint *.vue files
    plugins: [
        'html'
    ],
    // check if imports actually resolve
    'settings': {
        'import/resolver': {
            'webpack': {
                'config': 'project/static/build/webpack.base.conf.js'
            }
        }
    },
    // add your custom rules here
    'rules': {
        // don't require .vue extension when importing
        'import/extensions': ['error', 'always', {
            'js': 'never',
            'vue': 'never'
        }],
        "indent": ["error", 'tab'],
        "no-tabs": ["off"],
        "brace-style": ["error", "stroustrup"],
        "arrow-body-style": ["error", "always"],
        // allow optionalDependencies
        'import/no-extraneous-dependencies': ['error', {
            'optionalDependencies': ['test/unit/index.js']
        }],
        // allow debugger during development
        'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0
    },
    'globals': {
        'test': true,
        'expect': true,
        'describe': true
    }
}
