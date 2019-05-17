window.onload = function() {
  // set up simulate button
  $('#simulate-button').on('click', function () {
    simulate();
  });
}

function simulate() {
  console.log('clicked button')

  // get twitter handle from input
  var handle = $('#handle-input').val();
  console.log('handle: ' + handle);

  // not ideal, but it's the only way that's worked so far
  window.location = ('/@' + handle);

  // prevent reloading of page
  event.preventDefault();
}
