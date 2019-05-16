window.onload = function() {
  // // set up simulate button
  // $('#simulate-button').onclick = function() {
  //   simulate();
  // };

  $('#simulate-button').on('click', function () {
    simulate();
  });
}

function simulate() {
  console.log('clicked button')

  // get twitter handle from input
  var handle = $('#handle-input').val();
  console.log('handle: ' + handle);

  window.location = ('/@' + handle);

  // console.log('sending handle')
  // // send handle to python
  // $.post('/posthandle', {
  //   js_handle: handle
  // });
  //
  // console.log('getting tweet')
  // // get simulated tweet from python
  // $.get('/gettweet', function(data) {
  //   tweet_str = $.parseJSON(data);
  //   console.log(tweet_str);
  // });

  // prevent reloading of page
  event.preventDefault();
}
