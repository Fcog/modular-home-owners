/**
 * Increase or decrease with buttons a number inside a number input.
 */
export default function numberControl() {
    const numberControlContainers = document.querySelectorAll('.js-number-control')

    numberControlContainers.forEach( numberControlContainer => {    
        const decreaseButton = numberControlContainer.querySelector('.js-number-control-decrease')
        const increaseButton = numberControlContainer.querySelector('.js-number-control-increase')
        const numberInput = numberControlContainer.querySelector('.js-number-control-input')

        decreaseButton.addEventListener('click', () => {
            let number = parseInt(numberInput.value) - 1

            if (number < 0) {
                return
            }

            numberInput.value = number--
        })

        increaseButton.addEventListener('click', () => {
            numberInput.value = parseInt(numberInput.value) + 1
        })    
    })
}