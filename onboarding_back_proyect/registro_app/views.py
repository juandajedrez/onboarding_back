from django.shortcuts import render

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Empleado

# Create your views here.
@csrf_exempt
def agregar_empleado(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            empleado = Empleado(
                nombre=data.get("nombre"),
                apellido=data.get("apellido"),
                telefono=data.get("telefono"),
                direccion=data.get("direccion"),
                ciudad=data.get("ciudad"),
                codigo_postal=data.get("codigo_postal"),
                cargo=data.get("cargo"),
                area=data.get("area"),
                numero_identificacion=data.get("numero_identificacion")
            )

            empleado.save()

            return JsonResponse({
                "mensaje": "Empleado agregado correctamente",
                "id": empleado.id
            }, status=201)

        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=400)

    return JsonResponse({
        "error": "Método no permitido"
    }, status=405)

def consultar_empleado(request, numero_identificacion):
    if request.method == "GET":
        try:
            empleado = Empleado.objects.get(
                numero_identificacion=numero_identificacion
            )

            return JsonResponse({
                "id": empleado.id,
                "nombre": empleado.nombre,
                "apellido": empleado.apellido,
                "telefono": empleado.telefono,
                "direccion": empleado.direccion,
                "ciudad": empleado.ciudad,
                "codigo_postal": empleado.codigo_postal,
                "cargo": empleado.cargo,
                "area": empleado.area,
                "numero_identificacion": empleado.numero_identificacion
            }, status=200)

        except Empleado.DoesNotExist:
            return JsonResponse({
                "error": "Empleado no encontrado"
            }, status=404)

    return JsonResponse({
        "error": "Método no permitido"
    }, status=405)

