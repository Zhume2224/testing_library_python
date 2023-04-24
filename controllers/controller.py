from flask import render_template, request,redirect
from app import app
from models.books import *
from models.book import *


@app.route('/books')
def index():
    return render_template('index.html',books=books)

@app.route('/books/<int:index>')
def check_detail(index):
    # only fill up the () when there is <>
    return render_template('book_details.html', book=books[index])


@app.route('/books/delete', methods=['POST']) 
# if form;action is post, here must be the same
# if this route has been called, activate below function
def delete_book():
    book_name=request.form['book']
    # ['book']=={{book.name}} 
    decrease_book(book_name)
    return redirect('/books')



@app.route('/books/check_in', methods=['POST']) 
def check_in_book():
    book_name=request.form['book']
    check_in(book_name)
    return redirect('/books')


@app.route('/books/check_out', methods=['POST']) 
def check_out_book():
    book_name=request.form['book']
    check_out(book_name)
    return redirect('/books')


@app.route('/books', methods=['POST']) 
def add_books():
    name=request.form['add_name']
    author=request.form['add_author']
    genre=request.form['add_genre']
    checked_out= False if 'add_checked_out' in request.form else True
    new_book=Book(name,author,genre,checked_out)
    add_book(new_book)
    return redirect('/books')







# # Q1
# @app.route('/books/<int:index>/check_in', methods=['POST']) 
# def check_in_book(index):
#     book_name=request.form['book']
#     check_in(book_name)
#     return render_template('book_details.html',book=books[index],books=books)




