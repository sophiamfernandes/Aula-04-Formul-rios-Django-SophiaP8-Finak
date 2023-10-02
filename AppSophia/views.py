from django.shortcuts import render, redirect
from.models import lugares, coisasEssencias
# Create your views here.
def home(request):
  outroslugares=lugares.objects.all()
  coisasimp= coisasEssencias.objects.all()
  context= {"lugares": outroslugares, "coisasEssencias":coisasimp}
  print(outroslugares)
  return render(request,"home.html",context=context)

def create_lugar(request):
  if request.method=="POST":
    lugares.objects.create(
      cidade=request.POST["cidade"],
      pais=request.POST["pais"],
      continente=request.POST["continente"],
      clima=request.POST["clima"]
    )

    return redirect("home")
  return render(request,"formsLug.html", context={"action":"Adicionar"})
  
def update_lugar(request, id):
  lugar=lugares.objects.get(id=id)
  if request.method=="POST":
    lugar.cidade=request.POST["cidade"]
    lugar.pais=request.POST["pais"]
    lugar.continente= request.POST["continente"]
    lugar.clima=request.POST["clima"]
    lugar.save()

    return redirect("home")
  return render(request,"formsLug.html", context={"action":"Atualizar","lugar":lugar})

def delete_lugar(request, id):
  lugar=lugares.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
      lugar.delete()

    return redirect("home")
  return render(request,"r_u_sure_lug.html", context={"lugar":lugar})

def create_coisasEssencias(request):
  if request.method=="POST":
    coisasEssencias.objects.create(
      cidade=request.POST["cidade"],
      artefato=request.POST["artefato"],
      importancia=request.POST["importancia"],
      preco=request.POST["preco"]
    )

    return redirect("home")
  return render(request,"formsCois.html")

def update_coisa(request, id):
  coisa=coisasEssencias.objects.get(id=id)
  if request.method=="POST":
    coisa.cidade=request.POST["cidade"]
    coisa.artefato=request.POST["artefato"]
    coisa.importancia= request.POST["importancia"]
    coisa.preco=request.POST["preco"]
    coisa.save()

    return redirect("home")
  return render(request,"formsCois.html", context={"action":"Atualizar","coisa":coisa})

def delete_coisa(request, id):
  coisa=coisasEssencias.objects.get(id=id)
  if request.method=="POST":
    if "confirm" in request.POST:
      coisa.delete()

    return redirect("home")
  return render(request,"r_u_sure_cois.html", context={"coisa":coisa})