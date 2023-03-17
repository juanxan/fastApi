from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class ProductoDTO(BaseModel):   
    
    producto_id: Optional[int] = None
    producto_fecha: date = Field()
    producto_fecha_modificacion: date = Field()
    producto_estado: bool = Field()
    producto_nombre: str = Field(min_length=5, max_length=150)
    producto_descripcion: str = Field(min_length=5, max_length=350)
    producto_codigo: str = Field(min_length=5, max_length=100)
    producto_cod_barras: str = Field(min_length=5, max_length=100)
    producto_comision: float = Field(ge=1, le=10)
    producto_iva: float = Field(ge=1, le=10)
    producto_subtotal: float = Field(ge=1, le=10)

    class Config:
        schema_extra = {
            "example": {
                "producto_id": "a",
                "producto_fecha": date,
                "producto_fecha_modificacion": date,
                "producto_estado": True,
                "producto_nombre": "manzana",
                "producto_descripcion": "",
                "producto_codigo": "1111",
                "producto_cod_barras": "111",
                "producto_comision": 1,
                "producto_iva": 1,
                "producto_subtotal": 1
            }
        }