from django.urls import path
from .views import home, logout_

urlpatterns = [
    path('', home, name="home"),
    path('logout/', logout_, name="logout")
]
