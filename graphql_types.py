import strawberry



@strawberry.type
class PostType:
    id: int
    title: str
    author: str
    message: str
