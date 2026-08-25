# Project : Smart Library Management System!
#start 
class Book:
    def __init__(self, title,author,isbn):
        self.title = title 
        self.author = author 
        self.__isbn = isbn 
    def get_isbn(self):
        return self.__isbn 
    def get_details(self):
        return(f"The Title of the book is {self.title} , and the author of the book is {self.author}")

class AudioFeature:
    def play_audio(self):
        print("Playing Audio Book Stream...")

class DigitialRights:
    def check_license(self):
        print("DRM License Verified")

class AudioBook(Book , AudioFeature , DigitialRights):
    def __init__(self,title,author,isbn,file_size_mb):
        super().__init__(title,author,isbn)
        self.file_size_mb = file_size_mb
    def get_audio_file(self):
        print(f"The Size of the Audio File is {self.file_size_mb}")
class LibraryShelf:
    def __init__(self):
        self.books = []
    def add_book(self,book):
    
        self.books.append(book)
    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index+=1
            return book
        else :
            raise StopIteration


def overdue_checker(borrow_records, max_days):
    
    for book , days in borrow_records:
        if days>max_days:
            yield f"Alert Message: {book.title} is overdue! (Days: {days})"
#object created 
my_book = Book("Harry potter" , "william" , "ISBN-101")
my_audio_book = AudioBook("HarryPotter fire " , "jhon" , "ISBN-102" , file_size_mb=450)

my_audio_book.play_audio()
my_audio_book.check_license()
my_audio_book.get_audio_file()
print(my_audio_book.get_isbn())

shelf = LibraryShelf()
shelf.add_book(my_book)
shelf.add_book(my_audio_book)
for book in shelf:
    print(book.get_details())

#remaining methods call after object creation 
borrow_records = [(my_book ,5), (my_audio_book,14)]

for alert in overdue_checker(borrow_records,max_days=7):
     print(alert)
     

fines = [0,15,5,25,0,12]
fine_generator = (f"Warning : Unpaid fine of ${n}"for n in fines if n>0)
for fine in fine_generator:
    print(fine)






