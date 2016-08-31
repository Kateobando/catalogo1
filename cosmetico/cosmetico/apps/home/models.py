from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):

	nombre			= models.CharField(max_length = 100)
	descripcion     = models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.nombre

class Marca(models.Model):

	nombre	        = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.nombre

class Color (models.Model):
	nombre          = models.CharField(max_length = 100)
	hexadecimal     = models.CharField(max_length = 100)

	def __unicode__ (self):
		return self.nombre

class Ingredientes (models.Model):
	descripcion     = models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.descripcion

class Advertencias (models.Model):
	descripcion     = models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.descripcion

class Cosmetico (models.Model):

	def url (self,filename):
		ruta = "MultimediaData/Cosmetico/%s/%s"%(self.nombre, str(filename))
		return ruta

	imagen			= models.ImageField(upload_to = url, null = True, blank =True)
	nombre			= models.CharField(max_length = 100)
	descripcion     = models.TextField(max_length = 500)
	precio			= models.DecimalField(max_digits = 6, decimal_places = 2)
	categorias		= models.ManyToManyField(Categoria, null = True, blank = True)
	marca			= models.ForeignKey(Marca)
	color           = models.CharField(max_length = 100)
	instrucciones   = models.TextField(max_length = 500)
	ingredientes    = models.TextField(max_length = 500)
	advertencias    = models.TextField(max_length = 500)
	cantidad        = models.CharField(max_length = 100)
	stock			= models.IntegerField()
	status			= models.BooleanField(default = True)

	def __unicode__ (self):
		return self.nombre


class user_profile(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return ruta

	user        =  models.OneToOneField(User)
	photo       =  models.ImageField(upload_to=url)
	telefono    =  models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username



