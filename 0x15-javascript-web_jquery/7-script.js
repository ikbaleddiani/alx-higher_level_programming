const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url)
  .done(function (data) {
    $('#character').replaceWith(data.name);
  });