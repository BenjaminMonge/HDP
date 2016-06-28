# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.db.models import Q	
# The equivalent of the server page that distributes resources based or URI
#Here are the controllers too
from .models import Consulta, Enfermedad, Mes, Ano, Ecuacion
import csv
import json
import parser
from numpy import array	
from scipy.optimize import leastsq

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
		datamasc = []
		datafem = []
		xlist = []
		total = []
		myeq = Ecuacion.objects.get(nombreec="Extrapolacion lineal").asig
		for y in range(0, len(dbdise[x])): #Extrayendo los datos de los objetos de la base
			#listacon.append(dbdise[x][y])
			xlist.append(int(y+1))
			datamasc.append(int(dbdise[x][y].masculino))
			datafem.append(int(dbdise[x][y].femenino))

		remasc = getValue(xlist, datamasc, 2016, myeq)#here you must extratpolate expol(datadb)		
		refem = getValue(xlist, datafem, 2016, myeq)#here you must extratpolate expol(datadb)
		meses = asignarMeses()
		#reformating the data
		for i in range(0, 12):
			listacon.append(Consulta(masculino=remasc[i], femenino=refem[i], ano=Ano(identi=2017), enfermedad=dbdise[x][0].enfermedad, mes=meses[i]))
			total.append(remasc[i]+refem[i])

		graphd = {'name': dbdise[x][0].enfermedad.nombreenf, 'data': total}

		toreturn.append(graphd)

	context = {
		'lista_consultas' : listacon,
		'graphdata' : json.dumps(toreturn, ensure_ascii=True).encode("utf8")
	    }
	return render(request, 'datashow/html/layout.html', context)


def editeq(request):
	#do a 
	context	 = {
		
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

def getValue(dx, dy, year, myeq):
	list_interpol = []
	xi=array(dx)
	yi=array(dy)

	afir, bfir = 1.0, 1.0

	sol = leastsq(error, [afir, bfir], args=(xi, yi, myeq))	
	a = sol[0][0]
	b = sol[0][1]
	uplimit = 12*(year-2015)
	for x in range(0, 12*(year-2015)):
  		res = eval(myeq)
		list_interpol.append(int(res))

	return list_interpol[(uplimit-12):uplimit]	

def error(parametros,x,y, myeq):
  ''' El error se define pasando primero los parámetros y luego los vectores a ajustar '''
  a,b = parametros
  ec = myeq
  equation = y - eval(ec)
  return equation

def asignarMeses():
	meses = []
	meses.append(Mes(nombremes='Enero'))
	meses.append(Mes(nombremes='Febrero'))
	meses.append(Mes(nombremes='Marzo'))
	meses.append(Mes(nombremes='Abril'))
	meses.append(Mes(nombremes='Mayo'))
	meses.append(Mes(nombremes='Junio'))
	meses.append(Mes(nombremes='Julio'))
	meses.append(Mes(nombremes='Agosto'))
	meses.append(Mes(nombremes='Septiembre'))
	meses.append(Mes(nombremes='Octubre'))
	meses.append(Mes(nombremes='Noviembre'))
	meses.append(Mes(nombremes='Diciembre'))

	return meses


