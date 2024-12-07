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
init_model()

# Menambahkan blueprint ke aplikasi Flask
app.register_blueprint(predict_routes)

# Menangani error dan mengubah respons jika terjadi error
@app.after_request
def after_request(response):
    """
    Fungsi untuk menangani respons setelah request selesai diproses.
    Menambahkan logika error handling jika ada kesalahan.
    """
    if response.status_code >= 400:
        # Menangani error dan mengubah respons jika statusnya 4xx atau 5xx
        return jsonify({
            "status": "fail",
            "message": response.get_data(as_text=True)  # Menyertakan pesan error
        }), response.status_code
    return response

# Route default
@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "message": "Service is running"
    }, 200

if __name__ == "__main__":
    # Menjalankan server
    app.run(host="localhost", port=3000, debug=True)