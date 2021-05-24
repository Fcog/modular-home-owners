export default function floatingInputLabels() {
    const moveLabelUp = event => {
        const target = event.target
        target.parentNode.classList.add('active')
    }

    const moveLabelDown = event => {
        const target = event.target
        if (!target.value) {
          target.parentNode.classList.remove('active')
        }          
    }

    const bindEvents = (input) => {
        input.addEventListener('focus', moveLabelUp)
        input.addEventListener('blur', moveLabelDown)
    }

    const init = () => {
        const inputContainers = document.querySelectorAll('.js-input')

        inputContainers.forEach( inputContainer => {
            const input = inputContainer.querySelector('.js-input input, .js-input textarea, .js-input select')
            
            if (!input) {
                return
            }

            // If input has an initial value set or it has focus, then active class.
            if (input.value || input === document.activeElement) {
                inputContainer.classList.add('active')
            }

            bindEvents(input)
        })
    }

    return {
      init: init
    }
}