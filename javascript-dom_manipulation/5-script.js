const button = document.querySelector('#update_header');
button.addEventListener('click', () => {
  const element = document.querySelector('header');
  element.textContent = 'New Header!!!';
});
