from watchlist_app import views
from django.urls import path , include

urlpatterns = [
    path('list/' , views.movie_list , name='movie_list'),
]
