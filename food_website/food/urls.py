from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:item_id>/',   views.item, name='item'),
    path('item', views.item, name='item')
]