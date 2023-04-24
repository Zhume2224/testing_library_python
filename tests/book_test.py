import unittest
from models.book import Book
# from models.books import *

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1=Book('book1',"person1",1999,False)
        self.book2=Book('book2','person2',1945,False)
      
        self.books=[self.book1,self.book2]

    def test_book_has_elements(self):
         self.assertEqual('book1',self.book1.name)
         self.assertEqual('person1',self.book1.author)
         self.assertEqual(1999,self.book1.genre)
         self.assertEqual(False,self.book1.checked_out)

    def test_book_has_a_list(self):
        bookslist=self.book1.get_bookslist(self.book1)
        self.assertEqual(['book1'],bookslist)

    def test_increase_book(self):
          book3=Book('book3','person3',1933,False)
          self.books.increase_book(book3)
          self.assertEqual(3,len(self.books))


    # def test_decrease_book(self):

    

