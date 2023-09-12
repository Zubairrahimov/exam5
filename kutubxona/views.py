from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.




class AuthorGetView(APIView):
    def get(self, request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

class AuthorDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        author = get_object_or_404(Author, id = kwargs['author_id'])
        author.delete()
        return Response({'message' : 'Task deleted successfully'}) 
    
class AuthorUpdateView(APIView):
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(request.data)
    
class BooksGetView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
        

class BookDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id = kwargs['book_id'])
        book.delete()
        return Response({'message' : 'Task deleted successfully'}) 
    


class BookUpdateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(request.data)
    


# NOW all left is to create authorsbooks class to show authors books


class AuthorBooksAPIView(APIView):
    def get(self, request, author_id, **kwargs):
        
        book = get_object_or_404(Book, id = author_id)
        books = Book.objects.filter(author=book.id)
        serializer = BookSerializer(books,many=True)
        
        return Response(serializer.data)
    

