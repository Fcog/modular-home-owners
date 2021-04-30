/**
 * Sets the correct URL query params when using the Price Range select field.
 * Removes the price Select query URL before submitting.
 */
export default function heroHomePriceRange() {
    const form = document.getElementById('hero-home-form')

    if (!form) {
        return
    }

    const priceRangeSelect = document.getElementById('price-range')
    const minPriceInput = document.getElementById('min-price-range')
    const maxPriceInput = document.getElementById('max-price-range')

    priceRangeSelect.addEventListener('change', event => {
        const value = event.target.value

        const parts = value.split('-')

        if (parts[0] === 'under') {
            maxPriceInput.value = parts[1]
            minPriceInput.value = null
        } else {
            minPriceInput.value = parts[1]
            maxPriceInput.value = null
        }
    })

    /**
     * Remove URL query params from Select field and when an input range is null.
     */
    form.addEventListener('submit', event => {
        event.preventDefault()

        priceRangeSelect.disabled = true

        if (!minPriceInput.value) {
            minPriceInput.disabled = true
        }

        if (!maxPriceInput.value) {
            maxPriceInput.disabled = true
        }        

        form.submit()
    })
}