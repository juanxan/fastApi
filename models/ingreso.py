from config.database import Base
from sqlalchemy import Table, Column, Integer, String,Float,Date,Boolean,ForeignKey
from sqlalchemy.orm import relationship

class Ingreso(Base):
    __tablename__ = "ingreso"
    
    ingreso_id = Column(Integer, primary_key=True)
    ingreso_fecha = Column(Date)
    ingreso_estado = Column(Boolean)
    ingreso_cod_factura = Column(String(100), nullable=False)
    ingreso_tipo = Column(String(150), nullable=False)
    ingreso_comision = Column(Float(precision=2), nullable=False)
    ingreso_total_comision = Column(Float(precision=2), nullable=False)
    ingreso_iva = Column(Float(precision=2), nullable=False)
    ingreso_total_iva = Column(Float(precision=2), nullable=False)
    ingreso_subtotal = Column(Float(precision=2), nullable=False)
    ingreso_total = Column(Float(precision=2), nullable=False)
    ingreso_descuento = Column(Float(precision=2), nullable=False)
    ingreso_valor_ingreso = Column(Float(precision=2), nullable=False)
    ingreso_fiado = Column(Float(precision=2), nullable=False)
    
    ingreso_det = relationship("IngresoDet", uselist=True, back_populates="ingreso")    
    
    zona_id = Column(Integer, ForeignKey("zona.zona_id"), nullable=False)
    zona = relationship('Zona', back_populates="ingreso")