from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from app.server.routes import predict_routes 
from app.services.initModel import init_model

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Konfigurasi CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Panggil init_model saat aplikasi diinisialisasi
init_model(app)

# Menambahkan blueprint ke aplikasi Flask
app.register_blueprint(predict_routes)

# Menangani error dan mengubah respons jika terjadi error
@app.after_request
def after_request(response):
    if response.status_code >= 400:
        try:
            original_data = response.get_json()  # Ambil respons JSON asli
        except Exception:
            original_data = {"message": "An error occurred"}  # Default jika tidak ada JSON

        # Ubah format respons JSON dengan status fail
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

# Route default
@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "message": "Service is running"
    }, 200

if __name__ == "__main__":
    app.run(host="localhost", port=3000, debug=True, use_reloader=False)  # Disable reloader
