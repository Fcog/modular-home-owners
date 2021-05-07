/**
 * Toggles the filters menu.
 */
export default function filtersMenu() {
    const menu = document.getElementById('filters-menu')
    const openButton = document.getElementById('filters-open-button')
    const closeButton = document.getElementById('filters-close-button')

    if (!menu) {
        return
    }

    function openMenu() {
        menu.classList.add('opened')
        document.body.classList.add('black-overlay')
    }    

    function closeMenu() {
        menu.classList.remove('opened')
        document.body.classList.remove('black-overlay')
    }

    openButton.addEventListener('click', openMenu)
    closeButton.addEventListener('click', closeMenu)    

    document.addEventListener('click', function closeMenuOutside(event) {
        if (!menu.contains(event.target) && event.target.id !== 'filters-open-button') {
            closeMenu()
        }
    })

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            closeMenu()
        }
    })
}