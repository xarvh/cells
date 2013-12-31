//
var context, width, height, frames = null
var mouseX, mouseY, frameId = 0


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









function findPos(obj) {
  var curleft = 0, curtop = 0;
  while (obj.offsetParent) {
    curleft += obj.offsetLeft;
    curtop += obj.offsetTop;
    obj = obj.offsetParent;
  }
  return { x: curleft, y: curtop };
}


window.onload = function() {

  var canavasE = document.getElementById('grid')
  var gf = window.gridFrames

  // set globals
  width = gf.width
  height = gf.height
  frames = gf.frames
  context = canavasE.getContext('2d');

  // set context size
  context.canvas.width = width
  context.canvas.height = height

  // set hooks
  canavasE.onmousemove = function(e) {
    var pos = findPos(this);
    mouseX = e.pageX - pos.x;
    mouseY = e.pageY - pos.y;
    draw()
  };

  // initial draw
  draw()
}

