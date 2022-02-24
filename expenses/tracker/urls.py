from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('expense/<str:expense_id>/', views.expense_info, name='expense_info'),
    path('expense/add/', views.add_expense_full_form, name='expense_add'),
]