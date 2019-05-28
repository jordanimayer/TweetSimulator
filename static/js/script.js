window.onload = function() {
  // set up simulate button
  $('#simulate-button').on('click', function () {
    simulate();
  });
}

function simulate() {
  // get twitter handle from input
  var handle = $('#handle-input').val();

  // not ideal, but it's the only way that's worked so far
  window.location = ('/@' + handle);

  // prevent reloading of page
  event.preventDefault();
}

function another() {
  location.reload();  // refresh page
}

function home() {
  console.log('here!');
  window.location = '/';
}
