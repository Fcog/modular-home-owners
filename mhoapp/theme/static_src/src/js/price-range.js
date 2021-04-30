import noUiSlider from 'nouislider'
import wNumb from 'wNumb'

/**
 * Initiate input range widgets.
 * 
 * Docs: https://refreshless.com/nouislider
 */
export default function inputRange() {
    const inputRangeContainers = document.querySelectorAll('.js-uislider')

    inputRangeContainers.forEach( inputRangeContainer => {
        // uislider widget init element.
        const inputRange = inputRangeContainer.querySelector('.js-uislider-widget')
        // Range texts
        const inputRangeMin = inputRangeContainer.querySelector('.js-uislider-min-value')
        const inputRangeMax = inputRangeContainer.querySelector('.js-uislider-max-value')
        // URL query hidden inputs
        const minRangeInput = inputRangeContainer.querySelector('.js-uislider-min-range-input')
        const maxRangeInput = inputRangeContainer.querySelector('.js-uislider-max-range-input')
        // Widget data configs.
        const minRange = parseInt(inputRangeContainer.dataset.minRange)
        const maxRange = parseInt(inputRangeContainer.dataset.maxRange) 
        const step = parseInt(inputRangeContainer.dataset.step)        
        const minInputName = inputRangeContainer.dataset.minInputName
        const maxInputName = inputRangeContainer.dataset.maxInputName        

        // UISlider init.
        noUiSlider.create(inputRange, {
            start: [minRange, maxRange],
            step: step,
            connect: true,
            behaviour: 'drag',
            range: {
                'min': minRange,
                'max': maxRange,
            }
        })
    
        // Text range values formatting
        var moneyFormat = wNumb({
            mark: '.',
            thousand: ',',
            prefix: '$',
        })

        // Query URL values formatting.    
        var noDecimalsFormat = wNumb({
            decimals: 0,
        })              

        /**
         * Updates the money texts values and the hidden input values with no decimals from the URL query values.
         */
        const urlParams = new URLSearchParams(window.location.search)

        const maxValueFromURL = parseInt(urlParams.get(maxInputName))
        const minValueFromURL = parseInt(urlParams.get(minInputName))       

        // Max initial value.
        if (maxValueFromURL) {
            inputRangeMax.innerHTML = moneyFormat.to(maxValueFromURL)
            inputRange.noUiSlider.set([null, maxValueFromURL])
        }

        // Min initial value.
        if (minValueFromURL) {
            inputRangeMin.innerHTML = moneyFormat.to(minValueFromURL)
            inputRange.noUiSlider.set([minValueFromURL, null])
        }                 

        /**
         * Event when the input range buttons are moved.
         * Updates the money texts values and the hidden input values with no decimals.
         * 
         * Docs: https://refreshless.com/nouislider/events-callbacks/
         * 
         * @param {array} values an array with the min and max values as strings.
         * @param {int} handle is equal to 1 when the right toggle button is moving, else 0.
         */
        inputRange.noUiSlider.on('update', function (values, handle) {
            const maxValue = parseInt(values[handle])
            const minValue = parseInt(values[handle])

            if (handle) {
                // Max value changes.
                inputRangeMax.innerHTML = moneyFormat.to(maxValue)
                maxRangeInput.value = noDecimalsFormat.to(maxValue)
            } else {
                // Min value changes.
                inputRangeMin.innerHTML = moneyFormat.to(minValue)
                minRangeInput.value = noDecimalsFormat.to(minValue)
            }       
        })
    })
}
