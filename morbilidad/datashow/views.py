from django.shortcuts import render
from django.http import HttpResponse
# The equivalent of the server page that distributes resources based or URI
#Here are the controllers too
from .models import Consulta, Enfermedad, Mes, Ano
import csv
import json

if Consulta.objects.all():
	lista_consultas = Consulta.objects.all()
else:
	lista_consultas = []

def index(request):
	return HttpResponse("Las rutas disponibles son /management /see /editeq /extrapolate. Este es el inicio")

def management(request):

	if request.POST and request.FILES:
		print('uploaded something')
		file = request.FILES['csv_file']
		data = [row for row in csv.reader(file.read().splitlines())]
		limit = len(data)
		for x in range(0, limit): 
   			m = Mes(nombremes=data[x][3])
   			an = Ano(identi=data[x][4])
   			enf = Enfermedad(nombreenf=data[x][0])			
			con = Consulta(masculino=int(data[x][1]), femenino=int(data[x][2]), mes=m, ano=an, enfermedad=enf) 

			lista_consultas.append(con)
		

	if request.is_ajax():
		if request.body:
			Consulta.objects.all().delete()
		if lista_consultas:
			del lista_consultas[:]
		print('all saved')		
		objs = json.loads(request.body)
		for x in range(0, len(objs)):
		 	mascu = int(objs[x]["masculino"])
		 	feme = int(objs[x]["femenino"])
		 	m = Mes(nombremes=objs[x]["mes"])
		 	m.save()
		 	an = Ano(identi=objs[x]["agno"])
		 	an.save()
		 	enf = Enfermedad(nombreenf=objs[x]["enfermedad"])
		 	enf.save()
		 	con = Consulta(masculino=mascu, femenino=feme, ano=an, enfermedad=enf, mes=m)
		 	con.save()
		 	lista_consultas.append(con)
			
		
	context = {
		'lista_consultas' : lista_consultas
	    }

	return render(request, 'datashow/html/Agregar Datos.html', context)

def extrapolate(request):
	#year = json.load(request.body)
	#Consulta.objects.all().filter(ano=year)
	#do a 
	context = {
		'lista_consultas' : Consulta.objects.all()
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
	


