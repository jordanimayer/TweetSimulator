window.onload = function() {
  // set up simulate button
  $("#simulate-button").onclick = function() {
    simulate();
  };
}

function simulate() {
  // get twitter handle from input
  var handle = $("#handle-input").val();

  // send handle to python
  $.post("/posthandle"), {
    js_handle: handle
  });

  // get simulated tweet from python
  $.get('/gettweet', function(data) {
    tweet_str = $.parseJSON(data);
    console.log(tweet_str);
  });

  // prevent reloading of page
  event.preventDefault();
}
