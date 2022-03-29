"""Contains the project decorators."""
from django.shortcuts import render, redirect
from django.http import HttpResponse


def unauthenticated_user(view_func):
    """Redirect an authenticated user to the home page.
    Used for the views which should be accessed only by unauthenticated users.
    """

    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return view_func(request, *args, **kwargs)

    return wrapper_func
