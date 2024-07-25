from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

# Ensure that your class names are sorted
class_names = [
    "A", "B", "C", "D", "DELAPAN", "DUA", "E", "EMPAT", "ENAM", "F", "G", "H",
    "I", "J", "K", "L", "LIMA", "M", "N", "NOL", "O", "P", "Q", "R", "S", "SATU",
    "SEMBILAN", "SEPULUH", "T", "TIGA", "TUJUH", "U", "V", "W", "X", "Y", "Z"
]

# Load the model
model = tf.keras.models.load_model('model-lama.h5')  # Ganti dengan path model yang tepat

def predict(img):
    img = img.resize((100, 100))  # Resize image to match model input size
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)
    return predicted_class, confidence
