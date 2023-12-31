from pydantic import BaseModel, Field

#Book classen
class BookBase(BaseModel):
    title: str
    description: str | None = None
    publication_date: str
    genre: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

#PenName classen
class PenNameBase(BaseModel):
    pen_name: str

class PenNameCreate(PenNameBase):
    pass

class PenName(PenNameBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

#Author classen
class AuthorBase(BaseModel):
    email: str = Field(
        ...,
        regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
        description='Valid email address'
    )
    first_name: str | None = Field(None, max_length=50)
    last_name: str | None = Field(None, max_length=50)
    place_of_birth: str | None = Field(None, max_length=50)
    biography: str | None = Field(None, max_length=50)

class AuthorCreate(AuthorBase):
    password: str

class Author(AuthorBase):
    id: int
    is_active: bool
    #om classen Book & PenName hier te gebruiken moeten ze boven boven deze classen gedefinieerd staan
    books: list[Book] = []
    pen_names: list[PenName] = []

    class Config:
        orm_mode = True

