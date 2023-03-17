from config.database import Base
from sqlalchemy import Column, Integer, String,Float,Date,Boolean,ForeignKey
from sqlalchemy.orm import relationship


class ProductoModel(Base):
    __tablename__ = "producto"
    
    producto_id = Column(Integer, primary_key=True)
    producto_fecha = Column(Date)
    producto_fecha_modificacion = Column(Date)
    producto_estado = Column(Boolean)
    producto_nombre = Column(String(150), nullable=False)
    producto_descripcion = Column(String(350), nullable=True)
    producto_codigo = Column(String(100), nullable=True)
    producto_cod_barras = Column(String(100), nullable=True)
    producto_comision = Column(Float(precision=2), nullable=False)
    producto_iva = Column(Float(precision=2), nullable=False)
    producto_subtotal = Column(Float(precision=2), nullable=False)
    
    ingreso_det = relationship("IngresoDet", uselist=False, back_populates="producto")   