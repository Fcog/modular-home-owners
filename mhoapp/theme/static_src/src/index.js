import './styles.css'

import inputRange from './js/price-range'
import slider from './js/slider'
import readMore from './js/read-more'
import menuMobileDropdown from './js/menu-mobile-dropdown'
import heroHomePriceRange from './js/hero-home-price-range'
import numberControl from './js/number-control'


document.addEventListener( 'DOMContentLoaded', () => {
    inputRange()
    slider()
    readMore()
    heroHomePriceRange()
    numberControl()

    /**
     * Main menu mobile dropdown toggling.
     */
    menuMobileDropdown(
        '.luxbar-menu .dropdown', 
        '.luxbar-item-a-first-level', 
        'ul', 
        (menuItem, submenu) => { 
            submenu.classList.toggle('block')
            menuItem.classList.toggle('opened')
        }
    )

    /**
     * Footer menu mobile dropdown toggling.
     */    
    menuMobileDropdown(
        '.js-menu-vertical', 
        '.js-menu-vertical-parent-menu', 
        '.js-menu-vertical-submenu',
        (menuItem, submenu) => { 
            submenu.classList.toggle('hidden')
            menuItem.classList.toggle('opened')
            menuItem.classList.toggle('icon-rotate')
        }
    )
})