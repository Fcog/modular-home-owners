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
        const format = inputRangeContainer.dataset.format        

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
    
        // Money formatting
        var moneyFormat = wNumb({
            mark: '.',
            thousand: ',',
            prefix: '$',
        })

        // Square feet formatting
        var sqftFormat = wNumb({
            thousand: ',',
            suffix: ' ft',
        })        

        // No decimals formatting for values in the URL query params.
        var noDecimalsFormat = wNumb({
            decimals: 0,
        })              

        // Widget formatting.
        const widgetFormatting = format === 'money' ? moneyFormat : sqftFormat

        /**
         * Updates on initialization the range texts values and the hidden input values with no decimals from the URL query values or the default values.
         */
        const urlParams = new URLSearchParams(window.location.search)

        const initialMinValue = urlParams.get(minInputName) ? parseInt(urlParams.get(minInputName)) : minRange
        const initialMaxValue = urlParams.get(maxInputName) ? parseInt(urlParams.get(maxInputName)) : maxRange
        
        // Min initial value.
        inputRangeMin.innerHTML = widgetFormatting.to(initialMinValue)
        inputRange.noUiSlider.set([initialMinValue, null])          

        // Sets the max initial value.
        inputRangeMax.innerHTML = widgetFormatting.to(initialMaxValue)
        inputRange.noUiSlider.set([null, initialMaxValue])

        /**
         * Event triggered when the input range buttons are moved (released).
         * 
         * Docs: https://refreshless.com/nouislider/events-callbacks/
         * 
         * @param {array} values an array with the min and max values as strings.
         * @param {int} handle is equal to 1 when the right toggle button is moving, else 0.
         */
        inputRange.noUiSlider.on('update', function (values, handle) {
            const value = parseInt(values[handle])

            if (handle) {
                // Max value changes.
                inputRangeMax.innerHTML = widgetFormatting.to(value)
                maxRangeInput.value = noDecimalsFormat.to(value)
            } else {
                // Min value changes.
                inputRangeMin.innerHTML = widgetFormatting.to(value)
                minRangeInput.value = noDecimalsFormat.to(value)
            }   
        })
    })
}
