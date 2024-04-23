from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vendor_sweets = relationship("VendorSweet", back_populates="vendor", cascade="all, delete")

class Sweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    vendor_sweets = relationship("VendorSweet", back_populates="sweet", cascade="all, delete")

class VendorSweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    vendor = relationship("Vendor", back_populates="vendor_sweets")
    sweet = relationship("Sweet", back_populates="vendor_sweets")
