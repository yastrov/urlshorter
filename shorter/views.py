# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, View, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Url
from .utils import b64ToInt, intToB64
from django.utils import simplejson

class IndexPage(TemplateView):
    template_name = 'index.html'


class UrlCreate(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
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
            if request.is_ajax():
                results ={
                    "url": url.url,
                    "short": url.get_short_url()
                }
                json = simplejson.dumps(results)
                return HttpResponse(json, mimetype='application/json')
            else:
                return render(request, 'url_info.html', {'url': url})
        else:
            return HttpResponse('ERROR')


class UrlRecoverRedirect(RedirectView):
    permanent = True
    query_string = True

    def get_redirect_url(self, uri):
        try:
            uri = b64ToInt(uri)
            url = get_object_or_404(Url, pk=uri)
            return url.url
        except:
            raise Http404


class UrlAbout(DetailView):
    model = Url
    template_name = 'url_info.html'

    def get_object(self, queryset=None):
        try:
            uri = self.kwargs.get('uri', None)
            udata = b64ToInt(uri)
            return get_object_or_404(Url, pk=udata)
        except:
            raise Http404


class UrlList(ListView):
    template_name = 'url_list.html'
    queryset = Url.objects.all().order_by('-pub_date')
    context_object_name = 'urls'
    paginate_by = 40


#Next for AJAX
def url_create(request):
    if request.is_ajax():
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
        results ={
            "url": url.url,
            "short": url.get_short_url()
        }
        json = simplejson.dumps(results)
        return HttpResponse(json, mimetype='application/json')

    else:
        return HttpResponse('ERROR')