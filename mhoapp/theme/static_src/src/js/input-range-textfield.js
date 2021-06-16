export default function inputRangeTextfield() {
    const texfields = document.querySelectorAll('.js-money-textfield')

    if ( ! texfields ) {
        return
    }

    // Money formatting
    var moneyFormat = wNumb({
        mark: '.',
        thousand: ',',
        prefix: '$',
    })

    texfields.forEach( texfield => {
        texfield.value = moneyFormat.to(parseInt(texfield.value)) 

        texfield.addEventListener('keyup', () => {
            const moneyAsInt = moneyFormat.from(texfield.value)

            // Prevent showing a "false" value when the user erases the number.
            if ( moneyAsInt ) {
                texfield.value = moneyFormat.to(moneyAsInt)        
            }
        })
    })
}