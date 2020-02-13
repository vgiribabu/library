from django.shortcuts import render, get_object_or_404
from books.models import Library
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    lib = Library.objects.all()
    context = {'lib': lib}
    return render(request, 'books/index.html', context)


def create(request):
    if request.method == 'POST':
        Library.objects.create(
            book_name=request.POST['book_name'],
            author=request.POST['author'],
            description=request.POST['description'],
            date=timezone.now()
        )
        return HttpResponseRedirect(reverse('books:index'))
    return render(request, 'books/create.html')


def detail(request, i_id):
    check = get_object_or_404(Library, pk=i_id)
    return render(request, "books/detail.html", {'check': check})
