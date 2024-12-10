from flask import Flask, jsonify, make_response
from flask_cors import CORS
from dotenv import load_dotenv
from app.server.routes import predict_routes 
from app.services.initModel import init_model

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

init_model(app)

app.register_blueprint(predict_routes)

@app.after_request
def after_request(response):
    if response.status_code >= 400:
        try:
            original_data = response.get_json()  
        except Exception:
            original_data = {"message": "An error occurred"} 

        response = make_response(
            jsonify(
                {
                    "status": "fail",
                    "message": original_data.get("message", "An error occurred"),
                }
            ),
            response.status_code,
        )
    return response

@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "message": "Service is running"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)  # Disable reloader
