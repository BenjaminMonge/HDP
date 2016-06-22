#from __future__ import unicode_literals

from django.db import models

# Create your models here. #Logic of the program

class Ano(models.Model):
	identi = models.CharField(max_length=6, primary_key=True)
	def __str__(self):
		return str(self.identi)

class Mes(models.Model):
	nombremes = models.CharField(max_length=15, primary_key=True)
	def __str__(self):
		return self.nombremes

class Enfermedad(models.Model):
	nombreenf = models.CharField(max_length=50, primary_key=True)
	def __str__(self):
		return self.nombreenf	


class Consulta(models.Model):
	ano = models.ForeignKey(Ano, on_delete=models.CASCADE)
	enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE)
	mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
	masculino = models.IntegerField(default=0)
	femenino = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)
		
	def subtotal(self):
	 return self.masculino + self.femenino


