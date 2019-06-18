from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)


def addAuthors(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'books_authors_app/addauthor.html', context)

def addAuthor(request):
    if request.method == "POST":
        fname = request.POST["first_name"]
        lname = request.POST["last_name"]
        notes = request.POST["notes"]
        new_author = Author.objects.create(first_name=fname, last_name=lname, notes=notes)
        return redirect('/authors/'+ str(new_author.id))

def author(request, authorid):
    context = {
        "author": Author.objects.get(id=authorid),
        "books": Author.objects.get(id=authorid).books,
        "all_books": Book.objects.all(),
    }
    return render(request, 'books_authors_app/showauthor.html', context)

def addbooktoauthor(request):
    if request.method == "POST":
        author_id = request.POST["authorid"]
        author = Author.objects.get(id=author_id)
        book_id = request.POST["books"]
        book = Book.objects.get(id=book_id)
        author.books.add(book)
        return redirect("/authors/"+author_id)

def book(request, bookid):
    context = {
        "book": Book.objects.get(id=bookid),
        "authors": Book.objects.get(id=bookid).authors,
        "all_authors": Author.objects.all(),
    }
    print(context)
    return render(request, 'books_authors_app/showbook.html', context)

def addBook(request):
    if request.method == "POST":
        title = request.POST["book_title"]
        desc = request.POST["book_description"]
        new_book = Book.objects.create(title=title, desc=desc)
        return redirect('/books/'+ str(new_book.id))

def addauthortobook(request):
    if request.method == "POST":
        book_id = request.POST["bookid"]
        book = Book.objects.get(id=book_id)
        author_id = request.POST["authors"]
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
        return redirect("/books/"+book_id)
