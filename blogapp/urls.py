
from django.urls import path
from .views import homeView, listBlogsView

urlpatterns = [
    path('home/', homeView ),
    path('list/',listBlogsView ),
]