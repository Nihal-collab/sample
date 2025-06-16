from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_book(request):
    data=list(Books.objects.values())
    context={'data':data}
    return render(request,'table.html',context)

def post_book(request):
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        content=request.POST.get('content')
        Books.objects.create(title=title,author=author,content=content)
        return redirect('get_book')
    else:
        return render(request,'form.html')

def update_book(request,id):
    book=Books.objects.get(id=id)
    context={'book':book}
    if request.method=="POST":
        book.title=request.POST.get('title')
        book.author=request.POST.get('author')
        book.content=request.POST.get('content')
        book.save()
        return redirect('get_book')
    return render(request,'edit.html',context)

def delete_book(request,id):
    book=Books.objects.get(id=id)
    book.delete()
    return redirect(get_book)


@api_view(["GET"])
def get_sample_data(request):
    data = list(Books.objects.values())
    return Response({"data":data})

@api_view(["POST"])
def post_sample_data(request):
    print(request.data)
    Books.objects.create(title=request.data["title"], author=request.data["author"], content=request.data["content"])
    return Response("POST")

@api_view(["PUT"])
def put_sample_data(request,id):
    print(request.data)
    book=Books.objects.get(id=id)
    book.title=request.data["title"]
    book.author=request.data["author"]
    book.content=request.data["content"]
    book.save()
    return Response("PUT")