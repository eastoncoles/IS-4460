from django.urls import path
from .views import MovieListCreateView
from .views import MovieLogin, MovieTest, MovieAdd, MovieList, MovieUpdate, MovieDelete, MovieDetails

urlpatterns = [
    path('movies/',MovieAdd.as_view(), name ='movie-list-create'),
    path('movies/<int:movie_id>/',MovieDetails.as_view(), name='movie-detail'),
    path('test/', MovieTest.as_view(), name='test'),
    path('movie-login/', MovieLogin.as_view(), name='movie-login'),
    path('movie-add/', MovieAdd.as_view(), name ='movie-add'),
    path('movie-list/', MovieList.as_view(), name="movie-list"),
    path('movie-update/<int:movie_id>/', MovieUpdate.as_view(), name='movie-update'),
    path('movie-delete/<int:movie_id>/', MovieDelete.as_view(), name='movie-delete'),
    path('movies-detail/int', MovieDetails.as_view(), name='movie-details')

]

