import os
from dotenv import load_dotenv
import tensorflow as tf

load_dotenv()

async def loadModel():

  model_path = os.getenv("MODEL_URL")
  model = tf.keras.models.load_model(model_path)
  return model