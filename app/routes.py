from flask import Blueprint, request, jsonify
from models import db, Patient

bp = Blueprint('api', __name__)

@bp.route('/patients', methods=['POST'])
def add():
    data = request.get_json()
    patient = Patient(**data)
    db.session.add(patient)
    db.session.commit()
    return jsonify({'id': patient.id}), 201

@bp.route('/patients/<int:id>', methods=['GET'])
def get(id):
    p = Patient.query.get_or_404(id)
    return jsonify({c.name: getattr(p, c.name) for c in p.__table__.columns})

@bp.route('/patients/<int:id>', methods=['PUT'])
def update(id):
    p = Patient.query.get_or_404(id)
    for key, value in request.get_json().items():
        setattr(p, key, value)
    db.session.commit()
    return jsonify({'message': 'updated'})

@bp.route('/patients/<int:id>', methods=['DELETE'])
def delete(id):
    p = Patient.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({'message': 'deleted'})

@bp.route('/patients', methods=['GET'])
def list_all():
    patients = Patient.query.all()
    return jsonify([{c.name: getattr(p, c.name) for c in p.__table__.columns} for p in patients])

