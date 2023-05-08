/* global $ */
// am adding $ as global since semistandard doesnt recognized and raises error
$(document).ready(function () {
    fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => response.json())
    .then(function (data) {
        $('#character').text(data.name);
    })
    .catch(error => console.log(error));
});
