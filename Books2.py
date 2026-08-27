from typing import Optional

from fastapi import FastAPI, Body
from ipykernel.datapub import publish_data
from pydantic import BaseModel, Field
app = FastAPI()

class Books:

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author": "codingwithomid",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2029
            }
        }
    }


BOOKS = [
    Books(1, "To Kill a Mockingbird", "Harper Lee", "A gripping tale of racial injustice and childhood innocence in the Deep South.", 5, 2030),
    Books(2, "1984", "George Orwell", "A dystopian masterpiece about totalitarianism, surveillance, and the loss of truth.", 5, 2030),
    Books(3, "Pride and Prejudice", "Jane Austen", "A witty exploration of love, class, and first impressions in Regency England.", 5, 2029),
    Books(4, "The Great Gatsby", "F. Scott Fitzgerald", "The tragic story of Jay Gatsby and his obsessive pursuit of the American Dream.", 4, 2028),
    Books(5, "Moby-Dick", "Herman Melville", "An epic tale of obsession as Captain Ahab hunts the white whale.", 4, 2027),
    Books(6, "The Catcher in the Rye", "J.D. Salinger", "A teenage boy's cynical journey through New York after being expelled from school.", 4, 2026),
    Books(7, "Brave New World", "Aldous Huxley", "A futuristic society engineered for happiness at the cost of individuality and freedom.", 5, 2021),
    Books(8, "The Hobbit", "J.R.R. Tolkien", "Bilbo Baggins embarks on an unexpected adventure with dwarves to reclaim a lost treasure.", 5, 2020),
    Books(9, "Fahrenheit 451", "Ray Bradbury", "In a future where books are banned, a fireman begins to question everything.", 5, 2002),
    Books(10, "Jane Eyre", "Charlotte Brontë", "An orphaned governess finds love and independence while uncovering dark secrets.", 5, 2009),
    Books(11, "The Lord of the Rings", "J.R.R. Tolkien", "A fellowship embarks on a perilous quest to destroy the One Ring and defeat Sauron.", 5, 2006),
    Books(12, "Animal Farm", "George Orwell", "A satirical allegory of a farm revolution that descends into tyranny.", 5, 2010),
    Books(13, "Wuthering Heights", "Emily Brontë", "A dark and passionate tale of love, revenge, and haunted hearts on the moors.", 4, 2011),
    Books(14, "The Odyssey", "Homer", "The epic journey of Odysseus as he struggles to return home after the Trojan War.", 5, 2025),
    Books(15, "Crime and Punishment", "Fyodor Dostoevsky", "A young man commits murder and grapples with guilt, morality, and redemption.", 5, 2020),
    Books(16, "The Picture of Dorian Gray", "Oscar Wilde", "A man remains forever young while his portrait ages and reveals his sins.", 4, 2021),
    Books(17, "Frankenstein", "Mary Shelley", "A scientist creates life and faces the devastating consequences of playing God.", 5, 2026),
    Books(18, "Dracula", "Bram Stoker", "The classic gothic tale of Count Dracula and those who try to stop him.", 4, 2001),
    Books(19, "The Adventures of Huckleberry Finn", "Mark Twain", "A boy and a runaway slave journey down the Mississippi River toward freedom.", 5, 2008),
    Books(20, "Les Misérables", "Victor Hugo", "An epic story of justice, redemption, and revolution in 19th-century France.", 5, 2023),
    Books(21, "The Brothers Karamazov", "Fyodor Dostoevsky", "A profound exploration of faith, doubt, and family conflict through three brothers.", 5, 2028),
    Books(22, "One Hundred Years of Solitude", "Gabriel García Márquez", "The multi-generational saga of the Buendía family in the mythical town of Macondo.", 5, 2030),
    Books(23, "The Alchemist", "Paulo Coelho", "A young shepherd follows his dreams and discovers the true meaning of life.", 4, 2020),
    Books(24, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "A young boy discovers he is a wizard and begins his magical education at Hogwarts.", 5, 2022),
    Books(25, "The Hunger Games", "Suzanne Collins", "In a dystopian future, a girl volunteers to fight in a televised battle to the death.", 4, 2025),
    Books(26, "The Handmaid's Tale", "Margaret Atwood", "A woman struggles to survive in a theocratic regime that controls women's bodies.", 5, 2024),
    Books(27, "Slaughterhouse-Five", "Kurt Vonnegut", "A soldier becomes unstuck in time while reflecting on the bombing of Dresden.", 5, 2019),
    Books(28, "Beloved", "Toni Morrison", "A former slave is haunted by the ghost of her dead child and the trauma of slavery.", 5, 2018),
    Books(29, "The Road", "Cormac McCarthy", "A father and son journey through a post-apocalyptic wasteland in search of hope.", 5, 2015),
    Books(30, "Life of Pi", "Yann Martel", "A boy survives a shipwreck and shares a lifeboat with a Bengal tiger.", 4, 2021),
    Books(31, "The Kite Runner", "Khaled Hosseini", "A story of friendship, betrayal, and redemption set against the backdrop of Afghanistan.", 5, 2018),
    Books(32, "A Game of Thrones", "George R.R. Martin", "Noble families fight for control of the Iron Throne in a land of ice and fire.", 5, 2002),
    Books(33, "The Name of the Wind", "Patrick Rothfuss", "A legendary hero recounts the story of his extraordinary life and magical education.", 5, 2023),
    Books(34, "Dune", "Frank Herbert", "On a desert planet, a young heir becomes the center of a galactic power struggle.", 5, 2025),
    Books(35, "Neuromancer", "William Gibson", "A washed-up hacker is hired for one last job in a world of cybernetics and AI.", 4, 2029),
    Books(36, "The Martian", "Andy Weir", "An astronaut is stranded on Mars and must use science to survive against all odds.", 5, 2023),
    Books(37, "Project Hail Mary", "Andy Weir", "A lone astronaut wakes up with amnesia and must save Earth from extinction.", 5, 2014),
    Books(38, "The Silent Patient", "Alex Michaelides", "A famous painter stops speaking after allegedly murdering her husband.", 4, 2026),
    Books(39, "Where the Crawdads Sing", "Delia Owens", "A mysterious girl raised in the marsh becomes a suspect in a small-town murder.", 4, 2011),
    Books(40, "Educated", "Tara Westover", "A woman raised in isolation by survivalist parents fights to gain an education.", 5, 2013),
    Books(41, "Atomic Habits", "James Clear", "A practical guide to building good habits and breaking bad ones through small changes.", 5, 2023),
    Books(42, "Sapiens", "Yuval Noah Harari", "A sweeping history of humankind from the Stone Age to the modern age.", 5, 2012),
    Books(43, "Thinking, Fast and Slow", "Daniel Kahneman", "A groundbreaking exploration of the two systems that drive the way we think.", 5, 2009),
    Books(44, "The Subtle Art of Not Giving a F*ck", "Mark Manson", "A counterintuitive approach to living a good life by caring about what truly matters.", 4, 2023),
    Books(45, "Normal People", "Sally Rooney", "The complicated relationship between two young people as they grow into adulthood.", 4, 2026),
    Books(46, "Circe", "Madeline Miller", "The story of the mythical witch Circe, who transforms from outcast to powerful sorceress.", 5, 2001),
    Books(47, "The Midnight Library", "Matt Haig", "A woman discovers a library between life and death where every book is a different life she could have lived.", 4, 2023),
    Books(48, "Klara and the Sun", "Kazuo Ishiguro", "An artificial friend observes the world and forms a unique bond with the human she serves.", 4, 2015),
    Books(49, "Piranesi", "Susanna Clarke", "A man lives in a vast, mysterious house filled with statues and tides, slowly uncovering its secrets.", 5, 2030),
    Books(50, "The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "A reclusive Hollywood icon finally tells the truth about her glamorous and scandalous life.", 5, 2028),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

@app.get("/books/publish/")
async def read_books_by_publish_date(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Books(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Books):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break