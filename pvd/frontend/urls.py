from django.urls import path

from frontend.views import hello_world


urlpatterns = [

    path('', hello_world),

]