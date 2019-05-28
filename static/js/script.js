window.onload = function() {
  // set up simulate button
  $('#simulate-button').on('click', function () {
    simulate();
  });

  // simulate if enter is pressed
  $(document).keypress(function(e) {
    var keycode = (e.keyCode ? e.keyCode : e.which);
    if (keycode == '13') {
      simulate();
    }
  });
}

// Display loading gif while simulating
function loading() {
  $('.content').hide();
  $('.loading').show();
}

function simulate() {
  // show loading icon
  loading();

  // get twitter handle from input
  var handle = $('#handle-input').val();

  // not ideal, but it's the only way that's worked so far
  window.location = ('/@' + handle);

  // prevent reloading of page
  event.preventDefault();
}

function another() {
  loading();

  window.location = '';

  //event.preventDefault();
}

function home() {
  window.location = '/';
}
