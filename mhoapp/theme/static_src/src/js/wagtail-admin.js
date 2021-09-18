export default function homesLayoutToggler() {
    const layoutSelector = document.querySelector('#id_layout')

    if (!layoutSelector) {
        return 
    }

    const leftColPanel = document.querySelector('.js-left-col-panel')
    const rightColPanel = document.querySelector('.js-right-col-panel')
    const fullContentPanel = document.querySelector('.js-full-content-panel')

    const containers = [
        leftColPanel,
        rightColPanel,
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
            toggleDisplay(leftColPanel)
            toggleDisplay(rightColPanel)
        }   

        if (layoutSelector.value == 'LS') {
            toggleDisplay(leftColPanel)
            toggleDisplay(rightColPanel)
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