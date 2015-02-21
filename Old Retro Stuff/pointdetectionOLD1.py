import rr
import math
from collections import namedtuple

#Axis m1013 field of view 62.38 degrees in the x direction
cameraWidth = rr.GetVariable("IMAGE_WIDTH")
cameraHeight = rr.GetVariable("IMAGE_HEIGHT")
fieldOfView = 62.4 #Horizontal field of view
degreesPerPixel = 62.4/cameraWidth
cameraHeightAboveTarget = 0

#Define named tuples for better self-documentation of our point array
Point = namedtuple('Point', 'x y')
Corners = namedtuple('Corners', 'topRight topLeft bottomLeft bottomRight')

#Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt( (p1.x - p2.x)**2 + (p1.y - p2.y)**2)
#Calculates arithmetic mean of a list
def average(list):
    return sum(list)/len(list)
def pointAverage(p1, p2):
    return Point((p1.x+p2.x)/2,(p1.y+p2.y)/2)
def cameraYToWorldP(y):
    Yp = (cameraHeight/2)-y
    theta = Yp * degreesPerPixel
    return cameraHeightAboveTarget/math.tan(theta)
def cameraXToWorldTheta(x):
    theta = (x-cameraWidth/2) * degreesPerPixel
    return theta
def slope(p1, p2):
    return (p1.y-p2.y)/(p1.x-p2.x)

#Program Start Here
c = rr.GetArrayVariable("MEQ_COORDINATES")

try:
    centerP = rr.GetVariable("FIDUCIAL_DISTANCE")
    thetaY = 
    cameraPlaneP = 
    
except (ValueError, ZeroDivisionError):
    pass
