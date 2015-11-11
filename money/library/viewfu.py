from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
from allbook.models import Book,Author
def index(request):
    return render_to_response("index.html")
    
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
    else:
        return HttpResponse("hHH")
    
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
def update_book(request):
    if request.POST:
        post=request.POST
        new_book = Book(
            title = post["textfield"],
            authorID  = post["textfiel2"], 
            publisher = post["textfield3"],
            publishdate = post["textfield4"],
            price = post["textfield5"],
            )
        new_book.save()
    return render_to_response("update_book.html")
def update(request):
    if request.POST:
        post=request.POST
        books = Book.objects.filter(title = post["textfield"])
        books.authorID.update(post["textfield2"])
        books.publisher.update(post["textfield3"])
        books.publishdate.update(post["textfield4"])
        books.price.update(post["textfield5"])
        return render_to_response('update_book.html')
    else:
        return render_to_response('update_form.html')  
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
        #if len(new_book.isbn)==0:
         #   new_book.delete()
        #auth=Author.objects.filter(authorID=new_book.authorID)
        #if len(auth)==0:
        #    return render_to_response("error.html")
        #else:
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
        if len(author_list)==0:
             return render_to_response("error.html")
        else:
        #return render_to_response('search.html',{'author_list':author_list})
            books = Book.objects.filter(authorID = author_list[0].authorID)
            return render_to_response('search_book.html',{'books': books})
    else:
        return render_to_response('error.html')
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

