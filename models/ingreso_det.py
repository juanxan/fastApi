from config.database import Base
from sqlalchemy import Table, Column, Integer, String,Float,Date,Boolean,ForeignKey
from sqlalchemy.orm import mapper,relationship

class IngresoDet(Base):
    __tablename__ = "ingreso_det"
    
    ingreso_det_id = Column(Integer, primary_key=True)
    ingreso_det_fecha = Column(Date)
    ingreso_det_comision = Column(Float(precision=2), nullable=False)
    ingreso_det_iva = Column(Float(precision=2), nullable=False)
    ingreso_det_precio = Column(Float(precision=2), nullable=False)
    ingreso_det_cantidad = Column(Float(precision=2), nullable=False)
    
    producto_id = Column(Integer, ForeignKey("producto.producto_id"), nullable=False)
    producto = relationship('ProductoModel', back_populates="ingreso_det")
    
    ingreso_id = Column(Integer, ForeignKey("ingreso.ingreso_id"), nullable=False)
    ingreso = relationship("Ingreso", back_populates="ingreso_det")