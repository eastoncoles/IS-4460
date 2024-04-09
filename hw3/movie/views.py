from django.shortcuts import render, redirect
from django.views import View
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.urls import reverse
from .forms import MovieForm
from django import forms
from django.http import HttpResponse
# Create your views here.

class MovieListCreateView(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieTest(View):

    template_name = 'movie-add.html'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


    def get(self, request):
     
        return render(request, self.template_name,)
    
class MovieLogin(View):

    template_name ='movie-login.html'

    def get(self, request):

        return render(request, self.template_name,)
    
class MovieList(View):
        
        template_name = 'movie-list.html'

        def get(self, request):
             movies = Movie.objects.all()
             return render(request, self.template_name, context={'movies':movies})
        
        
class MovieAdd(View):
     
     template_name = 'movie-add.html'

     def get(self, request):
          form = MovieForm()
          return render(request, self.template_name, context={'form':form})
     
     def post(self, request):
          form = MovieForm(request.POST)
          if form.is_valid():
               movie = form.save()
               return redirect(reverse('movie-list'))
          return render(request=request, template_name='movie-add.html', context={'form': form})
     
class MovieUpdate(View):
     
     template_name = 'movie-update.html'
     
     def get(self, request, movie_id):
          movie = Movie.objects.get(pk=movie_id)
          form = MovieForm(instance=movie)
          return render(request, self.template_name, {'movie': movie})

     def post(self, request, movie_id):
          movie=Movie.objects.get(pk=movie_id)
          form = MovieForm(request.POST, instance=movie)
          if form.is_valid():
               movie=form.save()
               return redirect(reverse('movie-list'))
          return render(request, self.template_name, context={'movie':movie, 'form':form})
     
class MovieDelete(View):
     def get(self, request, movie_id):
          movie = Movie.objects.get(pk=movie_id)
          form = MovieForm (instance=movie)
          for field in form.fields:
               form.fields[field].widget.attrs['disabled'] = True
          return render(request, 'movie-delete.html', {'movie':movie, 'form':form})
     
     def post(self, request, movie_id):
          movie = Movie.objects.get(pk=movie_id)
          movie.delete()
          return redirect(reverse('movie-list'))
     
class MovieDetails(View):
     def get(self, request, movie_id):
          movie = Movie.objects.get(pk=movie_id)
          return render(request, template_name='movie-details.html',context={'movie':movie})
     


    
    
