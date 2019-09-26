$(document).ready(function(){
  $.ajax({
    type: 'POST',
    url: 'https://fourtonfish.com/hellosalut/',
    success: function(data) {
      $.each(data.results, function(i, film) {
        $('UL#list_movies').append("<li>" + film.title +"</li>");
      });
    }
  });
});
