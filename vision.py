import rr
import math

try:
    index = -1
    names = rr.GetArrayVariable("FIDUCIAL_NAME_ARRAY")
    for x in range(len(names)):
        s = str(names[x])
        if "arrow" in s:
            index = x
    if index != -1:
        rr.SetVariable("InsideVisible", True)
        distances = rr.GetArrayVariable("FIDUCIAL_DISTANCE_ARRAY")
        x_positions = rr.GetArrayVariable("FIDUCIAL_X_COORD_ARRAY")
        
        #Output the horizontal displacement of the middle target
        imageCenterX = rr.GetVariable("IMAGE_WIDTH")/2
        targetX = x_positions[index]
        centerDistance = distances[index]
        rr.SetVariable("TargetDistance", centerDistance)
        rr.SetVariable("TargetX", targetX - imageCenterX)
        rr.SetVariable("TargetVisible", True)
        
        rightIndex = -1
        names = rr.GetArrayVariable("FIDUCIAL_NAME_ARRAY")
        for x in range(len(names)):
            s = str(names[x])
            if "right" in s:
                rightIndex = x
                
        leftIndex = -1
        names = rr.GetArrayVariable("FIDUCIAL_NAME_ARRAY")
        for x in range(len(names)):
            s = str(names[x])
            if "left" in s:
                leftIndex = x
        if leftIndex != -1 and rightIndex != -1: 
            r = distances[leftIndex]
            l = distances[rightIndex]

            rr.SetVariable("r", r)
            rr.SetVariable("l", l)
            
            cam = 14.125

            beforeL = (-(l**2)+cam**2+r**2)/(2*cam*r)
            beforeR = (l**2+cam**2-r**2)/(2*l*cam)
            rr.SetVariable("before L", beforeL)
            rr.SetVariable("before R", beforeR)
            L = math.acos(beforeL)
            R = math.acos(beforeR)

            A = math.pi - L - R
            C = (math.pi-A)/2.0

            error = C-L
            
            #rr.SetVariable("C", C*180./math.pi)
            #rr.SetVariable("A", A*180./math.pi)
            rr.SetVariable("TargetAngleError", error)
            rr.SetVariable("OutsidesVisible", True)
        else:
            rr.SetVariable("OutsidesVisible", False)
    else:
        rr.SetVariable("InsideVisible", False)
    rr.SetVariable("TargetVisible", True)
except TypeError:
    rr.SetVariable("TargetVisible", False)
except NameError:
    rr.SetVariable("TargetVisible", False)
except ValueError:
    rr.SetVariable("TargetVisible", False)
