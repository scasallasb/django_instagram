"""
# Django
from django.shortcuts import redirect
from django.urls import reverse



class ProfileCompletionMiddleware:
    

    def __init__(self, get_response):
        #Middleware initialization.
        self.get_response = get_response


    def __call__(self, request):

        #Code to be executed for each request before the view is called.
        #import pdb;pdb.set_trace()
        if  request.GET:
            if not request.user.is_anonymous:
                
                try:

                    if not request.user.is_staff:
                        profile = request.user.profile
                        if not profile.picture or not profile.biography:
                            if request.path not in [reverse('update_profile'), reverse('logout')]:
                                return redirect('update_profile')
                        response = self.get_response(request)
                        return response

                except Object.DoesNotExitst:
                    return redirect('login')
"""


"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response
        #import pdb;pdb.set_trace()

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        #import pdb;pdb.set_trace()
        if not request.user.is_anonymous:

            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response