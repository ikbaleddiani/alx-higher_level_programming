const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url)
  .done(function (data) {
    for (let i = 0; i < data.count; i++) {
      const movie = '<li>' + data.results[i].title + '</li>';
      $('#list_movies').append(movie);
    }
  });