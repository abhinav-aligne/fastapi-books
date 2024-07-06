from fastapi import FastAPI

app = FastAPI()

# @app.get("/api-endpoint")
# def first_api():
#     return {'message' : 'Hello Abhinav'}

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS


#Path parameter
@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').lower() == book_title.lower():
            return book
        
#Query parameter
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


#HTTP Request POST METHOD
from fastapi import Body
@app.post("/create_book/")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

#HTTP Request PUT METHOD
@app.put("/books/update_book")
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == update_book.get("title").casefold():
            BOOKS[i] = update_book

#HTTP Request DELETE METHOD
@app.delete("/books/delete_book/{delete_param}")
async def delete_book(delete_param:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').lower() == delete_param.lower():
            BOOKS.pop(i)
            break

# Fetching Author using Path parameter
@app.get('/books/byauthor/{author_param}')
async def author_fetch(author_param:str):
    author_file = []
    for book in BOOKS:
        if book.get("author").lower() == author_param.lower():
            author_file.append(book)
    return author_file

