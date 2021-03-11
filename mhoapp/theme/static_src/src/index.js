import './styles.css';

document.addEventListener( 'DOMContentLoaded', () => {
    redirectToSearch()
})

function redirectToSearch() {
    document
        .getElementById('search-homes')
        .addEventListener('click', function() {
            const params = new URLSearchParams({
                'style': document.getElementById('style').value,
                'price-range': document.getElementById('price-range').value,
            })
            window.location.href = window.location.href + 'homes?' + params
        }, false )
}