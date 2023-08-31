import strawberry
from typing import List, Type
from fastapi import Depends
from sqlalchemy.orm import Session

import models
from models import Post
# import models
# from types import PostType
from database import SessionLocal, engine
from graphql_types import PostType

models.Base.metadata.create_all(bind=engine)
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db = next(get_db())

# Query

@strawberry.type
class Query:
    @strawberry.field
    def posts(self) -> list[PostType]:
        
        posts = db.query(models.Post).all()
        return posts


# Mutation
@strawberry.type()
class Mutation:
    @strawberry.field
    def create_post(self, title: str, author: str, message: str) -> PostType:
        
        blog = models.Post(title=title, author=author, message=message)
        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog

    @strawberry.field
    def update_blogpost(self, id: int, title: str, author: str, message: str) -> PostType:
        blog = SessionLocal().query(models.Post).filter(models.Post.id == id).first()
        blog.title = title
        blog.author = author
        blog.message = message
        db.add(blog)
        db.commit()
        return blog

    @strawberry.field
    def delete_blogpost(self, id: int) -> bool:
        db.query(models.Post).filter(models.Post.id == id).delete()
        db.commit()
        return True


# Defined a Schema
final_schema = strawberry.Schema(query=Query, mutation=Mutation)
