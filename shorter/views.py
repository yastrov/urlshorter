from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.utils import timezone
from .models import Url
from .utils import b64ToInt, intToB64
from .forms import UrlForm

class IndexPage(TemplateView):
    template_name = 'index.html'


class UrlCreate(FormView):
    template_name = 'index.html'
    success_url = '/about/'
    form_class =  UrlForm

    # def get_form_kwargs(self):
    #     #It be good for send form with prepaired data.
    #     kwargs = super(UrlCreate, self).get_form_kwargs()
    #     kwargs.update({
    #         'pub_date': timezone.now()
    #     })
    #     return kwargs

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.pub_date = timezone.now()
        instance.save()
        full_url = self.get_success_url() + instance.get_b64_number()
        #full_url = reverse(self.get_success_url(), kwargs={'uri': instance.get_b64_number() } )
        return redirect(full_url)


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