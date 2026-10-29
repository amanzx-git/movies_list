from watchlist_app.api import views
from django.urls import path , include

urlpatterns = [
    path('list/' , views.movie_list , name='movie_list'),
    path('<int:pk>', views.movie_details, name='movie-detail')
]