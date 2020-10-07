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
from helper_functions import unit_vector
from vector import Vector
from kivy.graphics.instructions import *
from kivy.uix.screenmanager import ScreenManager, Screen

from config_projectile import *
