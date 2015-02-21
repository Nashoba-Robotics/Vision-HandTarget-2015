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
    points = Corners(Point(c[0], c[1]), Point(c[2], c[3]), Point(c[4], c[5]), Point(c[6], c[7]))

    PArray = Corners(cameraYToWorldP(points[0].y), cameraYToWorldP(points[1].y), cameraYToWorldP(points[2].y), cameraYToWorldP(points[3].y))
    
    leftP = average((PArray.topLeft, PArray.bottomLeft))
    rightP = average((PArray.topRight, PArray.bottomRight))
    centerP = average((leftP, rightP))
    print(points)
    
    leftTheta = average((cameraXToWorldTheta(points.topLeft.x), cameraXToWorldTheta(points.bottomLeft.x)))
    rightTheta = average((cameraXToWorldTheta(points.topRight.x), cameraXToWorldTheta(points.bottomRight.x)))
    centerTheta = average((leftTheta, rightTheta))

    targetX = 0
    targetY = 0
    if rightP <= leftP:
        insideLeftTheta = math.fabs(leftTheta-centerTheta)
        farLeftHalf = math.sqrt(centerP**2 + leftP**2 - 2*centerP*leftP*math.cos(insideLeftTheta))
        farLeftAngle = math.asin(centerP * math.sin(insideLeftTheta) / farLeftHalf)

        targetX = math.sin(farLeftAngle) * leftP

        bigAngle = 90 - farLeftAngle
        combinedInsideRight = bigAngle - insideLeftTheta
        targetY = -math.sin(combinedInsideRight) * centerP
    else:
        insideRightTheta = math.abs(centerTheta - rightTheta)
        farRightHalf = math.sqrt(centerP**2 + rightP**2 - 2*centerP*rightP*math.cos(insideRightTheta))
        farRightAngle = math.asin(centerP * math.sin(insideRightTheta) / farRightHalf)

        targetX = math.sin(farRihtAngle) * rightP

        bigAngle = 90 - farRightAngle
        combinedInsideLeft = bigAngle - insideRightTheta
        targetY = -math.sin(combinedInsideLeft) * centerP
    rr.SetVariable("Target X", targetX)
    rr.SetVariable("Target Y", targetY)
    
except (ValueError, ZeroDivisionError):
    pass
