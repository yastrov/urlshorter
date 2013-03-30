from django.utils import timezone
from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        exclude = ('pub_date', 'short_version')
        fields = ('url',)

    def save(self, commit=True):
        try:
            u = self.cleaned_data['url']
            url = Url.objects.get(url=u)
        except Url.DoesNotExist:
            url = super(UrlForm, self).save(commit=False)
            #url.pub_date = timezone.now()
            if commit:
                url.save()
        return url