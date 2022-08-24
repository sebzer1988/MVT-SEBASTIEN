from re import T
from django.shortcuts import render
from .models import FamiliaHumano, FamiliaPerro
from django.http import HttpResponse
from django.template import Context, Template, loader


def plantilla_principal(request):
    duenio = FamiliaHumano(nombre="Sebastien", edad=34, fecha_nacimiento="1988-05-26" )
    esposa = FamiliaHumano(nombre="Selva Soledad", edad=31, fecha_nacimiento="1990-11-30")
    perro1 = FamiliaPerro(nombre="Luli", edad=4, fecha_nacimiento="2018-05-15")
    perro2 = FamiliaPerro(nombre="Moka", edad=2, fecha_nacimiento="2019-09-21")
    perro3 = FamiliaPerro(nombre="Bruna", edad=2, fecha_nacimiento="2019-09-21")
    perro4 = FamiliaPerro(nombre="Bella", edad=1, fecha_nacimiento="2020-10-22")

    duenio.save()
    esposa.save()
    perro1.save()
    perro2.save()
    perro3.save()
    perro4.save()

    duenio_infos = (duenio.nombre, duenio.edad, duenio.fecha_nacimiento)
    esposa_infos = (esposa.nombre, esposa.edad, esposa.fecha_nacimiento)
    perro1_infos = (perro1.nombre, perro1.edad, perro1.fecha_nacimiento)
    perro2_infos = (perro2.nombre, perro2.edad, perro2.fecha_nacimiento)
    perro3_infos = (perro3.nombre, perro3.edad, perro3.fecha_nacimiento)
    perro4_infos = (perro4.nombre, perro4.edad, perro4.fecha_nacimiento)


    diccionario={"jefe": duenio_infos , "mujer": esposa_infos, "perra1": perro1_infos, "perra2": perro2_infos, "perra3": perro3_infos, "perra4": perro4_infos}

    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)

    return HttpResponse(documento)