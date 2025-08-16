from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from fruits.forms import CreateFruit
from fruits.models import Fruit


def index(request):

    all_fruit = Fruit.objects.all()[:5] # juste 5 fruits

    return render(request, 'base.html', {'all_fruit': all_fruit})

def detail_fruit(request, pk):

    try :
        fruit = Fruit.objects.get(pk=pk)
    except :
        messages.error(request, f"le fruit avec l'identifiant {pk}")
        return redirect("fruits_app:home_page")

    return render(request, 'detail_fruit.html', context={'fruit': fruit})

def delete_fruit(request, pk):

    name_fuit = ""

    try :
        fruit = Fruit.objects.get(pk=pk)
        name_fuit = fruit.name
        fruit.delete()

    except :
        messages.error(request, f"Une erreur est survenue")
        return redirect("fruits_app:home_page")

    messages.info(request, f"le fruit : {name_fuit} a ete supprimer avec success")
    return redirect("fruits_app:home_page")

def create_fruit(request):
    """
    Vue de creation d'un fruit,
    """

    # on charge le formulaire
    form = CreateFruit()

    if request.method == "POST":
        form = CreateFruit(request.POST, request.FILES)
        if form.is_valid():
            try:
                fruit = form.save(commit=True)
                fruit.save()
            except Exception as e:
                messages.error(request, f"Impossible d'enregistre le fruit{e}")
            return redirect('fruits_app:detail_fruit', fruit.pk)

        else:
            context = {
                "form": form,
                'error' : form.errors,
            }
            return render(request, 'create_fruit.html', context)

    # contexte a injecter dans le template
    context = {
        'form': form,
    }
    return render(request, 'create_fruit.html', context)

def update_fuit(request, pk):
    """
        Vue de mise a jour d'un fruit existant
    """
    # on va s'assurer que le fruit existe
    try:
        fruit = Fruit.objects.get(pk=pk)

    except :
        messages.error(request, f"le fruit avec l'identifiant {pk}")
        return redirect("fruits_app:home_page") # si le fruit n'existe pas on retourne a la page d'accueil

    # on passe l'instance de fruit dans le formulaire (les valeurs de ses champ dans la base de donnne )
    form = CreateFruit(instance=fruit)
    if request.method == "POST":
        form = CreateFruit(request.POST, request.FILES)
        if form.is_valid():
            # on s'assure que l'enregistrement se passe bien
            try:
                fruit.name = form.cleaned_data['name']
                fruit.description = form.cleaned_data['description']
                fruit.image = form.cleaned_data['image']
                fruit.save()
                redirect('fruits_app:detail_fruit', fruit.pk)
            except Exception as e:
                messages.error(request, f"Impossible d'enregistre le fruit{e}")
            return redirect('fruits_app:detail_fruit', fruit.pk)

        else:
            context = {
                "form": form,
                'error': form.errors,
            }
            return render(request, 'create_fruit.html', context)

    context = {
        'form': form,
    }
    return render(request, 'create_fruit.html', context)


def liste_fruit(request):

    all_fruit = Fruit.objects.all()

    return render(request, 'liste_fruit.html', {'all_fruit': all_fruit})