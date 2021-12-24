from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view),
    path('search', views.search_view),
    path('result', views.result_view)
]