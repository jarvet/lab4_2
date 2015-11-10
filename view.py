from BookDB.models import Book, Author
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.

#input the author's name and find all the book he write
#show the detail information of the book and the author
#when clicking the title of a book
def main(request):
    post = request.POST
    if post:#if there's a form posted means it comes to search the author
        name = post.get('author', '')
        book_lst = Book.objects.filter(AuthorID__Name=name)
        content = {'book_lst':book_lst,}
    else:#else show all the books
        book_lst = Book.objects.all()
    content = {'book_lst':book_lst,}
    return render(request, 'main.html', content)

#delete the book when clicking delete
def delete_book(request,ISBN):
    book = Book.objects.filter(ISBN=ISBN)#find the book to be deleted
    book.delete()
    return HttpResponseRedirect('/')

#add a book, if the author isn't in the db,then add it
def add_book(request):
    post = request.POST
    if post:#getting the form of a new book
        authorName = post.get('Author', '')
        [author,flag] = Author.objects.get_or_create(Name=authorName)#if the author is new, create one
        newbook=Book(
            ISBN=post.get('ISBN', ''),
            Title=post.get('Title', ''),
            Publisher=post.get('Publisher', ''),
            PublishDate=post.get('PublishDate', ''),
            Price=post.get('Price', ''),
            AuthorID=author
        )
        newbook.save()
    return render(request, 'add_book.html', {})

#add an author
def add_author(request):
    post = request.POST
    if post:#getting the form of a new author
        newauthor = Author(
            Name=post.get('Name', ''),
            Age=post.get('Age', ''),
            Country=post.get('Country', ''),
        )
        newauthor.save()
    return render(request, 'add_author.html', {})


#update the author, publisher, publishdate, price of a book
def update_book(request,ISBN):
    book = Book.objects.get(ISBN=ISBN)
    author = book.AuthorID
    content = {'book':book, 'author':author}#original information of the book
    post = request.POST
    if post:#get new information
        book.ISBN = post.get('ISBN', '')
        book.Title = post.get('Title', '')
        book.Publisher = post.get('Publisher', '')
        book.PublishDate = post.get('PublishDate', '')
        book.Price = post.get('Price', '')
        author.Name = post.get('Author', '')
        author.Age = post.get('Age', '')
        author.Country = post.get('Country', '')
        book.save()
        author.save()
    return render(request, 'update_book.html', content)
