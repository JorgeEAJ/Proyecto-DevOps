from . import db
from datetime import datetime

class Item(db.Model):
    __tablename__ = 'items'  # Igual que en tu CREATE TABLE

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Tamaño coincide con VARCHAR(100)
    description = db.Column(db.Text)  # Para el campo description
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # DEFAULT CURRENT_TIMESTAMP
