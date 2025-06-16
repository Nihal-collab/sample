from django.urls import path
from . import views

urlpatterns=[
    path('get_book/',views.get_book,name="get_book"),
    path('post_book/',views.post_book,name="post_book"),
    path('update_book/<int:id>/',views.update_book,name="update_book"),
    path('delete_book/<int:id>/',views.delete_book,name="delete_book"),
    path('get_sample_data/',views.get_sample_data,name="get_sample_data"),
    path('post_sample_data/',views.post_sample_data,name="post_sample_data"),
    path('put_sample_data/<int:id>/',views.put_sample_data,name="put_sample_data"),

]