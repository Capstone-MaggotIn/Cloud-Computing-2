from flask import Blueprint
from app.server.handler import post_predict_handler

predict_routes = Blueprint('predict_routes', __name__)
predict_routes.add_url_rule('/predict', view_func=post_predict_handler, methods=['POST'])
