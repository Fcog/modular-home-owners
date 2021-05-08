import Splide from '@splidejs/splide'

// Initiate sliders.
export default function slider() {
    const slidersHomes = document.querySelectorAll('.js-splide-homes')

    slidersHomes.forEach( slider => {    
        new Splide(slider, {
            pagination: false,
            focus: 'center',
        }).mount()
    })

    const sliderContainers = document.querySelectorAll('.js-slide-images')

    sliderContainers.forEach( sliderContainer => {    
        const thumbnailsSlider = new Splide(sliderContainer.querySelector('.js-thumbnails'), {
            fixedWidth: 247,
            height: 184,
            rewind: true,
            gap : 20,
            pagination: false,
            arrows: false,
            cover: true,
        }).mount()

        const mainSlider = new Splide(sliderContainer.querySelector('.js-main-slider'), {
            heightRatio: 0.745, 
            cover: true,        
            pagination: false,
            focus: 'center',
            breakpoints: {
                768: {
                    pagination: true,
                }
            }
        })

        mainSlider.sync( thumbnailsSlider ).mount();
    })    
}