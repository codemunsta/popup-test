from django.urls import path
from .views import BookCreate, AuthorCreate, index


urlpatterns = [
    path('', index, name='home'),
    path('book/create', BookCreate.as_view(), name='book_create'),
    path('author/create', AuthorCreate.as_view(), name='author_created'),
]