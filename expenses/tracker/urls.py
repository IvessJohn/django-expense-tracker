from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('about/', views.about, name='about'),
    path('expense_add/', views.add_expense_full_form, name='expense_add'),
    path('expenses/<str:expense_id>/', views.expense_info, name='expense_info'),
]