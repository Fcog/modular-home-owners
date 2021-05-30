import { createPopper } from '@popperjs/core'

/**
 * Tooltip.
 * https://popper.js.org/
 */
export default function tooltip() {
    document.querySelectorAll('.js-tooltip').forEach( tooltipContainer => { 
        const box = tooltipContainer.querySelector('.js-tooltip-box')
        const trigger = tooltipContainer.querySelector('.js-tooltip-trigger')
    
        const popperInstance = createPopper(trigger, box, {
            placement: 'top',
            modifiers: [
                {
                    name: 'offset',
                    options: {
                        offset: [0, 8],
                    },
                },
            ],
        })

        function show() {
            box.setAttribute('data-show', '')
          
            // We need to tell Popper to update the tooltip position
            // after we show the tooltip, otherwise it will be incorrect
            popperInstance.update()
        }
          
        function hide() {
            box.removeAttribute('data-show')
        }
          
        const showEvents = ['mouseenter', 'focus']
        const hideEvents = ['mouseleave', 'blur']
          
        showEvents.forEach(event => {
            trigger.addEventListener(event, show)
        })
          
        hideEvents.forEach(event => {
            trigger.addEventListener(event, hide)
        })        
    })
}
