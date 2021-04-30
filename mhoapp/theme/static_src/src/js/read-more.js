// Initiate read more texts.
export default function readMore() {
    const readMoreContainers = document.querySelectorAll('.js-read-more')

    readMoreContainers.forEach( readMoreContainer => {
        const readMoreButton = readMoreContainer.querySelector('.js-read-more-button')
        const readMoreText = readMoreContainer.querySelector('.js-read-more-text')

        readMoreButton.addEventListener('click', event => {
            readMoreText.classList.toggle('hidden')
            readMoreButton.classList.add('hidden')
        })
    })
}