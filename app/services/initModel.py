# initModel.py
from flask import Flask
from app.services.loadModel import loadModel

# Global cache for the model
cached_model = None

def init_model(app: Flask):
    global cached_model
    print("Initializing model...")

    if cached_model is None:
        try:
            # Load model if it hasn't been cached
            cached_model = loadModel()
            print("Model loaded successfully.")
        except Exception as error:
            print(f"Error loading model: {error}")
            raise error
    else:
        print("Model already loaded, using cached model.")

    # Attach the cached model to the app config
    app.config['model'] = cached_model
