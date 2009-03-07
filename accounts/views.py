# Create your views here.
from django.shortcuts import render_to_response
from django.conf import settings
from utilities.djangologging import *
import logging

def register(request):
    """
    View which is used for Registration.

    @param request: The HTTP request Object.

    """
    logging.debug('This is a sample debug message')
    return render_to_response('register.html')