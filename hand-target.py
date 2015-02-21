import rr

imageCenterX = rr.GetVariable("IMAGE_WIDTH")/2
imageCenterY = rr.GetVariable("IMAGE_HEIGHT")/2

rr.SetVariable("ImageCenterX", imageCenterX)
rr.SetVariable("ImageCenterY", imageCenterY)

targetX = rr.GetVariable("FIDUCIAL_X_COORD")
targetY = rr.GetVariable("FIDUCIAL_Y_COORD")

if targetX == 0 and targetY == 0:
    rr.SetVariable("TargetVisible", False)
else:
    rr.SetVariable("TargetVisible", True)

rr.SetVariable("TargetX", targetX - imageCenterX)
rr.SetVariable("TargetY", targetY - imageCenterY)
