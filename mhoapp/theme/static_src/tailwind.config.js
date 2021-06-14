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
            green: {
                DEFAULT: '#609c00',
                medium: '#5F9B00',
                light: '#98FB98',
                light2: '#7AB41E',
            },
            gray: {
                '20': '#F5F5F5',
                '30': '#B2B2B2',
                '40': '#CCCCCC',
                '50': '#f8f8f8',
                '60': '#E5E5E5',
                '70': '#888888',
                '80': '#D3D3D3',
                '90': '#696969',
            },
            blue: {
                DEFAULT: '#003E64',
                light: '#36B2FF',
                light2: '#8ED4FF',
                light3: '#EBF8FF',
                light4: '#E2F4FF',
                dark: '#09293C',
                green: '#1A5E88',
            },
            black: {
                DEFAULT: '#000000',
                'light': '#707070',
                'medium': '#231F20',
                'medium2': '#1A1A1A',
            }
        },
        extend: {
            screens: {
                '2xl': '1640px',
                'max-740px': {'raw': 'screen and (max-height: 740px)'},
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
                'xxxs': '.6rem',
                'xxs': '.7rem',
                '1.5xl': [ '1.31rem' , {
                    lineHeight: '1.9rem',
                }],
                '4.5xl': [ '2.5rem' , {
                    lineHeight: '3.15rem',
                }],                
                '5.5xl': '3.438rem',
            },
            lineHeight: {
                '4.5': '4.5rem',
            },
            outline: {
                'blue-green': '1px solid #1A5E88',
            },
            height: {
                15: '3.75rem',
                '283px': '283px',
                '339px': '339px',
            },
            width: {
                '94%': '94%',
                '87%': '87%',
                '73.5%': '73.5%',
                '64.5%': '64.5%',
                '55%': '55%',
                '48%': '48%',
                '45%': '45%',
                '43%': '43%',
                '37%': '37%',
                '32%': '32%',
                '31%': '31%',
                '31.7%': '31.7%',
                '26.5%': '26.5%',
                '29%': '29%',
            },
            maxWidth: {
                '380px': '380px',
                '455px': '455px',
                '15': '15rem',
                '16.25': '16.25rem',
                '21.25': '21.25rem',
            },
            backgroundSize: {
               '50%': '50%',
               '70%': '70%',
               '125%': '125%',
            },
            backgroundPosition: {
                'right-40%': 'right 40%',
            },
            zIndex: {
                '-10': '-10',
            },
            boxShadow: {
                'custom-1': '0px 5px 20px #00000012',
            },
            typography: {
                DEFAULT: {
                    css: {
                        a: {
                            color: '#609c00',
                        },
                    },
                },
                'lg': {
                    css: {
                        p: {
                            marginBottom: '2em',
                        }
                    }
                }
            },
            columnGap: {
                lg: '2rem',
            },
        }
    },
    variants: {
        extend: {
            display: ['hover', 'group-hover'],
            borderWidth: ['hover'],
            cursor: ['hover'],
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('tailwindcss-multi-column')(),
    ],
}