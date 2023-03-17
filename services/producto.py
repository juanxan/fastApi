from models.producto import ProductoModel
from schemas.producto import ProductoDTO


class ProductoService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(ProductoModel).all()
        return result

    def get_movie_by_id(self, id):
        result = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()
        return result

    def create_movie(self, movie: ProductoDTO):
        new_movie = ProductoModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return
