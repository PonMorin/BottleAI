from cv2 import *
class TakePhoto:
    def __init__(self) -> None:
        pass

    def takePicture(self):
        cam_port = 1
        cam = VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            imwrite("Bottle.png", image)
        else:
            print("No image detected. Please! try again")