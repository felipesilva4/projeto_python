from django.forms import ModelForm
from .models import Vitimas1


class VitimaForm(ModelForm):
    class Meta:
        model = Vitimas1
        fields = ['nome','sobrenome','telefone','email','senha']