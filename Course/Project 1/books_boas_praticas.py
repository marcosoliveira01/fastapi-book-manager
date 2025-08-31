from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import unicodedata

app = FastAPI(title="Book API", description="API de livros com boas práticas FastAPI", version="1.0")

# Função auxiliar para normalizar strings (insensível a maiúsculas, acentos e espaços)
def normalize(text: str) -> str:
    return unicodedata.normalize("NFKD", text.strip()).casefold()

# Pydantic model
class Book(BaseModel):
    title: str
    author: str
    category: str

# Lista de livros (in-memory)
BOOKS: List[Book] = [
    Book(title='Title One', author='Author One', category='science'),
    Book(title='Title Two', author='Author Two', category='science'),
    Book(title='Title Three', author='Author Three', category='history'),
    Book(title='Title Four', author='Author Four', category='math'),
    Book(title='Title Five', author='Author Five', category='math'),
    Book(title='Title Six', author='Author Two', category='math')
]

# =====================
# GET - Todos os livros
# =====================
@app.get("/books", response_model=List[Book])
async def read_all_books():
    return BOOKS

# =====================
# GET - Livro por título
# =====================
@app.get("/books/{book_title}", response_model=Book)
async def read_book(book_title: str):
    for book in BOOKS:
        if normalize(book.title) == normalize(book_title):
            return book
    raise HTTPException(status_code=404, detail=f"Book '{book_title}' not found")

# =====================
# GET - Livros por categoria (query param)
# =====================
@app.get("/books/category/", response_model=List[Book])
async def read_category_by_query(category: str):
    result = [book for book in BOOKS if normalize(book.category) == normalize(category)]
    if not result:
        raise HTTPException(status_code=404, detail=f"No books found in category '{category}'")
    return result

# =====================
# GET - Livros por autor (query param)
# =====================
@app.get("/books/byauthor/", response_model=List[Book])
async def read_books_by_author(author: str):
    result = [book for book in BOOKS if normalize(book.author) == normalize(author)]
    if not result:
        raise HTTPException(status_code=404, detail=f"No books found by author '{author}'")
    return result

# =====================
# GET - Livros por autor e categoria
# =====================
@app.get("/books/{book_author}/category/", response_model=List[Book])
async def read_author_category_by_query(book_author: str, category: str):
    result = [
        book for book in BOOKS
        if normalize(book.author) == normalize(book_author) and normalize(book.category) == normalize(category)
    ]
    if not result:
        raise HTTPException(
            status_code=404,
            detail=f"No books found by '{book_author}' in category '{category}'"
        )
    return result

# =====================
# POST - Criar livro
# =====================
@app.post("/books/create_book", response_model=Book, status_code=201)
async def create_book(new_book: Book = Body(...)):
    # Evita duplicatas pelo título
    for book in BOOKS:
        if normalize(book.title) == normalize(new_book.title):
            raise HTTPException(status_code=400, detail=f"Book '{new_book.title}' already exists")
    BOOKS.append(new_book)
    return new_book

# =====================
# PUT - Atualizar livro
# =====================
@app.put("/books/update_book", response_model=Book)
async def update_book(update_book: Book = Body(...)):
    for i, book in enumerate(BOOKS):
        if normalize(book.title) == normalize(update_book.title):
            BOOKS[i] = update_book
            return update_book
    raise HTTPException(status_code=404, detail=f"Book '{update_book.title}' not found")

# =====================
# DELETE - Deletar livro
# =====================
@app.delete("/books/delete_book/{book_title}", status_code=204)
async def delete_book(book_title: str):
    for i, book in enumerate(BOOKS):
        if normalize(book.title) == normalize(book_title):
            BOOKS.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Book '{book_title}' not found")
