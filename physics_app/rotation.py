import kivy
# kivy.require('1.10.0')
from kivy.app import App
from kivy.properties import *
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
#from transitions import Machine
from kivy.core.window import Window
from kivy.clock import Clock
from functools import partial
from time import time
from helper_functions import unit_vector, _sin_cos
from vector import Vector
from kivy.graphics.instructions import *
from kivy.uix.screenmanager import ScreenManager, Screen

from config_projectile import *
from kivy.lang import Builder


# Builder.load_file('physics.kv')


line_points=[0,0,200,200]
# Line(points=line_points, group='arrows')


class Spoke(Widget):
    # line_points = line_points
    def __init__(self, **kwargs):
        super(Spoke, self).__init__(**kwargs)

        self.spoke_length = 125 # half_length
        app = App.get_running_app()
        print("root------")
        print(app.root)
        self.pos = app.root.pos
        self.angle=90
        line_end_1=unit_vector(self.spoke_length, self.angle)
        line_end_2=unit_vector(self.spoke_length, -1*self.angle)
        p1=Vector(*self.pos)+line_end_1
        p2=Vector(*self.pos)+line_end_2
        # import pdb; pdb.set_trace()
        self.line_points=[p1[0],p1[1],p2[0],p2[1]]
        Clock.schedule_interval(self.rotate_spoke, 0.1)

    def rotate_spoke(self, dt):
        # if self.ellipse_pos_x + self.ellipse_width >= 500:
        #     self.move = -10
        # elif self.ellipse_pos_x <= 0:
        self.angle = +10
        # self.pos = (self.ellipse_pos_x, self.ellipse_pos_y)
        line_end_1=unit_vector(self.spoke_length, self.angle)
        line_end_2=unit_vector(self.spoke_length, -1*self.angle)
        p1=Vector(*self.pos)+line_end_1
        p2=Vector(*self.pos)+line_end_2
        self.line_points=[p1[0],p1[1],p2[0],p2[1]]
        # return Line(points=line_points)

class Wheel(Widget):
    

    def __init__(self, **kwargs):
        super(Wheel, self).__init__(**kwargs)
        self.ellipse_pos_x = 320
        self.ellipse_pos_y = 260
        self.pos = (self.ellipse_pos_x, self.ellipse_pos_y)
        self.ellipse_width = 250
        self.ellipse_height = 250
        self.size = (self.ellipse_width, self.ellipse_height)
        self.pos=(self.ellipse_pos_x, self.ellipse_pos_y)
        self.size=(self.ellipse_width, self.ellipse_height)
        Clock.schedule_interval(self.rotate_wheel, 0.1)
        # line_points = line_points
        # return Line(points=line_points)

    def rotate_wheel(self, dt):
        # if self.ellipse_pos_x + self.ellipse_width >= 500:
        #     self.move = -10
        # elif self.ellipse_pos_x <= 0:
        self.move = +10

        self.ellipse_pos_x += self.move
        self.pos = (self.ellipse_pos_x, self.ellipse_pos_y)


class CompleteWheel(Widget):
    spoke = ObjectProperty(None)
    wheel = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(CompleteWheel, self).__init__(**kwargs)    


class RotationApp(App):

    def build(self):
        # arrow1 = Arrow1()
        # arrow1 = ObjectProperty(None)
        return CompleteWheel()


if __name__ == "__main__":
    RotationApp().run()