import Splide from '@splidejs/splide'

// Initiate sliders.
export default function slider() {
    const sliders = document.querySelectorAll('.splide')

    sliders.forEach( slider => {    
        new Splide(slider, {
            pagination: false,
            focus: 'center',
        }).mount()
    })
}