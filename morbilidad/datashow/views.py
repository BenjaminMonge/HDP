# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
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
	listacon = []
	toreturn = []	
	dbdise = getDisease()
	for x in range(0, len(dbdise)):
		datadb = []
		for y in range(0, len(dbdise[x])):
			listacon.append(dbdise[x][y])
			datadb.append(int(dbdise[x][y].masculino)+int(dbdise[x][y].femenino))	
		ranvar = {'name': dbdise[x][0].enfermedad.nombreenf, 'data': datadb}
		toreturn.append(ranvar)	

	context = {
		'lista_consultas' : listacon,
		'graphdata' : json.dumps(toreturn, ensure_ascii=True).encode("utf8")
	    }
	return render(request, 'datashow/html/layout.html', context)


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
	
def getDisease():
	topdiseases = []
	cursor = connection.cursor()
	cursor.execute("select *, (fem+mas) as total from (select enfermedad_id, sum(femenino) as fem, sum(masculino) as mas from (select * from datashow_consulta where ano_id=2015 order by enfermedad_id) as dis group by dis.enfermedad_id) as sums order by total desc limit 5")
	enfermedades = cursor.fetchall()
	for p in enfermedades:
		adise = Consulta.objects.filter(Q(enfermedad_id__exact=p[0]), Q(ano_id=2015)).distinct()
		topdiseases.append(adise)

	return topdiseases


