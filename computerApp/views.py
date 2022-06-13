from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from computerApp.models import Machine
from computerApp.forms import AddMachineForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(request) :
    context={}
    return render(request, 'index.html', context)

def machine_list_view(request):
    machines = Machine.objects.all()
    context={'machines':machines}
    return render(request,'template/computerApp/machines_list.html',context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context= {'machine':machine}
    return render(request,'template/computerApp/machine_detail.html',context)

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine= Machine(nom=form.cleaned_data['nom'],mach=form.cleaned_data['mach'])
            new_machine.save()
            return HttpResponseRedirect('machines')
    else:
        form = AddMachineForm()
        context = {'form':form}
        return render(request,'template/computerApp/machine_add.html',context)

def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "template/computerApp/register/register.html", context)

def GES(request) :
    context={}
    return render(request, 'template/computerApp/GES.html', context)

def NAQ(request) :
    context={}
    return render(request, 'template/computerApp/NAQ.html', context)

def ARA(request) :
    context={}
    return render(request, 'template/computerApp/ARA.html', context)

def BFC(request) :
    context={}
    return render(request, 'template/computerApp/BFC.html', context)

def BRE(request) :
    context={}
    return render(request, 'template/computerApp/BRE.html', context)

def CVL(request) :
    context={}
    return render(request, 'template/computerApp/CVL.html', context)

def COR(request) :
    context={}
    return render(request, 'template/computerApp/COR.html', context)

def IDF(request) :
    context={}
    return render(request, 'template/computerApp/IDF.html', context)

def OCC(request) :
    context={}
    return render(request, 'template/computerApp/OCC.html', context)

def HDF(request) :
    context={}
    return render(request, 'template/computerApp/HDF.html', context)

def NOR(request) :
    context={}
    return render(request, 'template/computerApp/NOR.html', context)

def PDL(request) :
    context={}
    return render(request, 'template/computerApp/PDL.html', context)

def PAC(request) :
    context={}
    return render(request, 'template/computerApp/PAC.html', context)

def login(request) :
    context={}
    return render(request, 'template/computerApp/registration/login.html', context)