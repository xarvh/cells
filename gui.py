#!/usr/bin/python -B
"""
Loads and display populations through their whole evolutionary history.

"""
from pyglet.gl import *
import pyglet.window.key as key
import random
import sys



from pyglet import image


class PixelSpace:
  def __init__(self, width, height, gui=None):
    self.width = width
    self.height = height
    self.gui = gui or Gui(self.draw)

    self.image = image.ColorBufferImage(0, 0, width, height)
    self.buffer = [0] * width * height * 3


  def pixel(self, x, y, color=None):
    offset = (x + y*self.width) * 3
    bf = self.buffer

    if color:
      bf[offset + 0], bf[offset+1], bf[offset+2] = color

    return bf[offset + 0], bf[offset+1], bf[offset+2]


  def draw(self):
    self.image.get_image_data().set_data('RGB', self.width*3, self.buffer)
    self.gui.window.clear()
    self.image.blit(0, 0)
    


class Gui:

  def __init__(self, draw, forcedRedrawFrequency = 0):
    self.draw = draw
    if forcedRedrawFrequency:
      pyglet.clock.schedule_interval(self.draw, 1.0/forcedRedrawFrequency)

    self.keys = key.KeyStateHandler()
    self.window = pyglet.window.Window()
    self.window.push_handlers(self.keys)
    self.window.on_draw = self.draw


#    def keyboard_input(self):
#        if self.keys[key.LEFT]: self.select_individual(-1)
#        if self.keys[key.RIGHT]: self.select_individual(+1)
#        if self.keys[key.UP]: self.select_generation(-1)
#        if self.keys[key.DOWN]: self.select_generation(+1)
#        if symbol == key.s: screenshot.take()
#        if symbol == key.ENTER:
#            print 'saving genome'
#            open('new_genomes', 'ab').write(sw.body.genome + '\n')



#    def draw(self):
#        self.window.clear()
#
#        # glMatrixMode interferes with text rendering
#        glPushMatrix()
#        #glMatrixMode(GL_PROJECTION)
#        glLoadIdentity()
#        w = self.window.width
#        h = self.window.height
#        glTranslated(w/2, h/2, 0)
#        glScaled(h/2, h/2, 1)   # want uniform coordinates
#        #glMatrixMode(GL_MODELVIEW)
#
#
#        # write label
#        text = "ind %d/%d, gen %d/%d, cells %d" % (
#            self.sind, len(self.pops[self.sgen]),
#            self.sgen, len(self.pops),
#            len(self.dbody)
#        )
#        glPushMatrix()
#        pyglet.text.Label(text,
#            font_name='Times New Roman', font_size=20,
#            x=5, y=5, anchor_x='left', anchor_y='bottom').draw()
#        glPopMatrix()





#    # perform operations that required drawing to be completed
#    def after_draw(self):
#        pass









#=========================================================================================


#"""
#class screenshot:
#    cnt = 0
#    @staticmethod
#    def take(name=None):
#        if not name:
#            screenshot.cnt += 1
#            name = 'shot%04d.png' % screenshot.cnt
#        pyglet.image.get_buffer_manager().get_color_buffer().save(name)
#
#
#
#
#
#    def after_draw(self):
#        if '--shot' in sys.argv:
#            screenshot.take('movie%04d.png' % self.total_cnt)
#
#        self.total_cnt += 1
#
#        if not self.free:
#            self.frames_cnt += 1
#            if self.frames_cnt >= self.frames_per_body:
#                if self.genomes:
#                    self.next()
#                else:
#                    sys.exit(0)
#"""



# =============================================================================


def main():

    ps = PixelSpace(400, 400)

    while True:
      r, g, b = [random.uniform(0, 255) for i in 'rgb']
      for x in range(ps.width):
        for y in range(ps.height):
          ps.pixel(x, y, (r, g, b))
      ps.draw()



if __name__ == '__main__':
    main()

#EOF ==========================================================================
