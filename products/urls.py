from products import views
from django.urls import path

app_name = 'products'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:item_id>/', views.details, name='details'),
    path('add/', views.create_item, name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

]