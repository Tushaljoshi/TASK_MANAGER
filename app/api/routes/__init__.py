from flask import Blueprint

api_bp = Blueprint('api', __name__)

@api_bp.route('/health')
def health():
    return {"status": "running"}, 200

