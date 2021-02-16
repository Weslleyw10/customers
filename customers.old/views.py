from django.shortcuts import get_object_or_404, redirect, render
from .models import Person
from .forms import Form

def list(request):
    listPersons = Person.objects.all()

    context = {
        'persons': listPersons,
    }

    return render(request, 'customers/index.html', context)


def new(request):
    form = Form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('list')
    else:
        context = { 'form': form }
        return render(request, 'customers/new.html', context)


def single(request, id):
    person = get_object_or_404(Person, pk=id)
    form = Form(request.POST or None, request.FILES or None, instance=person)    

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            
    context = { 'form': form }
    return render(request, 'customers/single.html', context)
    
def delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('list')

    context = { 'person': person }
    return render(request, 'customers   /del.html', context)