from django.views import View
from django.shortcuts import render

class HomePageView(View):
    def get(self, request):
        
        my_hello = 'hello world'

        context = {"hi":my_hello,
                   }

        return render(request, '/lab4project/webapps_IS4460-main/ab3/templates/lab3/index.html', context)    
    
    





