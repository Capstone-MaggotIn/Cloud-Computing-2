import tensorflow as tf
import numpy as np

def preprocess_image(image):
    """
    Preprocess the input image to match the model's expected input format.
    """
    tensor = tf.image.decode_image(image, channels=3)  # Decode image as RGB
    tensor = tf.image.resize(tensor, [128, 128])       # Resize to the expected input size
    tensor = tf.cast(tensor, tf.float32) / 255.0       # Normalize pixel values to [0, 1]
    tensor = tf.expand_dims(tensor, axis=0)            # Add batch dimension
    return tensor

def predict_classification(model, image):
    """
    Predict the classification of the uploaded image.
    """
    try:
        tensor = preprocess_image(image)
        prediction = model.predict(tensor)             # Predict using the model
        score = prediction[0]
        confidence_score = float(np.max(score) * 100)

        # Map prediction to class labels
        classes = ['Larva Tahap 1', 'Larva Tahap 2', 'Larva Tahap 3', 'Maggot', 'Prepupa', 'Pupa']
        class_result = int(np.argmax(score))
        label = classes[class_result]

        # If confidence score is below threshold, raise error
        if confidence_score < 50:  # Adjust threshold as needed
            raise ValueError("Low confidence in prediction")

        result_integer = class_result + 1  # Convert to 1-based index for integer result

        return {
            'confidenceScore': confidence_score,
            'result': result_integer,
            'phase': label
        }
    except ValueError as e:
        raise RuntimeError(f"Prediction error: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during prediction: {e}")
