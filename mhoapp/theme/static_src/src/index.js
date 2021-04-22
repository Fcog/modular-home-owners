import './styles.css'

document.addEventListener( 'DOMContentLoaded', () => {
    const parentMenus = document.querySelectorAll('.luxbar-menu .dropdown')
    
    parentMenus.forEach( parentMenu => {
        const menuItem = parentMenu.querySelector('.luxbar-item-a-first-level')
        const submenu = parentMenu.querySelector('ul')

        menuItem.addEventListener('click', event => {
            event.preventDefault()
            submenu.classList.toggle('block')
            menuItem.classList.toggle('opened')
        })
    })
})