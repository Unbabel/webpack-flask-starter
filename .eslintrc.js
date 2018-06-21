// https://eslint.org/docs/user-guide/configuring

module.exports = {
    extends: 'airbnb-base',
    // add your custom rules here
    'rules': {
        "indent": ["error", 'tab'],
        "no-tabs": ["off"],
        "brace-style": ["error", "stroustrup"],
        "arrow-body-style": ["error", "always"],
        // allow debugger during development
        'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
        'import/extensions': [
            'error', 'always', {
                'js': 'never',
                'vue': 'never'
            }
        ]
    },
    'globals': {
        'test': true,
        'expect': true,
        'describe': true,
        'window': true,
        'beforeEach': true,
    }
}
