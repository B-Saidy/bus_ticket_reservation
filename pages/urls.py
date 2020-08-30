from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('routes', views.routes, name='routes'),
    path('search/', views.search_results, name='search'),
    path('reserve/<int:id>/', views.reserve, name='reserve'),
    path('cancel/<int:id>/', views.cancel_booking, name='cancel'),
    path('update/<int:id>/', views.update, name='update'),

]
