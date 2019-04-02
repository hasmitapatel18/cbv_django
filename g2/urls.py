from django.urls import path
from . import views
from g2.views import *



urlpatterns = [
    path('', FilmListView.as_view(), name='film_list'),

    path('film_detail/<int:pk>', views.FilmDetailView.as_view(), name='film_detail'),

    path('film/', views.FilmCreateView.as_view(), name='film_create'),

    path('g2/<int:pk>', views.FilmUpdateView.as_view(), name='film_update'),

    path('delete/<int:pk>', views.FilmDeleteView.as_view(), name='film_delete'),















]
