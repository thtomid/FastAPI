from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
app = FastAPI()

class Books:

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


BOOKS = [
    Books(1, "To Kill a Mockingbird", "Harper Lee", "A gripping tale of racial injustice and childhood innocence in the Deep South.", 5),
    Books(2, "1984", "George Orwell", "A dystopian masterpiece about totalitarianism, surveillance, and the loss of truth.", 5),
    Books(3, "Pride and Prejudice", "Jane Austen", "A witty exploration of love, class, and first impressions in Regency England.", 5),
    Books(4, "The Great Gatsby", "F. Scott Fitzgerald", "The tragic story of Jay Gatsby and his obsessive pursuit of the American Dream.", 4),
    Books(5, "Moby-Dick", "Herman Melville", "An epic tale of obsession as Captain Ahab hunts the white whale.", 4),
    Books(6, "The Catcher in the Rye", "J.D. Salinger", "A teenage boy's cynical journey through New York after being expelled from school.", 4),
    Books(7, "Brave New World", "Aldous Huxley", "A futuristic society engineered for happiness at the cost of individuality and freedom.", 5),
    Books(8, "The Hobbit", "J.R.R. Tolkien", "Bilbo Baggins embarks on an unexpected adventure with dwarves to reclaim a lost treasure.", 5),
    Books(9, "Fahrenheit 451", "Ray Bradbury", "In a future where books are banned, a fireman begins to question everything.", 5),
    Books(10, "Jane Eyre", "Charlotte Brontë", "An orphaned governess finds love and independence while uncovering dark secrets.", 5),
    Books(11, "The Lord of the Rings", "J.R.R. Tolkien", "A fellowship embarks on a perilous quest to destroy the One Ring and defeat Sauron.", 5),
    Books(12, "Animal Farm", "George Orwell", "A satirical allegory of a farm revolution that descends into tyranny.", 5),
    Books(13, "Wuthering Heights", "Emily Brontë", "A dark and passionate tale of love, revenge, and haunted hearts on the moors.", 4),
    Books(14, "The Odyssey", "Homer", "The epic journey of Odysseus as he struggles to return home after the Trojan War.", 5),
    Books(15, "Crime and Punishment", "Fyodor Dostoevsky", "A young man commits murder and grapples with guilt, morality, and redemption.", 5),
    Books(16, "The Picture of Dorian Gray", "Oscar Wilde", "A man remains forever young while his portrait ages and reveals his sins.", 4),
    Books(17, "Frankenstein", "Mary Shelley", "A scientist creates life and faces the devastating consequences of playing God.", 5),
    Books(18, "Dracula", "Bram Stoker", "The classic gothic tale of Count Dracula and those who try to stop him.", 4),
    Books(19, "The Adventures of Huckleberry Finn", "Mark Twain", "A boy and a runaway slave journey down the Mississippi River toward freedom.", 5),
    Books(20, "Les Misérables", "Victor Hugo", "An epic story of justice, redemption, and revolution in 19th-century France.", 5),
    Books(21, "The Brothers Karamazov", "Fyodor Dostoevsky", "A profound exploration of faith, doubt, and family conflict through three brothers.", 5),
    Books(22, "One Hundred Years of Solitude", "Gabriel García Márquez", "The multi-generational saga of the Buendía family in the mythical town of Macondo.", 5),
    Books(23, "The Alchemist", "Paulo Coelho", "A young shepherd follows his dreams and discovers the true meaning of life.", 4),
    Books(24, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "A young boy discovers he is a wizard and begins his magical education at Hogwarts.", 5),
    Books(25, "The Hunger Games", "Suzanne Collins", "In a dystopian future, a girl volunteers to fight in a televised battle to the death.", 4),
    Books(26, "The Handmaid's Tale", "Margaret Atwood", "A woman struggles to survive in a theocratic regime that controls women's bodies.", 5),
    Books(27, "Slaughterhouse-Five", "Kurt Vonnegut", "A soldier becomes unstuck in time while reflecting on the bombing of Dresden.", 5),
    Books(28, "Beloved", "Toni Morrison", "A former slave is haunted by the ghost of her dead child and the trauma of slavery.", 5),
    Books(29, "The Road", "Cormac McCarthy", "A father and son journey through a post-apocalyptic wasteland in search of hope.", 5),
    Books(30, "Life of Pi", "Yann Martel", "A boy survives a shipwreck and shares a lifeboat with a Bengal tiger.", 4),
    Books(31, "The Kite Runner", "Khaled Hosseini", "A story of friendship, betrayal, and redemption set against the backdrop of Afghanistan.", 5),
    Books(32, "A Game of Thrones", "George R.R. Martin", "Noble families fight for control of the Iron Throne in a land of ice and fire.", 5),
    Books(33, "The Name of the Wind", "Patrick Rothfuss", "A legendary hero recounts the story of his extraordinary life and magical education.", 5),
    Books(34, "Dune", "Frank Herbert", "On a desert planet, a young heir becomes the center of a galactic power struggle.", 5),
    Books(35, "Neuromancer", "William Gibson", "A washed-up hacker is hired for one last job in a world of cybernetics and AI.", 4),
    Books(36, "The Martian", "Andy Weir", "An astronaut is stranded on Mars and must use science to survive against all odds.", 5),
    Books(37, "Project Hail Mary", "Andy Weir", "A lone astronaut wakes up with amnesia and must save Earth from extinction.", 5),
    Books(38, "The Silent Patient", "Alex Michaelides", "A famous painter stops speaking after allegedly murdering her husband.", 4),
    Books(39, "Where the Crawdads Sing", "Delia Owens", "A mysterious girl raised in the marsh becomes a suspect in a small-town murder.", 4),
    Books(40, "Educated", "Tara Westover", "A woman raised in isolation by survivalist parents fights to gain an education.", 5),
    Books(41, "Atomic Habits", "James Clear", "A practical guide to building good habits and breaking bad ones through small changes.", 5),
    Books(42, "Sapiens", "Yuval Noah Harari", "A sweeping history of humankind from the Stone Age to the modern age.", 5),
    Books(43, "Thinking, Fast and Slow", "Daniel Kahneman", "A groundbreaking exploration of the two systems that drive the way we think.", 5),
    Books(44, "The Subtle Art of Not Giving a F*ck", "Mark Manson", "A counterintuitive approach to living a good life by caring about what truly matters.", 4),
    Books(45, "Normal People", "Sally Rooney", "The complicated relationship between two young people as they grow into adulthood.", 4),
    Books(46, "Circe", "Madeline Miller", "The story of the mythical witch Circe, who transforms from outcast to powerful sorceress.", 5),
    Books(47, "The Midnight Library", "Matt Haig", "A woman discovers a library between life and death where every book is a different life she could have lived.", 4),
    Books(48, "Klara and the Sun", "Kazuo Ishiguro", "An artificial friend observes the world and forms a unique bond with the human she serves.", 4),
    Books(49, "Piranesi", "Susanna Clarke", "A man lives in a vast, mysterious house filled with statues and tides, slowly uncovering its secrets.", 5),
    Books(50, "The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "A reclusive Hollywood icon finally tells the truth about her glamorous and scandalous life.", 5),
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Books(**book_request.dict())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Books):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book