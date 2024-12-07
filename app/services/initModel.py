from flask import Flask
from app.services.loadModel import loadModel 

app = Flask(__name__)
def init_model():
    print("Initializing model...")
    try:
        # Load model and assign it to app.model
        app.config['model'] = loadModel()
        print("Model loaded successfully")
    except Exception as error:
        print(f"Error loading model: {error}")
