from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreateUser.as_view()),
    path('barbers/', views.BarberList.as_view(), name='barber_read'),
    path('barbers/<int:pk>', views.BarberDetail.as_view(), name='barber_detail'),
    path('comments/', views.CommentList.as_view(), name='comment_read'),
]