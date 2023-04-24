from models.book import Book

book1=Book('The Hobbit', 'J.R.R. Tolkien', 'fantasy',True)
book2=Book('To Kill a Mockingbird', 'Harper Lee', 'classic',True)
book3=Book('Harry Potter and the Philosopher\'s Stone','J.K Rowling','fantasy',False)

books=[book1,book2,book3]
# bookslist=[]

# def get_bookslist(book):
#     if book.name not in bookslist:
#        bookslist.append(book.name)
   

def add_book(book):
    if book not in books:
       books.append(book)
  
def decrease_book(book_name):
    for book in books:
       if book.name==book_name:
          books.remove(book)
 
def check_in(book_name):
    for book in books :
        if book.name==book_name and book.checked_out==True:
            book.checked_out = False
        else:
            pass 

def check_out(book_name):
    for book in books :
        if book.name==book_name and book.checked_out==False:
            book.checked_out = True
        else:
            pass 

