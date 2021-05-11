import './styles.css'

import MicroModal from 'micromodal'

import inputRange from './js/input-range'
import slider from './js/slider'
import readMore from './js/read-more'
import menuMobileDropdown from './js/menu-mobile-dropdown'
import heroHomePriceRange from './js/hero-home-price-range'
import numberControl from './js/number-control'
import filtersMenu from './js/filters-menu'
import floatingInputLabels from './js/floating-input-labels'


document.addEventListener( 'DOMContentLoaded', () => {
    MicroModal.init()
    inputRange()
    slider()
    readMore()
    heroHomePriceRange()
    numberControl()
    filtersMenu()
    floatingInputLabels().init()

    document.addEventListener('htmx:afterRequest', () => {
        console.log('hola')
        floatingInputLabels().init()
    } )

    /**
     * Main menu mobile dropdown toggling.
     */
    if ( window.innerWidth < 768 ) {
        menuMobileDropdown(
            '.luxbar-menu .dropdown', 
            '.luxbar-item-a-first-level', 
            'ul', 
            (menuItem, submenu) => { 
                submenu.classList.toggle('block')
                menuItem.classList.toggle('opened')
            }
        )
    }

    /**
     * Footer menu mobile dropdown toggling.
     */    
    if ( window.innerWidth < 768 ) {
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
    }
})