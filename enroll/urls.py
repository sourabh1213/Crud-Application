from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete_data, name='delete'),
    path('update/<int:id>', views.update, name='update'),
]
