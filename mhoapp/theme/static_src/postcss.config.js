module.exports = {
  plugins: [
    require('postcss-import'),
    require('tailwindcss'),
    require('postcss-simple-vars'),
    require('postcss-mixins'),
    require('postcss-nested'),
    require('autoprefixer')
  ]
};