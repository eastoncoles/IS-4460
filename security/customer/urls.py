from django.urls import include, path
from .views import CustomerListView


urlpatterns=[path('list/',CustomerListView.as_view(), name='customer_list'
                  )]
