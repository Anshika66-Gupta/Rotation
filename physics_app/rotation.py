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


line_points=[0,0,200,200]
# Line(points=line_points, group='arrows')

class Arrow1(Widget):
    def __init__(self, **kwargs):
        super(Arrow1, self).__init__(**kwargs)
        # self._points = line_points

    @property
    def points(self):
        return self._points



class RotationApp(App):
	def build(self):
		arrow1 = ObjectProperty(None)



if __name__ == "__main__":
    RotationApp().run()