export default function floatingInputLabels() {
    const handleFocus = event => {
        const target = event.target
        target.parentNode.classList.add('active')
    }

    const handleBlur = event => {
        const target = event.target
        if (!target.value) {
          target.parentNode.classList.remove('active')
        }          
    }

    const bindEvents = (input) => {
        input.addEventListener('focus', handleFocus)
        input.addEventListener('blur', handleBlur)
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