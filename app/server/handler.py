from flask import request, jsonify, current_app
from app.services.inferenceServices import predict_classification
from app.services.storeData import save_prediction_to_db
import uuid
from datetime import datetime

def post_predict_handler():
    try:
        image_file = request.files.get('image')
        if not image_file:
            return jsonify({"error": "No image file provided"}), 400

        image = image_file.read()

        model = current_app.config.get('model')
        if not model:
            return jsonify({"error": "Model not initialized"}), 500

        try:
            result = predict_classification(model, image)
        except RuntimeError as e:
            return jsonify({
                "status": "fail",
                "message": "An error occurred making a prediction. Please re-upload the image and try again."
            }), 400

        confidence_score = result['confidenceScore']
        result_integer = result['result']
        phase = result['phase']

        prediction_id = str(uuid.uuid4())
        created_at = datetime.utcnow().isoformat()

        save_prediction_to_db(prediction_id, result_integer, phase, confidence_score, created_at)

        data = {
            "id": prediction_id,
            "created_at": created_at,
            "result": result_integer,
            "phase": phase,
            "confidenceScore": confidence_score
        }

        message = (
            'Model is predicted successfully'
            if confidence_score > 75
            else 'Model predicted successfully but under threshold. Please use the correct picture.'
        )

        return jsonify({
            'status': "true",
            'message': message,
            'data': data
        }), 201

    except Exception as error:
        return jsonify({"error": str(error)}), 500
