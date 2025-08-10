from flask import Blueprint, jsonify
from .models import Item
from . import db
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from flask import Response

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@bp.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@bp.route("/items")
def get_items():
    items = Item.query.all()
    return jsonify([
        {
            "id": i.id,
            "name": i.name,
            "description": i.description,
            "created_at": i.created_at.isoformat() if i.created_at else None
        }
        for i in items
    ])
# Nuevo endpoint para recibir alertas de Alertmanager
@bp.route("/alertas", methods=["POST"])
def recibir_alerta():
    """
    Endpoint para recibir las alertas enviadas por Alertmanager.
    """
    data = request.json  # El Alertmanager envía un JSON con las alertas
    print("📢 Alerta recibida desde Alertmanager:", data)

    # Aquí podrías:
    # 1. Guardar la alerta en la base de datos
    # 2. Enviar notificación a un frontend (WebSocket, SSE, etc.)
    # 3. Disparar otra acción (email, Slack, etc.)

    return jsonify({"status": "ok", "mensaje": "Alerta recibida"}), 200