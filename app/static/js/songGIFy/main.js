var beat = 2450

smilin_onplay = function() {
    console.log("The video has started to play");
    setTimeout(automatic, 8500)
};


function myFunction() {
  var x = document.getElementById("frm1");
  var text = "";
  text += x.elements[0].value;

  callApi(text, function(response){
    res = JSON.parse(response);
    // console.log(res.data.embed_url);
    document.getElementById("gif").src = res.data.embed_url
    // document.getElementById("gif").src = res.data.image_url
  })

}

function automatic(){
  var i = 0
  recursive(i)
}

function recursive(i){
  console.log(phrases[i].phrase);
  setTimeout(function(){
    text = phrases[i].phrase

    callApi(text, function(response){
      res = JSON.parse(response);

      document.getElementById("gif").src = res.data.embed_url;

      document.getElementById("lyrics").innerHTML = phrases[i].lyrics;

      i++
      if (i<phrases.length) {
        recursive(i)
      }
    })
  }, (i==0) ? 0 : phrases[i-1].duration * beat)
}

function translate(phrase){
  endpoint = "https://api.giphy.com/v1/gifs/translate"
  api_key = "dc6zaTOxFJmzC"
  built = endpoint + "?api_key=" + api_key + "&s=" + phrase.replace(" ", "+") + "&fmt=json&rating=r"
  console.log(built);
  return built
}

function random(phrase){
  tags = phrase.split(" ");
  endpoint = "https://api.giphy.com/v1/gifs/random"
  api_key = "dc6zaTOxFJmzC"
  built = endpoint + "?api_key=" + api_key + "&fmt=json&tag=" + tags.join("+")
  console.log(built);
  return built
}

function httpGetAsync(theUrl, callback){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
    if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
    // console.log(xmlHttp.responseText);
    callback(xmlHttp.responseText);
  }
  xmlHttp.open("GET", theUrl, true); // true for asynchronous
  xmlHttp.send(null);
}

function callApi(phrase, callback){
  // url = random(phrase)
  url = translate(phrase)
  httpGetAsync(url, callback)
}

function readTextFile(file)
{
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", file, false);
  rawFile.onreadystatechange = function ()
  {
    if(rawFile.readyState === 4)
    {
      if(rawFile.status === 200 || rawFile.status == 0)
      {
        var allText = rawFile.responseText;
        alert(allText);
      }
    }
  }
  rawFile.send(null);
}
