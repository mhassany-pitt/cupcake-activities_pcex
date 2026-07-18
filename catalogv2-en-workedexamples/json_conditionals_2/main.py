import json


book_data = [
        {"_id": 1, "title": "The Great Adventure", "genre": "Fiction", "pages": 350},
        {"_id": 2, "title": "Science 101", "genre": "Non-Fiction", "pages": 250},
        {"_id": 3, "title": "Mystery Night", "genre": "Fiction", "pages": 290},
        {"_id": 4, "title": "Epic Saga", "genre": "Fiction", "pages": 450},
]


long_fiction_books = []

for book in book_data:
        if book["genre"] == "Fiction" and book["pages"] > 300:
                long_fiction_books.append(book["title"])

# Display result
print(long_fiction_books)
