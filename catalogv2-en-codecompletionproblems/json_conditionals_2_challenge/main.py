import json

# Sample book data
book_data = [
        {"_id": 1, "title": "The Great Adventure", "genre": "Fiction", "pages": 350, "rating": 4.2},
        {"_id": 2, "title": "Science 101", "genre": "Non-Fiction", "pages": 250, "rating": 4.7},
        {"_id": 3, "title": "Mystery Night", "genre": "Fiction", "pages": 290, "rating": 4.1},
        {"_id": 4, "title": "Epic Saga", "genre": "Fiction", "pages": 450, "rating": 4.8},
        {"_id": 5, "title": "History of Time", "genre": "Non-Fiction", "pages": 400, "rating": 4.9},
        {"_id": 6, "title": "Self-Improvement Guide", "genre": "Non-Fiction", "pages": 320, "rating": 4.3},
        {"_id": 7, "title": "Cooking Basics", "genre": "Non-Fiction", "pages": 200, "rating": 4.6},
]

# Filtering books that are Non-Fiction and have a rating of at least 4.5
high_rated_nonfiction_books = []

for book in book_data:
        if book["genre"] == "Non-Fiction" and book["rating"] >= 4.5:
                high_rated_nonfiction_books.append(book["title"])

# Display result
print(high_rated_nonfiction_books)
