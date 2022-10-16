import tensorflow.keras

from PIL import Image, ImageOps
import numpy as np

class PredicData:
    def __init__(self) -> None:
        self.model = tensorflow.keras.models.load_model('keras_model.h5')
    
    def sendData(self):
        with open('labels.txt', 'r') as f:
            class_names = f.read().split('\n')

        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        image = Image.open('test04.jpg').convert('RGB')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        
        image_array = np.asarray(image)
        
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        
        data[0] = normalized_image_array

        prediction = self.model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        send_className = class_name.split(" ")
        # confidence_score = prediction[0][index]
        return send_className[1]
