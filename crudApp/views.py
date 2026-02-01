from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.exceptions import ValidationError
from .models import Persona
from .forms import PersonaForm


class ShowListView(ListView):
    model = Persona
    template_name = "show.html"
    context_object_name = "personas"


def save(request, pk='0'):
    form = PersonaForm

    if pk != '0':
        try:
            persona = Persona.objects.get(ci=pk)
            form = PersonaForm(instance=persona)
        except ValidationError:
            return render(request, "save.html", {"pk": pk, "form": form, "error": "No se encuentra el id."})

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona) if pk != '0' else PersonaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("result")
        else:
            return render(request, "save.html", {"pk": pk, "form": form, "error": "La información no es valida."})

    return render(request, "save.html", {"pk": pk, "form": form})


def delete(request, pk=0):
    if (pk != 0):
        try:
            persona = Persona.objects.get(ci=pk)
            persona.delete()
            return render(request, "result.html")
        except ValidationError:
            return render(request, "result.html", {"error": "No existe la persona."})
    else:
        return render(request, "result.html", {"error": "No ha seleccionado ninguna persona para eliminar."})


def result(request):
    return render(request, "result.html")
