from predic import *
from takePhoto import *

class Main:
    def __init__(self) -> None:
        self.getName = ""
    
    def getData(self):
        getModel = PredicData()
        getModel.sendData()
        
    
    def capture(self):
        openCam = TakePhoto()
        openCam.takePicture()

    
a = Main()
a.getData()
# a.capture()

def checkBottle(self):
                readyToCap = TakePhoto()
                getModel = PredicData()
                readyToCap.takePicture()
                print("In progress....")
                self.getLabel = getModel.sendData()
                print(self.getLabel)