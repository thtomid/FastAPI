from fastapi import FastAPI, Body

app = FastAPI()

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction", "price": 12.99, "in_stock": True},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction", "price": 14.99, "in_stock": True},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Science Fiction", "price": 11.99, "in_stock": True},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance", "price": 9.99, "in_stock": False},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Fiction", "price": 10.99, "in_stock": True},
    {"id": 6, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "genre": "Fantasy", "price": 15.99, "in_stock": True},
    {"id": 7, "title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "genre": "Science Fiction", "price": 12.49, "in_stock": False},
    {"id": 8, "title": "Jane Eyre", "author": "Charlotte Bronte", "year": 1847, "genre": "Romance", "price": 8.99, "in_stock": True},
    {"id": 9, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954, "genre": "Fantasy", "price": 29.99, "in_stock": True},
    {"id": 10, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997, "genre": "Fantasy", "price": 19.99, "in_stock": True},
    {"id": 11, "title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "genre": "Fiction", "price": 13.99, "in_stock": True},
    {"id": 12, "title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003, "genre": "Mystery", "price": 16.99, "in_stock": False},
    {"id": 13, "title": "The Hunger Games", "author": "Suzanne Collins", "year": 2008, "genre": "Science Fiction", "price": 14.49, "in_stock": True},
    {"id": 14, "title": "The Kite Runner", "author": "Khaled Hosseini", "year": 2003, "genre": "Fiction", "price": 12.99, "in_stock": True},
    {"id": 15, "title": "The Book Thief", "author": "Markus Zusak", "year": 2005, "genre": "Historical Fiction", "price": 11.49, "in_stock": False},
    {"id": 16, "title": "The Chronicles of Narnia", "author": "C.S. Lewis", "year": 1950, "genre": "Fantasy", "price": 22.99, "in_stock": True},
    {"id": 17, "title": "The Shining", "author": "Stephen King", "year": 1977, "genre": "Horror", "price": 13.99, "in_stock": True},
    {"id": 18, "title": "Gone with the Wind", "author": "Margaret Mitchell", "year": 1936, "genre": "Historical Fiction", "price": 18.99, "in_stock": False},
    {"id": 19, "title": "The Little Prince", "author": "Antoine de Saint-Exupery", "year": 1943, "genre": "Fiction", "price": 7.99, "in_stock": True},
    {"id": 20, "title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "year": 2005, "genre": "Mystery", "price": 15.49, "in_stock": True},
    {"id": 21, "title": "The Help", "author": "Kathryn Stockett", "year": 2009, "genre": "Historical Fiction", "price": 13.99, "in_stock": True},
    {"id": 22, "title": "The Fault in Our Stars", "author": "John Green", "year": 2012, "genre": "Young Adult", "price": 11.99, "in_stock": False},
    {"id": 23, "title": "The Maze Runner", "author": "James Dashner", "year": 2009, "genre": "Science Fiction", "price": 12.49, "in_stock": True},
    {"id": 24, "title": "The Notebook", "author": "Nicholas Sparks", "year": 1996, "genre": "Romance", "price": 10.49, "in_stock": True},
    {"id": 25, "title": "The Secret Garden", "author": "Frances Hodgson Burnett", "year": 1911, "genre": "Children's", "price": 6.99, "in_stock": True},
    {"id": 26, "title": "The Adventures of Sherlock Holmes", "author": "Arthur Conan Doyle", "year": 1892, "genre": "Mystery", "price": 9.99, "in_stock": True},
    {"id": 27, "title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "year": 1844, "genre": "Historical Fiction", "price": 16.99, "in_stock": False},
    {"id": 28, "title": "The Three Musketeers", "author": "Alexandre Dumas", "year": 1844, "genre": "Historical Fiction", "price": 14.99, "in_stock": True},
    {"id": 29, "title": "War and Peace", "author": "Leo Tolstoy", "year": 1869, "genre": "Historical Fiction", "price": 24.99, "in_stock": True},
    {"id": 30, "title": "Anna Karenina", "author": "Leo Tolstoy", "year": 1877, "genre": "Fiction", "price": 19.99, "in_stock": False},
    {"id": 31, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "year": 1866, "genre": "Fiction", "price": 15.99, "in_stock": True},
    {"id": 32, "title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "year": 1880, "genre": "Fiction", "price": 21.99, "in_stock": True},
    {"id": 33, "title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "genre": "Fiction", "price": 17.99, "in_stock": True},
    {"id": 34, "title": "The Odyssey", "author": "Homer", "year": -800, "genre": "Classics", "price": 11.99, "in_stock": True},
    {"id": 35, "title": "The Iliad", "author": "Homer", "year": -750, "genre": "Classics", "price": 12.99, "in_stock": False},
    {"id": 36, "title": "The Divine Comedy", "author": "Dante Alighieri", "year": 1321, "genre": "Classics", "price": 14.99, "in_stock": True},
    {"id": 37, "title": "Hamlet", "author": "William Shakespeare", "year": 1603, "genre": "Classics", "price": 8.99, "in_stock": True},
    {"id": 38, "title": "Macbeth", "author": "William Shakespeare", "year": 1606, "genre": "Classics", "price": 8.49, "in_stock": True},
    {"id": 39, "title": "Romeo and Juliet", "author": "William Shakespeare", "year": 1597, "genre": "Classics", "price": 7.99, "in_stock": True},
    {"id": 40, "title": "Don Quixote", "author": "Miguel de Cervantes", "year": 1605, "genre": "Classics", "price": 18.99, "in_stock": False},
    {"id": 41, "title": "The Art of War", "author": "Sun Tzu", "year": -500, "genre": "Philosophy", "price": 9.99, "in_stock": True},
    {"id": 42, "title": "Meditations", "author": "Marcus Aurelius", "year": 180, "genre": "Philosophy", "price": 10.99, "in_stock": True},
    {"id": 43, "title": "The Republic", "author": "Plato", "year": -380, "genre": "Philosophy", "price": 11.99, "in_stock": True},
    {"id": 44, "title": "Sapiens", "author": "Yuval Noah Harari", "year": 2011, "genre": "Non-Fiction", "price": 16.99, "in_stock": True},
    {"id": 45, "title": "Sapiens", "author": "Richard Dawkins", "year": 1976, "genre": "Science", "price": 14.99, "in_stock": True},
    {"id": 46, "title": "A Brief History of Time", "author": "Stephen Hawking", "year": 1988, "genre": "Science", "price": 15.49, "in_stock": False},
    {"id": 47, "title": "The Origin of Species", "author": "Charles Darwin", "year": 1859, "genre": "Science", "price": 17.99, "in_stock": True},
    {"id": 48, "title": "The Wealth of Nations", "author": "Adam Smith", "year": 1776, "genre": "Economics", "price": 19.99, "in_stock": True},
    {"id": 49, "title": "The Communist Manifesto", "author": "Karl Marx", "year": 1848, "genre": "Political Science", "price": 6.99, "in_stock": True},
    {"id": 50, "title": "The Theory of Everything", "author": "Stephen Hawking", "year": 2002, "genre": "Science", "price": 13.99, "in_stock": True}
]

@app.get("/books")
async def read_all_books():
    return books

@app.get("/books/{title}")
async def read_book(title: str):
    for book in books:
        if book["title"].casefold() == title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(year: int):
    books_to_return = []
    for book in books:
        if book.get('year') == year:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{author}/")
async def read_category_by_query(author: str, title: str):
    books_to_return = []
    for book in books:
        if (book.get("author").casefold() == author.casefold() and
                book.get("title").casefold() == title.casefold()):
            books_to_return.append(book)
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    books.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(books)):
        books[i] = updated_book