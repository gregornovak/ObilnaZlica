from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Recept

def zadnji_recepti(request):
    en_recept = Recept.objects.filter().order_by("-datum_objave")[0:1]
    recepti = Recept.objects.filter().order_by("-datum_objave")[1:7]

    #vsi_recepti = Recept.objects.all().order_by("-datum_objave")
    #poizvedba = request.GET.get("poizvedba")

    #if poizvedba:
    #    vsi_recepti = vsi_recepti.filter(ime_recepta__icontains=poizvedba)

    context = {
        "en_recept": en_recept,
        "recepti": recepti,
        #"vsi_recepti": vsi_recepti
    }
    #sestavine = Recept.objects.values_list("sestavine_recepta", flat=True)
    #sestavine_main = sestavine.split(".")

    return render(request, "index.html", context)

def vsi_recepti(request):
    vsi_receptki = Recept.objects.all().order_by("-datum_objave")
    poizvedba = request.GET.get("poizvedba")
    if poizvedba:
        vsi_receptki = vsi_receptki.filter(ime_recepta__icontains=poizvedba)

    paginator = Paginator(vsi_receptki, 9)

    page = request.GET.get('page')

    try:
        vsi_receptki = paginator.page(page)
    except PageNotAnInteger:
        vsi_receptki = paginator.page(1)
    except EmptyPage:
        vsi_receptki = paginator.page(paginator.num_pages)

    return render(request, "vsirecepti.html", {"vsi_receptki": vsi_receptki})

def posamezen_recept(request, id):
    recept = get_object_or_404(Recept, id=id)
    #sestavine = Recept.objects.values_list("sestavine_recepta", flat=True).get(id=id)
    #sestavina = sestavine.split(".")
    return render(request, "recept.html", {"recept": recept})

#def kategorija_recepta(request, tip):
    #kategorija = get_object_or_404(Recept, id=tip)
    #return render(request, "kategorije.html", {"kategorija": kategorija})
