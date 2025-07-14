const button = document.querySelector('#toggle_header');
button.addEventListener('click', () => {
  const element = document.querySelector('header');
  if (element.classList.contains('red')) {
    element.classList.remove('red');
    element.classList.add('green');
  } else {
    element.classList.remove('green');
    element.classList.add('red');
  }
});
