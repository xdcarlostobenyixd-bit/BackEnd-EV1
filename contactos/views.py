from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactoForm
from .models import Contacto


def lista_contactos(request):
    """
    Muestra todos los contactos y permite buscar por nombre o correo.
    """
    busqueda = request.GET.get("buscar", "").strip()

    contactos = Contacto.objects.all()

    # Estructura de decisión: solo se filtra cuando el usuario escribe algo.
    if busqueda:
        contactos = contactos.filter(
            nombre__icontains=busqueda
        ) | contactos.filter(
            correo__icontains=busqueda
        )

    contexto = {
        "contactos": contactos,
        "busqueda": busqueda,
        "cantidad": contactos.count(),
    }

    return render(request, "contactos/lista.html", contexto)


def agregar_contacto(request):
    """Procesa el formulario para crear un nuevo contacto."""

    if request.method == "POST":
        formulario = ContactoForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Contacto agregado correctamente.")
            return redirect("lista_contactos")
    else:
        formulario = ContactoForm()

    return render(
        request,
        "contactos/formulario.html",
        {
            "formulario": formulario,
            "titulo": "Agregar contacto",
            "boton": "Guardar contacto",
        },
    )


def editar_contacto(request, contacto_id):
    """Permite modificar un contacto existente."""

    contacto = get_object_or_404(Contacto, id=contacto_id)

    if request.method == "POST":
        formulario = ContactoForm(request.POST, instance=contacto)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Contacto actualizado correctamente.")
            return redirect("lista_contactos")
    else:
        formulario = ContactoForm(instance=contacto)

    return render(
        request,
        "contactos/formulario.html",
        {
            "formulario": formulario,
            "titulo": "Editar contacto",
            "boton": "Actualizar contacto",
        },
    )


def eliminar_contacto(request, contacto_id):
    """Elimina un contacto después de confirmar."""

    contacto = get_object_or_404(Contacto, id=contacto_id)

    if request.method == "POST":
        contacto.delete()
        messages.success(request, "Contacto eliminado correctamente.")
        return redirect("lista_contactos")

    return render(
        request,
        "contactos/confirmar_eliminacion.html",
        {"contacto": contacto},
    )
