from django.shortcuts import get_object_or_404, redirect, render
from .models import Person
from .forms import Form
from django.contrib.auth.decorators import login_required


def list(request):
    search = Person.objects.all()

    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    if first_name or last_name:
        """
        first_name && last_name
        """
        # listPersons = Person.objects.filter(
        #     first_name__icontains=first_name, last_name__icontains=last_name)

        """
        first_name || last_name
        """
        listPersons = Person.objects.filter(first_name__icontains=first_name) | Person.objects.filter(last_name__icontains=last_name)

        print(first_name)
        print(listPersons)

    else:
        listPersons = Person.objects.all()

    context = {
        'persons': listPersons,
    }

    return render(request, 'person/index.html', context)


@login_required
def new(request):
    form = Form(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('list')
    else:
        context = {'form': form}
        return render(request, 'person/new.html', context)


@login_required
def single(request, id):
    person = get_object_or_404(Person, pk=id)
    form = Form(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'person/single.html', context)


@login_required
def delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = Form(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('list')

    context = {'person': person}
    return render(request, 'person/del.html', context)
