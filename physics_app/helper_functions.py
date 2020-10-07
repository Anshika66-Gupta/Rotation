import math
from vector import Vector

def __sin_cos(theta):
	theta_in_radians = math.radians(theta)
	return ( math.sin(theta_in_radians), math.cos(theta_in_radians) )

def _sin_cos(theta):
	return Vector(*__sin_cos(theta))

def unit_vector(length, theta): # not a unit vector, but unit vector * length
	return _sin_cos(theta).__rmul__(length)