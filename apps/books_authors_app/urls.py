from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.addAuthors),
    url(r'^authors/(?P<authorid>\d+)$', views.author),
    url(r'^addAuthors$', views.addAuthors),
    url(r'^addAuthor$', views.addAuthor),
    url(r'^addbooktoauthor$', views.addbooktoauthor),
    url(r'^books/(?P<bookid>\d+)$', views.book),
    url(r'^addBook$', views.addBook),
    url(r'^addauthortobook$', views.addauthortobook),
]
