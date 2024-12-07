import tensorflow as tf
import numpy as np

def predict_classification(model, image):
  tensor = tf.image.decode_image(image, channels = 3)
  tensor = tf.image.resize(tensor, [128, 128])
  tensor = tf.expand_dims(tensor, axis = 0)
  tensor = tf.image.convert_image_dtype(tensor, tf.float32)
  
  #prediksi
  prediction = model.predict(tensor)
  score = prediction[0]
  confidence_score = np.max(score) * 100
  
  #label kelas
  classes = ['Larva Tahap 1', 'Larva Tahap 2', 'Larva Tahap 3', 'Maggot', 'Prepupa', 'Pupa']
  
  #mendapatkan prediksi kelas dan label
  class_result = np.argmax(score)
  label = classes[class_result]
  
  return {
    'confidence score': confidence_score,
    'label': label
  }