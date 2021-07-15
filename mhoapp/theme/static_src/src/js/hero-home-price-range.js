/**
 * Redirects to the proper Home Styles or Price Range pages if the Select fields are used. 
 * Else redirect to the Main Homes search page.
 * 
 * Also cleans the URL query params.
 */
export default function heroHomePriceRange() {
    let form = null
    let styleSelect = null
    let priceRangeSelect = null
    let minPriceInput = null
    let maxPriceInput = null

    const init = () => {
        form = document.getElementById('js-hero-home-form')

        if (!form) {
            return
        }
    
        styleSelect = document.getElementById('style')
        priceRangeSelect = document.getElementById('price-range')
        minPriceInput = document.getElementById('min-price-range')
        maxPriceInput = document.getElementById('max-price-range')
    
        bindEvents()
    }

    const bindEvents = () => {
        priceRangeSelect.addEventListener('change', priceDecoding)
        form.addEventListener('submit', onSubmit)
    }

    const priceDecoding = event => {
        const value = event.target.value

        const valueParts = value.split('-')

        minPriceInput.value = valueParts[0] === 'under' ? null: valueParts[1]
        maxPriceInput.value  = valueParts[0] === 'under' ? valueParts[1] : null
    }

    /**
     * On submit, check which Select field was changed and redirect accordingly to the
     * a Home Style page or to a Price Range page. 
     * 
     * If it redirects to a Home Style page then don't show the Style URL query.
     * If it redirects to a Price Range page then don't show the Price Range URL queries.
     * 
     * @param {*} event 
     */
    const onSubmit = event => {
        event.preventDefault()
        
        changeFormActionURL()

        if (redirectToHomeStylePage()) {
            removeHomeStyleURLQuery()
            cleanMaxMinPriceURLQueries()
        } else {
            removePriceURLQuery()
        }
        
        form.submit()
    }

    const redirectToHomeStylePage = () => styleSelect[styleSelect.selectedIndex].dataset.custom !== undefined
    const redirectToPriceRangePage = () => priceRangeSelect[priceRangeSelect.selectedIndex].dataset.custom !== undefined

    const changeFormActionURL = () => {
        const stylePageURL = styleSelect[styleSelect.selectedIndex].dataset.custom
        const pricePageURL = priceRangeSelect[priceRangeSelect.selectedIndex].dataset.custom
        form.action = redirectToHomeStylePage() ? stylePageURL : redirectToPriceRangePage() ? pricePageURL : form.action
    }

    const removePriceURLQuery = () => {
        minPriceInput.disabled = true
        maxPriceInput.disabled = true
        priceRangeSelect.disabled = true
    }

    const removeHomeStyleURLQuery = () => {
        styleSelect.disabled = true
    }

    /**
     * Removes the max or min URL query params accordingly from the Select field. 
     * Also removes the price URL queries when no input range is selected.
     */
    const cleanMaxMinPriceURLQueries = () => {
        priceRangeSelect.disabled = true

        if (!minPriceInput.value) {
            minPriceInput.disabled = true
        }

        if (!maxPriceInput.value) {
            maxPriceInput.disabled = true
        }        
    }

    return {
        init,
    }
}