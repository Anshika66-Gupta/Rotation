from kivy.app import App, Widget
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App, Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rotate, Rectangle
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.text import LabelBase, DEFAULT_FONT



class MyWidget(Widget):
    evn = None
    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.ellipse_pos_x = 320
        self.ellipse_pos_y = 260
        self.ellipse_pos = (self.ellipse_pos_x, self.ellipse_pos_y)
        self.ellipse_width = 250
        self.ellipse_height = 250
        self.ellipse_size = (self.ellipse_width, self.ellipse_height)
        self.move = 2
        self.evn = Clock.schedule_interval(self.update, 0.01)
        self.rect_pos_x = 150
        self.rect_pos_y = 200
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 1500
        self.rect_height = 60
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 0
        self.evn = Clock.schedule_interval(self.update, 0.01)

    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            Color(rgb=(0, 250, 0))
            Ellipse(pos=self.ellipse_pos, size=self.ellipse_size)
            if self.ellipse_pos_x + self.ellipse_width >= self.width:
                self.move = -3
            elif self.ellipse_pos_x <= 0:
                self.move = +3
            self.ellipse_pos_x += self.move
            self.ellipse_pos = (self.ellipse_pos_x, self.ellipse_pos_y)
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 0))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
        self.angle += dt * 0



class rotateapp(App):
    def build(self):
        return MyWidget()


rotateapp().run()