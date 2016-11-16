
from django.conf.urls import url
from imagebook import views

urlpatterns = [
    url(r'^books/$',views.books,name='books'),
    url(r'^books/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',views.bookdetail,{'day':'15'},name='books_time'),

    url(r'^detail/(?P<pk>[\d]+)$',views.bookdetail,name='book_detail'),

]
