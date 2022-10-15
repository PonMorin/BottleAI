from cv2 import *
  
# initialize the camera
# If you have multiple camera connected with 
# current device, assign a value in cam_port 
# variable according to that
cam_port = 1
cam = VideoCapture(cam_port)
  
# reading the input using the camera
result, image = cam.read()
  
# If image will detected without any error, 
# show result
if result:
  
    # showing result, it take frame name and image 
    # output
    imshow("Bottle", image)
  
    # saving image in local storage
    imwrite("Bottle.png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    waitKey(0)
    destroyWindow("Bottle")
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")