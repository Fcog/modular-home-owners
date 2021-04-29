import './styles.css'
import Splide from '@splidejs/splide'

document.addEventListener( 'DOMContentLoaded', () => {
    // Initiate sliders.
    if (document.querySelector('.splide')) {
        new Splide('.splide', {
            pagination: false,
            focus: 'center',
        }).mount()
    }

    function readMore() {
        const readMoreContainers = document.querySelectorAll('.js-read-more')

        readMoreContainers.forEach( readMoreContainer => {
            const readMoreButton = readMoreContainer.querySelector('.js-read-more-button')
            const readMoreText = readMoreContainer.querySelector('.js-read-more-text')
    
            readMoreButton.addEventListener('click', event => {
                readMoreText.classList.toggle('hidden')
                readMoreButton.classList.add('hidden')
            })
        })
    }


    function menuMobileDropdown( parentMenuSelector, menuItemSelector, submenuSelector, clickFunction ) {
        const parentMenus = document.querySelectorAll(parentMenuSelector)
    
        parentMenus.forEach( parentMenu => {
            const menuItem = parentMenu.querySelector(menuItemSelector)
            const submenu = parentMenu.querySelector(submenuSelector)
    
            menuItem.addEventListener('click', event => {
                event.preventDefault()
                clickFunction(menuItem, submenu)
            })
        })
    }
    
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

    readMore()
})