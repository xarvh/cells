//
var context, width, height = null
var frames = []
var mouseX, mouseY, frameId = 0
var imageData = null


var draw = function() {


  var data = imageData.data
  var frame = frames[frameId]


  for(var x = 0; x < width; x++) {
    for(var y = 0; y < height; y++) {
      i = (x + y * width) * 4

      data[i] = frame.r
      data[i+1] = frame.g
      data[i+2] = frame.b
      data[i+3] = 255
    }
  }

  context.putImageData(imageData, 0, 0, 0, 0, width, height)
}


function findPos(obj) {
  var curleft = 0, curtop = 0
  while (obj.offsetParent) {
    curleft += obj.offsetLeft
    curtop += obj.offsetTop
    obj = obj.offsetParent
  }
  return { x: curleft, y: curtop }
}


window.onload = function() {

  var canavasE = document.getElementById('grid')
  var gf = window.gridFrames

  // set globals
  width = gf.width
  height = gf.height
  frames = gf.frames
  context = canavasE.getContext('2d')
  imageData = context.createImageData(width, height)

  // set context size
  context.canvas.width = width
  context.canvas.height = height

  // set hooks
  canavasE.onmousemove = function(e) {
    var pos = findPos(this)
    mouseX = e.pageX - pos.x
    mouseY = e.pageY - pos.y
    draw()
  }

  frameE = document.getElementById('frame-selector')
  frameE.value = frameId = frames.length - 1
  frameE.onchange = function(e) {
    e.target.value = frameId = (parseInt(e.target.value) + frames.length) % frames.length
    draw()
  }

  // initial draw
  draw()
}

