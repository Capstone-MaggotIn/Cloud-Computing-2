import os
from dotenv import load_dotenv
import tensorflow as tf
import requests

load_dotenv()

def loadModel():
    model_url = os.getenv("MODEL_URL")
    local_model_path = './temp_model.h5'  

    try:
        response = requests.get(model_url)
        response.raise_for_status()
        
        with open(local_model_path, 'wb') as f:
            f.write(response.content)

        model = tf.keras.models.load_model(local_model_path)
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise
