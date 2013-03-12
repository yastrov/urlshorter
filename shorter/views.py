# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Url
import base64

class IndexPage(TemplateView):
    template_name = 'index.html'


def create_url(request):
    if request.method != "POST":
        HttpResponse('ERROR')
    if "url" in request.POST:
        udata = request.POST['url']
        try:
            url = Url.objects.get(url=udata)
        except Url.DoesNotExist:
            try:
                url = Url(url=udata, pub_date=timezone.now())
                url.full_clean()
                url.save()
            except:
                return HttpResponse('ERROR')
        data = base64.b64encode(str(url.short_version) )
        return HttpResponseRedirect( reverse('shorter.urls.about_url', args=(data,)) )
    return HttpResponse('ERROR')

def recover_url(request, uri):
    """uri - short version of URL in base64 encoding"""
    try:
        uri = base64.b64decode(uri)
        uri = int(uri)
        url = get_object_or_404(Url, pk=uri)
        return HttpResponseRedirect(url.url)
    except:
        return HttpResponse('ERROR')

def about_url(request, uri):
    """uri - short version of URL in base64 encoding"""
    try:
        udata =  base64.b64decode(uri)
        udata = int(udata)
        url = get_object_or_404(Url, pk=udata)
        return render(request, 'url_info.html', {'url': url})
    except:
        return HttpResponse('ERROR')

class UrlList(ListView):
    template_name = 'url_list.html'
    queryset = Url.objects.all().order_by('-pub_date')
    context_object_name = 'urls'
    paginate_by = 40
