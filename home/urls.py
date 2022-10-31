from django.urls import path
from home.views import create, routetourl


urlpatterns = [
    path('', create),
    path('<slug:key>/' , routetourl )
]
