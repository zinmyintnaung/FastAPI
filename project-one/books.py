from fastapi import Body, FastAPI

app = FastAPI()

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

# Example of dynamic path params
@app.get("/books/{book_title}")
async def read_title_by_path(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
# Example of query params, /books/?category=math
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Example of fixed path param with query param, get all books from a specific author using 
# /books/byauthor/?author=author%20two
@app.get("/books/byauthor/")
async def read_book_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

# Example of dynamic path with query params, get category of book by author
# /books/author%20two/?category=math
@app.get("/books/{author}/")
async def read_author_category_by_query(author: str, category: str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

# Example of POST request
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

# Example of PUT request
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
    return updated_book

# Example of DELETE request
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
    return book_title + ' is deleted.'
