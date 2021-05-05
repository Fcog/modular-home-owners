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
        const initialMinRange = parseInt(inputRangeContainer.dataset.initialMinRange)
        const initialMaxRange = parseInt(inputRangeContainer.dataset.initialMaxRange)         
        const step = parseInt(inputRangeContainer.dataset.step)        
        const minInputName = inputRangeContainer.dataset.minInputName
        const maxInputName = inputRangeContainer.dataset.maxInputName        
        const format = inputRangeContainer.dataset.format      

        // Get URL query params.
        const urlParams = new URLSearchParams(window.location.search)

        /* 
         * Logic to set the initial min range value:
         *
         * 1. Check if the URL if the values are set as query params.
         * 2. Check if the values are set in the initialMinRange and initialMaxRange data attributes (This values are set from Homes Search pages with an Initial Price Range set).
         */
        const initialMinValue = urlParams.get(minInputName) ? parseInt(urlParams.get(minInputName)) : isNaN(initialMinRange) ? minRange : initialMinRange
        const initialMaxValue = urlParams.get(maxInputName) ? parseInt(urlParams.get(maxInputName)) : isNaN(initialMaxRange) ? maxRange : initialMaxRange

        // UISlider init.
        noUiSlider.create(inputRange, {
            start: [
                initialMinValue, 
                initialMaxValue,
            ],
            step: step,
            connect: true,
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
         * Updates on initialization the hidden input values with no decimals from the URL query values or the default values.
         * This hidden inputs are used to generate the URL queries when filtering.
         */

        // Min initial value.
        inputRangeMin.innerHTML = widgetFormatting.to(initialMinValue)  
        // Sets the max initial value.
        inputRangeMax.innerHTML = widgetFormatting.to(initialMaxValue)

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
