export default function homesLayoutToggler() {
    const layoutSelector = document.querySelector('#id_layout')

    if (!layoutSelector) {
        return 
    }

    const twoColsPanel = document.querySelector('.js-two-cols-panel')
    const twoColsShorterPanel = document.querySelector('.js-two-cols-shorter-panel')
    const fullContentPanel = document.querySelector('.js-full-content-panel')

    const containers = [
        twoColsPanel,
        twoColsShorterPanel,
        fullContentPanel,
    ]

    toggleContainer()

    layoutSelector.addEventListener('change', toggleContainer)

    function toggleContainer() {
        hideAll(containers)

        if (layoutSelector.value == 'FW') {
            toggleDisplay(fullContentPanel)
        }

        if (layoutSelector.value == 'EW') {
            toggleDisplay(twoColsPanel)
        }   

        if (layoutSelector.value == 'LS') {
            toggleDisplay(twoColsShorterPanel)
        }           
    }

    function toggleDisplay(container) {
        if (container.style.display == 'block') {
            container.style.display = 'none'
        } else {
            container.style.display = 'block'
        }
    }

    function hideAll(containers) {
        containers.forEach(container => container.style.display = 'none')
    }
}