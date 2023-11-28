# Create a Book class that has two attributes:
# title
# author
# and two methods:

# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.

class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
    def get_title(self) -> str:
        return "Title: " + self.title
    def get_author(self) ->str:
        return "Author: " + self.author

PP = Book(title = "Pride and Prejudice" , author = "Jane Austen")
H = Book(title = "Hamlet " , author = "William Shakespeare")
WP = Book(title = "War and Peace" , author = "Leo Tolstoy ")

print(PP.get_title())
print(H.get_author())
print(WP.title)