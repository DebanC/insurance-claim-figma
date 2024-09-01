from flask import Blueprint, request, jsonify
from models import db, Claim

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/api/claims/submit', methods=['POST'])
def submit_claim():
    data = request.json
    user_name = data.get('user_name')
    email = data.get('email')
    claim_details = data.get('claim_details')
    
    new_claim = Claim(user_name=user_name, email=email, claim_details=claim_details)
    db.session.add(new_claim)
    db.session.commit()

    return jsonify({"message": "Claim submitted successfully", "claim_id": new_claim.id}), 201

@user_bp.route('/api/claims/status/<int:claim_id>', methods=['GET'])
def view_claim_status(claim_id):
    claim = Claim.query.get(claim_id)
    if not claim:
        return jsonify({"error": "Claim not found"}), 404
    return jsonify({"claim_id": claim.id, "status": claim.status})
