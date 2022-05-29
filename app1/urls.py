from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('account_list/',views.account_list),
    path('create_account/',views.create_account),
    path('edit/<int:id>/',views.edit),
    path('update/<int:id>/',views.update1),
    path('delete/<int:id>/',views.delete_id)
]