fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => response.json())
  .then((data) => {
    const list = document.querySelector('#list_movies');
    data.results.forEach((movie) => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      list.appendChild(li);
    });
  })
  .catch((error) => console.error('Erreur :', error));
