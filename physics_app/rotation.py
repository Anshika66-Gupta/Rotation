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


class Arrow1(Widget):
    def __init__(self, **kwargs):
        super(Arrow1, self).__init__(**kwargs)
        # self.points = line_points
        # return Line(points=line_points)


class RotationApp(App):

	arrow1 = ObjectProperty(None)
	def build(self):
		# arrow1 = Arrow1()
		# arrow1 = ObjectProperty(None)
		return Arrow1()


if __name__ == "__main__":
    RotationApp().run()