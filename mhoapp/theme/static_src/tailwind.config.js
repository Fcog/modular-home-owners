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
            gray: {
                '50': '#f8f8f8',
            },
            blue: {
                DEFAULT: '#003E64',
                light: '#36B2FF',
                light2: '#8ED4FF',
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
                DEFAULT: '2rem',
                sm: '2rem',
                lg: '2rem',
                xl: '2rem',
                '2xl': '0',
              },
            },
            spacing: {
                mob: '1rem',
                dsk: '2rem',
                '4.5': '1.15rem', // 16px
                '7.5': '1.875rem', // 30px
            },
            fontSize: {
                '1.5xl': '1.31rem',
                '5.5xl': '3.438rem',
            },
            height: {
                15: '3.75rem',
            },
            width: {
                '94%': '94%',
                '31%': '31%',
                '29%': '29%',
                '64.5%': '64.5%',
            },
            maxWidth: {
                '15': '15rem',
            },
            backgroundSize: {
               '50%': '50%',
               '70%': '70%',
            },
            backgroundPosition: {
                'right-40%': 'right 40%',
            },
            zIndex: {
                '-10': '-10',
            },
            boxShadow: {
                'custom-1': '0px 5px 20px #00000012'
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