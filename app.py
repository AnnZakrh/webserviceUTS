<!DOCTYPE html>
<html>

<head>
<! — title displayed on the browser tab →
<title>image classification app</title>
</head>

<! — contains our front-end elements →
<body>
<! — input to upload the image →
<input id=”upload” type=”file”>
<! — button to activate the script which call our Flask app →
<button id=”predict-button”>Predict</button>
<h1>Predictions</h1>
<! — parapgraph where we will display the result →
<p><span id=”prediction”></span></p>
<! — display the uploaded image →
<img id=”selected-image” src=””/>
</body>
<! — jquery lib →
<script src=”https://code.jquery.com/jquery-3.3.1.min.js”></script>
<! — The script which call our Flask app →
<script>
let base64Image;
// when we upload an image
$(“#upload”).change(function() {
let reader = new FileReader();
reader.onload = function(e) {
let dataURL = reader.result;
$(‘#selected-image’).attr(“src”, dataURL);
base64Image = dataURL.replace(“data:image/png;base64,”,””);
}
reader.readAsDataURL($(“#upload”)[0].files[0]);
//reset pred text as empty
$(“#prediction”).text(“”);
});
$(“#predict-button”).click(function(){
let message = {image: base64Image}
// you could also use 127.0.0.1 instead of 0.0.0.0
$.post(“https://127.0.0.1:5000/predict”, JSON.stringify(message), function(response){
$(“#prediction”).text(“results: “+response.prediction[0][0]+” ( confidence : “+response.prediction[0][1]+")");
console.log(response);
});
});
</script>