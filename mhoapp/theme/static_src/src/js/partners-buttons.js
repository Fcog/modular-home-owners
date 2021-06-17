/**
 * Toggles the partners logos section from the Partners Buttons block.
 */
export default function partnersButtons() {
    const partnersButtonsContainers = document.querySelectorAll('.js-partners-buttons')

    // Do the same behaviour if there are multiple instances of the block in the same page.
    partnersButtonsContainers.forEach( partnersButtonsContainer => {
        const partnerButtons = partnersButtonsContainer.querySelectorAll('.js-button-icon')
        const partnersLogoSection = partnersButtonsContainer.querySelector('.js-partners-buttons-ajax-response')

        // For all buttons.
        partnerButtons.forEach( partnerButton => {
            // On button click.
            partnerButton.addEventListener('click', event => {
                // If user clicked the same button.
                if (partnerButton.classList.contains('active')) {
                    // Hide the partners logo section if user clicked the same button.
                    partnersLogoSection.classList.add('hidden')

                    // Remove the styling and active states of all buttons.
                    resetState()
                } else {
                    // Remove the styling and active states of all buttons.
                    resetState()

                    // Add the button styling to the current button.
                    addActiveButtonState(partnerButton)

                    // Show the partners logo section.
                    partnersLogoSection.classList.remove('hidden')

                    // Add the active state to the current button.
                    partnerButton.classList.add('active')
                }
            })
        })

        // Remove the styling and active state of all buttons.
        function resetState() {
            partnerButtons.forEach( partnerButton => {
                partnerButton.classList.remove('active')
                removeActiveButtonState(partnerButton)
            })
        }        

        function addActiveButtonState(buttonContainer) {
            const button = buttonContainer.querySelector('.js-button')
            const icon = buttonContainer.querySelector('.js-button-icon-icon')
            const iconInverted = buttonContainer.querySelector('.js-button-icon-icon-inverted')
            
            if (button) {
                button.classList.add('bg-blue-light')
                button.classList.remove('text-blue-light')
                button.classList.add('text-white')
            }

            if (icon) {
                icon.classList.add('hidden')
                icon.classList.add('group-hover:hidden')
            }
            
            if (iconInverted) {
                iconInverted.classList.remove('hidden')    
                iconInverted.classList.add('group-hover:block')   
            }
        }        

        function removeActiveButtonState(buttonContainer) {
            const button = buttonContainer.querySelector('.js-button')
            const icon = buttonContainer.querySelector('.js-button-icon-icon')
            const iconInverted = buttonContainer.querySelector('.js-button-icon-icon-inverted')

            if (button) {
                button.classList.remove('bg-blue-light')
                button.classList.remove('hover:bg-blue-light')
                button.classList.remove('group-hover:bg-blue-light')
                button.classList.add('text-blue-light')
                button.classList.remove('text-white')
                button.classList.remove('hover:text-white')
                button.classList.remove('group-hover:text-white')
            }

            if (icon) {
                icon.classList.remove('hidden')
                icon.classList.remove('group-hover:hidden')
            }
            
            if (iconInverted) {
                iconInverted.classList.add('hidden')    
                iconInverted.classList.remove('group-hover:block')    
            }
        }
    })
}