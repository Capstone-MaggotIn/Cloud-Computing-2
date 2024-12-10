from flask import Flask
from app.services.loadModel import loadModel

cached_model = None

def init_model(app: Flask):
    global cached_model
    print("Initializing model...")

    if cached_model is None:
        try:
            cached_model = loadModel()
            print("Model loaded successfully.")
        except Exception as error:
            print(f"Error loading model: {error}")
            raise error
    else:
        print("Model already loaded, using cached model.")

    app.config['model'] = cached_model
