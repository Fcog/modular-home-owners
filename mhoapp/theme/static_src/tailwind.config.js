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
                dark: '#09293C',
                green: '#1A5E88',
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
                '7.5': '1.875rem', // 30px
            },
            fontSize: {
                '1.5xl': '1.31rem',
                '5.5xl': '3.438rem',
            },
            height: {
                15: '3.75rem',
            },
            maxWidth: {
                '15': '15rem',
            },
            backgroundSize: {
               '80%': '80%',
            },
            zIndex: {
                '-10': '-10',
            }
        },
    },
    variants: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
    ],
}