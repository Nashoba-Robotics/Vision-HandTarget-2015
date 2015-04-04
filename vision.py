import rr
import math

try: 
    distances = rr.GetArrayVariable("FIDUCIAL_DISTANCE_ARRAY")

    r = distances[0]
    l = distances[2]
    cam = 14.125

    L = math.acos((-(l**2)+cam**2+r**2)/(2*cam*r))
    R = math.acos((l**2+cam**2-r**2)/(2*l*cam))

    A = math.pi - L - R
    C = (math.pi-A)/2.0

    error = C-L
    
    rr.SetVariable("C", C*180./math.pi)
    rr.SetVariable("A", A*180./math.pi)
    rr.SetVariable("Error", error*180./math.pi/2)
    rr.SetVariable("Visible", True)
except IndexError:
    rr.SetVariable("Visible", False)
except ValueError:
    rr.SetVariable("Visible", False)
