from typing import Any
from django.shortcuts import redirect
from django.urls import reverse

class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        print("Middleware executed")
        if request.user.is_authenticated and request.path == reverse('eshikshaadminpanelapp:user_login'):
            print("Redirecting authenticated user")
            return redirect('eshikshaadminpanelapp:index')
        
        response = self.get_response(request)
        return response