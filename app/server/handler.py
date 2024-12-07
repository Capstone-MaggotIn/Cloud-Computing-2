from flask import request, jsonify, current_app
from app.services.inferenceServices import predict_classification
import uuid
from datetime import datetime

def post_predict_handler():
    try:
        # Ambil file gambar dari request
        image_file = request.files['image']
        if not image_file:
            return jsonify({"error": "No image file provided"}), 400
        
        # Baca file gambar sebagai byte stream
        image = image_file.read()

        # Ambil model yang sudah dimuat
        model = current_app.config.get('model')
        if not model:
            return jsonify({"error": "Model not initialized"}), 500

        # Prediksi dengan model
        result = predict_classification(model, image)
        confidence_score = result['confidence score']
        label = result['label']

        # Generate unique ID dan timestamp
        prediction_id = str(uuid.uuid4())
        created_at = datetime.utcnow().isoformat()

        # Data respons
        data = {
            "id": prediction_id,
            "created_at": created_at,
            "result": label
        }

        # Pesan respons
        message = (
            'Model predicted successfully.'
            if confidence_score > 99
            else 'Model predicted successfully but under threshold. Please use the correct picture.'
        )

        # Return JSON respons
        response = {
            'status': 'success',
            'message': message,
            'data': data
        }

        return response, 201

    except Exception as error:
        return jsonify({"error": str(error)}), 500