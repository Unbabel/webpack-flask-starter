module.exports = {
	verbose: false,
	rootDir: './coolest_app/static',
	moduleFileExtensions: ['vue', 'js', 'jsx'],
	moduleNameMapper: {
		'^@/(.*)$': '<rootDir>src/$1',
	},
	roots: [
		'<rootDir>/src',
		'<rootDir>/src/tests',
	],
	transform: {
		'^.+\\.jsx?$': 'babel-jest',
		'^.*\\.(vue)$': 'vue-jest',
	},
	transformIgnorePatterns: [
		// this lets us test vue components that import things
		// from the node_modules
		'node_modules/(?!@unbabel/ui)',
	],
	coverageDirectory: '../../coverage',
	collectCoverageFrom: [
		'**/*.{js,jsx,vue}',
		'!**/tests/**',
	],
	coveragePathIgnorePatterns: [
		// files that should be ignored in the test coverage
		'<rootDir>/src/tests/',
	],
	testPathIgnorePatterns: [
		'/node_modules/',
	],
	setupFiles: [
		'<rootDir>/src/tests/setup-mocks.js',
	],
	coverageThreshold: {
		global: {
			lines: 80,
			branches: 50,
			functions: 85,
			statements: 80,
		},
	},
};
