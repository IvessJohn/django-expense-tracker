from django.urls import path

from . import views

urlpatterns = [
    # Authentication
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    # Main functionality
    path('', views.dashboard, name='home'),
    path('expense_add/', views.add_expense_full_form, name='expense_add'),
    path('expenses/<str:expense_id>/', views.expense_info, name='expense_info'),
    path('expenses/<str:expense_id>/delete/', views.expense_delete, name='expense_delete'),
    # Extras
    path('about/', views.about, name='about'),
]