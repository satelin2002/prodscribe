from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.core.urlresolvers import reverse

# Helper functions related to URL connections and responses.

def render(request, template, data={}):
    """
    Renders the page with the request context.     
    """
    render_to_response(
        template,
        data,
        context_instance=RequestContext(request)
    )

def redirect(viewname):
    """ 
    Simply redirects to the URL represented by the view 
    function.
    """
    return HttpResponseRedirect(reverse(viewname));
 
def requires_post():
    """
    Like HttpResponse, but uses a 405 status code.
    """
    return HttpResponseNotAllowed(['POST'])    