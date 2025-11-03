module.exports = {
  env: {
    browser: false,
    es2021: true,
    node: true,
    jest: true
  },
  extends: ['airbnb-base'],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module'
  },
  rules: {
    'no-console': 0,      // allow console.log
    'no-unused-vars': 0   // allow unused vars during practice
  }
};

