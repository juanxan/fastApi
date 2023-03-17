from config.database import Base
from sqlalchemy import Table, Column, Integer, String,Float,Date,Boolean
from sqlalchemy.orm import mapper,relationship

class Zona(Base):
    __tablename__ = "zona"
    
    zona_id = Column(Integer, primary_key=True)
    zona_fecha = Column(Date)
    zona_fecha_modificacion = Column(Date)
    zona_estado = Column(Boolean)
    zona_nombre = Column(String(200), nullable=False)
    zona_descripcion = Column(String(350), nullable=False)
    zona_cod = Column(String(100), nullable=False)
    
    ingreso = relationship('Ingreso',uselist=False, back_populates="zona")   