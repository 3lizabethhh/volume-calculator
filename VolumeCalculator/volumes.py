# calculates volume of cubes
import math
def cube(sideLength):
  volume = sideLength*sideLength*sideLength
  return volume

def pyramid(base,height):
  volume = (1/3) *base*base*height
  return volume

def ellipsoid(r1,r2,r3):
  volume = (4/3)*math.pi*r1*r2*r3
  return volume
