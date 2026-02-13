
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='authors.index'),
    path('show/<int:author_id>/', views.show, name='authors.show'),
    path('turn_inactive/', views.turn_inactive, name='authors.turn_inactive'),
    path('change_age/', views.change_age, name='authors.change_age'),
    path('author_by_email/', views.author_by_email, name='authors.author_by_email'),
    path('author_by_age/', views.author_by_age, name='authors.author_by_age'),
    path('top_ten_authors/', views.top_ten_authors, name='authors.top_ten_authors'),
    path('age_between/', views.age_between, name='authors.age_between'),
]