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
a.capture()
a.getData()


