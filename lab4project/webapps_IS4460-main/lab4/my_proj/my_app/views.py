from django.views import View
from django.shortcuts import render, redirect
from . import my_functions
from . import my_objects

def fix_name(name: str):
    new_name = name.title()
    return new_name

class HomePageView(View):
    def get(self, request):

        orig_name = 'eASTON'
        name = fix_name(orig_name)

        names = ['luis','mike','joe']

        fixed_names = my_functions.fix_names_list(names)

        car1 = my_objects.Car(color="blue",sound="honk honk",make="Dodge",model="Viper",year="2008")
        car2 = my_objects.Car(color="red", sound="beep beep",make="Dodge",model="Charger",year="2009")
        motorcycle1 = my_objects.Motorcycle(color="red", sound="beep beep",make="BMW",model="abc",year="2023")


        context = {'hi':'hello world!',
                    'name':name,
                    'orig_name' : orig_name,
                    'names':names,
                    'fixed_names': fixed_names,
                    'car1': car1,
                    'car2': car2,
                    'motorcycle1': motorcycle1
                    }
        
        return render(request, 'my_app/index.html', 
                      context)
    
    

    
    