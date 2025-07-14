window.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then((data) => {
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => console.error('Erreur :', error));
});
