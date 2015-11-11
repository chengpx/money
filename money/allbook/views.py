from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from allbook.models import Book,Author
def index(request):
    return render_to_response("index.html")
def instruction(request):
    return render_to_response("instruction.html")
def success(request):
    return render_to_response("success.html")
def add_book(request):
    if request.POST:
        post=request.POST
        new_book = Book(
            isbn = post["textfield"],
            title = post["textfield2"],
            authorID = post["textfield3"],
            publisher = post["textfield4"],
            publishdate = post["textfield5"],
            price = post["textfield6"],
            )
        new_book.save()
    return render_to_response("add_book.html")
    
def add_author(request):
    if request.POST:
        post=request.POST
        new_author = Author(
            authorID = post["textfield"],
            name = post["textfield2"],
            age = post["textfield3"],
            country = post["textfield4"],
            )
        new_author.save()
    return render_to_response("add_author.html")
def insert_book(request):
    if request.POST:
        post=request.POST
        new_book = Book(
            isbn = post["textfield"],
            title = post["textfield2"],
            authorID = post["textfield3"],
            publisher = post["textfield4"],
            publishdate = post["textfield5"],
            price = post["textfield6"],
            )
        new_book.save()
        auth = Author.objects.filter(authorID=new_book.authorID)
        if len(auth)==0:
            return render_to_response("add_author.html")
        else:
            return render_to_response("insert_book.html")
def insert_author(request):
    if request.POST:
        post=request.POST
        new_author = Author(
            authorID = post["textfield"],
            name = post["textfield2"],
            age = post["textfield3"],
            country = post["textfield4"],
            )
        new_author.save()
    return render_to_response("insert_author.html")

def search_form(request):
    return render_to_response('search_form.html')
def update_form(request):
    return render_to_response('update_form.html')
def search_book(request):
    if "q" in request.GET and request.GET["q"]:
        q=request.GET["q"]
        author_list = Author.objects.filter(name = q)
        #return render_to_response('search.html',{'author_list':author_list})
        books = Book.objects.filter(authorID = author_list[0].authorID)
        if len(author_list)==0:
            return render_to_response('search_form.html')
        else:
            return render_to_response('search_book.html',{'books': books})
    else:
        return render_to_response('search_form.html')
def search_author(request):
    #return HttpResponse("HHHHH")
    if "p" in request.GET and request.GET["p"]:
        p=request.GET["p"]
        books = Book.objects.filter(title = p)
        author_list = Author.objects.filter(authorID = books[0].authorID)
        return render_to_response('search_author.html',{'books': books,'author_list':author_list})
    else:
        return HttpResponse("Error!")
def delete(request):
    if "q" in request.GET and request.GET["q"]:
        q=request.GET["q"]
        books = Book.objects.filter(title = q)
        if len(books)==0:
            return HttpResponse("Error!")
        #author_list = Author.objects.filter(authorID = books.authorID)
        #author_list.delete()
        books.delete()
        return render_to_response('delete.html')
    else:
        return HttpResponse("Error!")
def update_book(request):
    #process the update request and return a html with information
    if 'isbn' in request.GET and request.GET['isbn']:
         update_id = request.GET["isbn"]
         book = Book.objects.filter( isbn = update_id )[0]
         return render_to_response("update_book.html", {"book":book})
def update(request):
    if request.POST:
        post = request.POST
        book = Book.objects.get(isbn = post["isbn"])
        #update
        book.authorID = post["authorID"]
        book.publisher = post["publisher"]
        book.publishdate = post["publishdate"]
        book.price = post["price"]
        #save
        book.save()  
        return render_to_response("success.html")
