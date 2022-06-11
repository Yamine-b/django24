from django.shortcuts import render
from computerApp.models import Machine
# Create your views here.
def index(request):
    machines = Machine.objects.all()
    context= {
        'machines':machines,
    }

    return render(request, 'template/index.html', context=context)