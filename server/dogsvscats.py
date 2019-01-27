import io
import json
import numpy as np
from keras.models import load_model
from PIL import Image
from PIL.ImageOps import fit

DOGSVSCATS_MODEL = load_model('dogsvscats.h5')
animal_array = ['cat', 'dog']


def post_image(file):
    image = Image.open(io.BytesIO(file.read()))
    image = fit(image, (50, 50))
    image_bytes = image.tobytes()
    image_array = np.reshape(np.frombuffer(image_bytes,  dtype=np.uint8), (1, 50, 50, 3))
    prediction = DOGSVSCATS_MODEL.predict(image_array)
    print(prediction[0][0])
    return json.dumps({'animal': animal_array[int(prediction[0][0])]})
