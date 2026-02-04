#from django.shortcuts import render

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
                nombre=data.get("nameOne"),
                othername=data.get("otherName"),
                apellido=data.get("firstSurname"),
                segundoapellido=data.get("secondSurname"),
                telefono=data.get("telephone"),
                direccion=data.get("address"),
                ciudad=data.get("city"),
                codigo_postal=data.get("postalCode"),
                cargo=data.get("position"),
                area=data.get("area"),
                numberEmployee=data.get("numberEmployee")
            )

            empleado.save()

            return JsonResponse({
                "mensaje": "Empleado agregado correctamente",
                "id": empleado.numberEmployee
            }, status=201)

        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=400)

    return JsonResponse({
        "error": "Método no permitido"
    }, status=405)

def consultar_empleado(request, numberEmployee):
    if request.method == "GET":
        try:
            empleado = Empleado.objects.get(
                numberEmployee=numberEmployee
            )

            return JsonResponse({
                "numberEmployee": empleado.numberEmployee,
                "nameOne": empleado.nombre,
                "otherName": empleado.othername,
                "firstSurname": empleado.apellido,
                "secondSurname": empleado.segundoapellido,
                "telephone": empleado.telefono,
                "address": empleado.direccion,
                "city": empleado.ciudad,
                "postalCode": empleado.codigo_postal,
                "position": empleado.cargo,
                "area": empleado.area,
                
            }, status=200)

        except Empleado.DoesNotExist:
            return JsonResponse({
                "error": "Empleado no encontrado"
            }, status=404)

    return JsonResponse({
        "error": "Método no permitido"
    }, status=405)

