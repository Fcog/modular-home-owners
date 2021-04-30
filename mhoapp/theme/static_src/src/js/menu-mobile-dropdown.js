export default function menuMobileDropdown( parentMenuSelector, menuItemSelector, submenuSelector, clickFunction ) {
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