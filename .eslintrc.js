// https://eslint.org/docs/user-guide/configuring

module.exports = {
    extends: [
        'plugin:vue/recommended',
        'airbnb-base'
    ],
    'plugins': [
        'vue',
    ],
    'parser': 'vue-eslint-parser',
    'parserOptions': {
        'parser': 'babel-eslint',
    },
    // add your custom rules here
    'rules': {
        'indent': ['error', 'tab'],
        'no-tabs': ['off'],
        'brace-style': ['error', 'stroustrup'],
        'arrow-body-style': ['error', 'always'],
        // allow debugger during development
        'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
        'import/extensions': [
            'error', 'always', {
                'js': 'never',
                'vue': 'never'
            }
        ],
        'vue/html-indent': ['error', 'tab'],
    },
    'settings': {
        'import/resolver': {
            'webpack': {
                'config': 'webpack.config.js'
            }
        }
    },
    'globals': {
        'test': true,
        'expect': true,
        'describe': true,
        'window': true,
        'beforeEach': true,
        'history': true,
        'document': true,
        'jest': true,
        'it': true,
    },
}
