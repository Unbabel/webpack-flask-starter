// https://eslint.org/docs/user-guide/configuring

module.exports = {
    extends: [
        'plugin:vue/recommended',
        'airbnb-base'
    ],
    plugins: [
        'jest',
    ],
    'parser': 'vue-eslint-parser',
    'parserOptions': {
        'parser': 'babel-eslint',
    },
    'rules': {
        'indent': ['error', 'tab'],
        'no-tabs': ['off'],
        'brace-style': ['error', '1tbs'],
        'arrow-body-style': ['error', 'always'],
        'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
        'import/extensions': [
            'error', 'always', {
                'js': 'never',
            }
        ],
        'vue/html-indent': ['error', 'tab'],
        'vue/html-closing-bracket-newline': 'off',
        'vue/max-attributes-per-line': 'off',
        'vue/html-self-closing': 'off',
    },
    'settings': {
        'import/resolver': {
            'webpack': {
                'config': 'webpack.config.js'
            }
        }
    },
    'env': {
        'es6': true,
        'browser': true,
        'jest/globals': true,
    },
}
