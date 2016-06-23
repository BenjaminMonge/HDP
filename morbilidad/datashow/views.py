# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse	
from django.db.models import Q
# The equivalent of the server page that distributes resources based or URI
#Here are the controllers too
from .models import Consulta, Enfermedad, Mes, Ano
import csv
import json

def index(request):
	return HttpResponse("Las rutas disponibles son /management /see /editeq /extrapolate. Este es el inicio")

def management(request):
	lista_consultas = []

   	if request.is_ajax():
	 Consulta.objects.all().delete()		
	 objs = json.loads(request.body)
	 limit =len(objs)
	 for x in range(0, limit):
	 	print(x)
	 	mascu = int(objs[x]["masculino"])
		feme = int(objs[x]["femenino"])
		m, created = Mes.objects.get_or_create(nombremes=objs[x]["mes"])
		an, created = Ano.objects.get_or_create(identi=int(objs[x]["agno"]))
		enf, created = Enfermedad.objects.get_or_create(nombreenf=objs[x]["enfermedad"])
		con, created = Consulta.objects.get_or_create(masculino=mascu, femenino=feme, ano=an, enfermedad=enf, mes=m)
		lista_consultas.append(con)
		m = None
		an =None
		enf = None
		context = {
			'lista_consultas' : lista_consultas
	    	}

	 return render(request, 'datashow/html/Agregar Datos.html', context)

	else:
		return render(request, 'datashow/html/Agregar Datos.html', {'lista_consultas' : Consulta.objects.all()}
)

def extrapolate(request):

	context = {
		'lista_consultas' : Consulta.objects.all()
	    }
	return render(request, 'datashow/html/layout.html', context)


def getData(request):
	toreturn = []	
	data1 = {'name':'Tokyo', 'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]}
	data2 = {'name':'New York', 'data': [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]}
	toreturn.append(data1)
	toreturn.append(data2)

	return JsonResponse(json.dumps(toreturn), safe=False)

def editeq(request):
	#do a 
	context = {

	}
	return render(request, 'datashow/html/Editar Ecuaciones.html', context)

def see(request):
	context = {
		'lista_consultas' : Consulta.objects.all()
	    }
	return render(request, 'datashow/html/Muestra de Consultas.html', context)
	


