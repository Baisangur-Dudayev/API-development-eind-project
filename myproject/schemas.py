from pydantic import BaseModel, Field

#Book classen
class BookBase(BaseModel):
    title: str = Field(..., max_length=50)
    description: str | None = Field(None, max_length=500)
    publication_date: str = Field(..., regex=r'\d{2}/\d{2}/\d{4}', description='Publication date in day/month/year format (DD/MM/YYYY)')
    genre: str = Field(..., max_length=50)

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True

#PenName classen
class PenNameBase(BaseModel):
    pen_name: str = Field(..., max_length=50)

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
    password: str = Field(..., min_length=8)

class Author(AuthorBase):
    id: int
    is_active: bool
    #om classen Book & PenName hier te gebruiken moeten ze boven boven deze classen gedefinieerd staan
    books: list[Book] = []
    pen_names: list[PenName] = []

    class Config:
        orm_mode = True

