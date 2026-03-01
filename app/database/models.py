from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import mapped_column
from app.database.database import Base
from pgvector.sqlalchemy import VECTOR
from app.database.enums import RatingType, Genres


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255), index=True)
    overview = Column(String(255), index = True)
    genre = Column(Enum(Genres), index= True)
    embedding = mapped_column(VECTOR(1536))
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), index=True)
    created_at = Column(DateTime, index=True)

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), index=True)
    rating_type = Column(Enum(RatingType), index=True)


