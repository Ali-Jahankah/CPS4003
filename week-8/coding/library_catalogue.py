class LibraryCatalogue:
    library_name = "st Marys"
    next_book_id = 2000
    def __init__(self,title,author,genre,availability = True):
        self.id = LibraryCatalogue.next_book_id
        LibraryCatalogue.next_book_id +=1
        self.title=title
        self.author = author
        self.genre=genre
        self.availability = availability
        
    @classmethod
    def set_library_name(cls,new_name):
        cls.library_name = new_name
    
    def checkout(self):
        self.availability = False
        print(f"Book {self.title} checked-out!")
    def return_book(self):
        self.availability = True
        print(f"Book {self.title} returned!")
    def display_info(self):
        print(f"Displaying book info: \n ID: {self.id} | Title: {self.title} | Author: {self.author} | Genre: {self.genre} | Availability: {'Available' if self.availability else 'Not available'}")
        

book1 = LibraryCatalogue(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction")
book2 = LibraryCatalogue(title="To Kill a Mockingbird", author="Harper Lee", genre="Classics")
book1.display_info()
book2.display_info()
print("This is a test")