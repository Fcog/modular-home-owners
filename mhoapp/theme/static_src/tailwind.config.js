module.exports = {
    purge: [
        // Templates within theme app (e.g. base.html)
        '../templates/**/*.html',
        '../templates/**/**/*.html',
        '../templates/**/**/**/*.html',
        // Templates in other apps. Uncomment the following line if it matches
        // your project structure or change it to match.
        // '../../templates/**/*.html',
    ],
    important: true,
    darkMode: false, // or 'media' or 'class'
    theme: {
        colors: {
            transparent: 'transparent',
            current: 'currentColor',
            white: '#ffffff',
            green: '#609c00',
            blue: {
                DEFAULT: '#003E64',
                light: '#36B2FF',
            },
        },
        extend: {
            screens: {
                '2xl': '1640px'
            },
            container: {
              center: true,
              padding: {
                DEFAULT: '1rem',
                sm: '2rem',
                lg: '0',
                xl: '0',
                '2xl': '0',
              },
            },
            spacing: {
                mob: '1rem',
                dsk: '2rem',
            },
            height: {
                15: '3.75rem',
            }
        },
        maxWidth: {
            '15': '15rem',
        }
    },
    variants: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
    ],
}