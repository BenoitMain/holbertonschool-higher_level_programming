const button = document.querySelector('#red_header');
button.addEventListener('click', () => {
  const element = document.querySelector('header');
  element.classList.add('red');
});
