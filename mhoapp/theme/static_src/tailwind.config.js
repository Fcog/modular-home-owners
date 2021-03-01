module.exports = {
    purge: [
        // Templates within theme app (e.g. base.html)
        '../templates/**/*.html',
        // Templates in other apps. Uncomment the following line if it matches
        // your project structure or change it to match.
        // '../../templates/**/*.html',
    ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
            colors: {
                green: '#609c00',
                blue: '#0d476c',
                'blue-light': '#37b1ff'
            },
            container: {
              center: true,
              padding: {
                DEFAULT: '1rem',
                sm: '2rem',
                lg: '4rem',
                xl: '5rem',
                '2xl': '6rem',
              },
            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}