//
var context, width, height, frames = null


//
var draw = function() {

  var imageData = context.createImageData(width, height);

  var data = imageData.data;
  for(var x = 0; x < width; x++) {
    for(var y = 0; y < height; y++) {
      i = (x + y * width) * 4;

      data[i] = x % 256;
      data[i+1] = y % 256;
      data[i+2] = 0;
      data[i+3] = 255;
    }
  }

  context.putImageData(imageData, 0, 0, 0, 0, width, height);
}















window.onload = function() {

  var gf = window.gridFrames

  width = gf.width
  height = gf.height
  frames = gf.frames
  context = document.getElementById('grid').getContext('2d');

  context.canvas.width = width
  context.canvas.height = height

  draw()
}

