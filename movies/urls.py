from django.urls import path
from .views import SearchMovies,index,ParseToJson

app_name = "movies"

urlpatterns = [
    path('',index,name="index"),
    path('search/',SearchMovies,name="search"),
    path('parse/',ParseToJson,name="parse"),
]