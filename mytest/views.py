from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_form.html'

    def post(self, request, *args, **kwargs):
        form = AuthorForm(self.request.POST or None)
        if form.is_valid():
            instance = form.save()
            return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_author");</script>' % (instance.pk, instance))

