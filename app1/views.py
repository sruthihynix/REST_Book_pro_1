
from rest_framework.response import Response
from app1.models import Book

from rest_framework.decorators import api_view
from .serializers import BookSerializers

# Create your views here.

@api_view(['POST'])
def add(request):
    serial_obj = BookSerializers(data=request.data)
    if serial_obj.is_valid():
        serial_obj.save()
        return Response("Book added sucessfuly")
    else:
        return Response("invalid data")

@api_view(['GET'])
def display(request):
    info= Book.objects.all()
    serial_obj = BookSerializers(info,many=True)
    return  Response(serial_obj.data)


@api_view(['DELETE'])
def delete(request,book_id):
    try:
        book_obj=Book.objects.get(book_id=book_id)
        book_obj.delete()
        return Response("Deleted sucessfully")
    except:
        return Response ("book not found")

@api_view(['POST'])
def update(request,book_id):
    try:
        book_obj=Book.objects.get(book_id=book_id)
        serial_obj=BookSerializers(instance=book_obj, data=request.data,partial=True)
        serial_obj.is_valid()
        serial_obj.save()
        return Response("Updated sucessfully")
    except:
        return Response("Book not found")

# fetch one recod
@api_view(['GET'])
def fetch_one(request,book_id):
    try:
        book_obj=Book.objects.get(book_id=book_id)
        serial_obj = BookSerializers(book_obj)
        return Response(serial_obj.data)
    except:
        return Response("Book not found")



