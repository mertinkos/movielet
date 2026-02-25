from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import mapped_column 
from database import Base
from pgvector.sqlalchemy import VECTOR
from enums import RatingType, Genres

class Movie(Base):
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255), index=True)
    overview = Column(String(255), index = True)
    genre = Column(Genres, index= True)
    embedding = mapped_column(VECTOR(1536))
    
class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    email = Column(String(255), index=True)
    created_at = Column(DateTime, index=True)

class Rating(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(User.id, index=True)
    movie_id = Column(Movie.id, index=True)
    rating_type = Column(RatingType, index=True)

