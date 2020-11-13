from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App, Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rotate, Rectangle
from kivy.core.text import LabelBase, DEFAULT_FONT

class MyWidget(Widget):
    evn = None

    def __init__(self, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs)
        self.rect_pos_x = 150
        self.rect_pos_y = 300
        self.rect_pos = self.rect_pos_x, self.rect_pos_y
        self.rect_width = 1500
        self.rect_height = 60
        self.rect_size = self.rect_width, self.rect_height
        self.rotate_origin_x = self.rect_pos_x + self.rect_width / 2
        self.rotate_origin_y = self.rect_pos_y + self.rect_height / 2
        self.rotate_origin = self.rotate_origin_x, self.rotate_origin_y
        self.angle = 0
        self.evn = Clock.schedule_interval(self.update, 0.01)

        self.ellipse_pos_x = 400
        self.ellipse_pos_y = 400
        self.ellipse_pos = (self.ellipse_pos_x, self.ellipse_pos_y)
        self.ellipse_width = 250
        self.ellipse_height = 250
        self.ellipse_size = (self.ellipse_width, self.ellipse_height)
        self.move = 2
        self.evn = Clock.schedule_interval(self.update, 0.01)


    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            Rotate(origin=self.rotate_origin, angle=self.angle)
            Color(rgb=(0, 255, 0))
            Rectangle(pos=self.rect_pos, size=self.rect_size)
        self.angle += dt *0


        self.canvas.clear()
        with self.canvas:
            Color(rgb=(0, 255, 0))
            Ellipse(pos=self.ellipse_pos, size=self.ellipse_size)
            if self.ellipse_pos_x + self.ellipse_width >= self.width:
                self.move = -5
            elif self.ellipse_pos_x <= 0:
                self.move = +5
            self.ellipse_pos_x += self.move
            self.ellipse_pos = (self.ellipse_pos_x, self.ellipse_pos_y)




Builder.load_string('''
<RotatingLineWidget>:
    canvas:
        PushMatrix
        Translate:
            xy: self.pos[0], self.pos[1]
        Rotate:
            angle: -self.angle
            axis: 0, 0, 1
        Color:
            rgba: 1, 1, 1, 1
        Line:
            points: 0, -self.length * 0.5, 0, self.length * 0.5
            width: 3
        PopMatrix
''')


class RotatingLineWidget(Widget):
    length = NumericProperty(10.0)
    angle = NumericProperty()

    def __init__(self, **kwargs):
        super(RotatingLineWidget, self).__init__(**kwargs)

if __name__ == "__main__":
    from kivy.base import runTouchApp
    from kivy.uix.floatlayout import FloatLayout
    from kivy.animation import Animation
    from kivy.properties import ObjectProperty
    from kivy.clock import Clock

    Builder.load_string('''
<MainWindow>:
    line: line
    RotatingLineWidget:
        id: line
        length: 200
        angle: 0
        pos: root.size[0]/2, root.size[1]/2
''')

    class MainWindow(FloatLayout):
        line = ObjectProperty()

        def __init__(self, **kwargs):
            super(MainWindow, self).__init__(**kwargs)
            Clock.schedule_interval(self.animate, 0.9)

        def animate(self, *largs):
            self.line.angle = 0
            a = Animation(angle=360, t='in_out_quad')
            a.start(self.line)

    float_layout = MainWindow()
    Spokes(float_layout)