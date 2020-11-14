from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.app import App, Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rotate, Rectangle, Line
from kivy.core.text import LabelBase, DEFAULT_FONT

class RotatingLineWidget(Widget):


    def __init__(self, **kwargs):
        super(RotatingLineWidget, self).__init__(**kwargs)
        self.length = 200
        self.angle = 0
        self.pos = 100,100

if __name__ == "__main__":
    from kivy.base import runTouchApp
    from kivy.uix.floatlayout import FloatLayout
    from kivy.animation import Animation
    from kivy.properties import ObjectProperty
    # from kivy.clock import Clock

    # Builder.load_string('''
    # <MainWindow>:
    #     line: line
    #     RotatingLineWidget:
    #         id: line
    #         length: 200
    #         angle: 0
    #         pos: root.size[0]/2, root.size[1]/2
    # ''')

    class MainWindow(FloatLayout):
        # line = RotatingLineWidget()
        line = Line(points=[0,0,10,10])

        def __init__(self, **kwargs):
            super(MainWindow, self).__init__(**kwargs)
            Clock.schedule_interval(self.animate, 0.9)

        def animate(self, *largs):
            self.line.angle = 0
            a = Animation(angle=360, t='in_out_quad')
            a.start(self.line)

    float_layout = MainWindow()
    runTouchApp(float_layout)
