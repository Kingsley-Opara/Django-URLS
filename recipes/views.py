from multiprocessing import context
from django.shortcuts import render, get_object_or_404

from .models import Recieps
# Create your views here.
def home(request, *args, **kwargs):
    queryset = Recieps.objects.all()
    context = {
        'object': queryset
    }
    return render(request, 'index.html', context)

def detailView(request, id, *args, **kwargs):
    object = get_object_or_404(Recieps, id=id)
    context = {
        'object': object
    }
    return render(request, 'detail.html', context)