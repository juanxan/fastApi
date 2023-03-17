from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List
from config.database import Session
from models.producto import ProductoModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.producto import ProductoService
from schemas.producto import ProductoDTO

producto_router = APIRouter()

@producto_router.get('/productos', tags=['productos'], response_model=List[ProductoDTO], status_code=200)
def get_movies() -> List[ProductoDTO]:
    db = Session()
    result = ProductoService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@producto_router.get('/productos/{id}', tags=['productos'], response_model=ProductoDTO)
def get_movie_by_id(id: int = Path(ge=1, le=2000)) -> ProductoDTO:
    db = Session()
    result = ProductoService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@producto_router.post('/productos', tags=['productos'], response_model=dict, status_code=201)
def create_movie(producto: ProductoDTO) -> dict:
    db = Session()
    ProductoService(db).create_movie(producto)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el producto"})

