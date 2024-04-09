import os
import django
from movie.models import Movie
from movie.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hw2.settings')
django.setup()

##clearing instances
Movie.objects.all().delete()
User.objects.all().delete()

#Movies
MoviesToCreate = [{"title": "Movie A", "description":"Description A","director":"Director A","release_year":"2001","budget":"1000000","runtime":"2:10","rating":"PG","genre":"Comedy"},
                  {"title": "Movie B", "description":"Description B","director":"Director B","release_year":"2002","budget":"2000000","runtime":"2:20","rating":"PG","genre":"Action"},
                  {"title": "Movie C", "description":"Description C","director":"Director C","release_year":"2003","budget":"3000000","runtime":"2:30","rating":"PG-13","genre":"Comedy"},
                  {"title": "Movie D", "description":"Description D","director":"Director D","release_year":"2004","budget":"4000000","runtime":"2:40","rating":"PG-13","genre":"Romance"},
                  {"title": "Movies E", "description":"Description E","director":"Director E","release_year":"2005","budget":"5000000","runtime":"2:50","rating":"PG","genre":"Comedy"},
                  {"title": "Movie F", "description":"Description F","director":"Director F","release_year":"2006","budget":"6000000","runtime":"3:00","rating":"PG-13","genre":"Action"},
                  {"title": "Movies G", "description":"Description G","director":"Director G","release_year":"2007","budget":"7000000","runtime":"3:10","rating":"R","genre":"Comedy"},
                  {"title": "Movie H", "description":"Description H","director":"Director H","release_year":"2008","budget":"8000000","runtime":"3:20","rating":"PG","genre":"Animation"},
                  {"title": "Movie I", "description":"Description I","director":"Director I","release_year":"2009","budget":"9000000","runtime":"3:30","rating":"R","genre":"Horror"},
                  {"title": "Movies J", "description":"Description J","director":"Director J","release_year":"2010","budget":"10000000","runtime":"3:40","rating":"PG","genre":"Adventure"},
                  ]

for mov in MoviesToCreate:
    instance = Movie.objects.create(**mov)

UsersToCreate = [{"username":"username1","password":"Password1","fist_name":"Alpha","last_name":"Johnson","email":"alpha@abc.com"},
                 {"username":"username2","password":"Password2","fist_name":"Beta","last_name":"Williams","email":"beta@abc.com"},
                 {"username":"username3","password":"Password3","fist_name":"Charlie","last_name":"Johns","email":"charlie@abc.com"}
                 ]

for us in UsersToCreate:
    instance = User.objects.creat(**us)


#Queries
MovieList = Movie.objects.all()
print(MovieList)
MovieFilter = Movie.objects.filter(title__startswith='Movie')
print(MovieFilter)
MovieA = Movie.objects.get(ID="1")
print(MovieA)
MovieA.update(director="Stephen Spielberg")
print(MovieA)
Movie.objects.filter(id="7").delete()

#Data Validation
UserInput = input("What is your username?")
UserTest = User.objects.filter(username=UserInput)







