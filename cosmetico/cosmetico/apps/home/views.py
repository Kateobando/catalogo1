from django.shortcuts import render_to_response
from django.template import RequestContext
from cosmetico.apps.home.forms import *
from cosmetico.apps.home.models import *
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))


def single_cosmetic_view(request, id_prod):
	prod = Cosmetico.objects.get(id = id_prod) 
	ctx = {'cosmetico':prod}
	return render_to_response('home/single_cosmetico.html',ctx,context_instance = RequestContext(request))

def single_marca_view(request, id_prod):
	prod = Marca.objects.get(id = id_prod) 
	ctx = {'marca':prod}
	return render_to_response('home/single_marca.html',ctx,context_instance = RequestContext(request))

def single_categoria_view(request, id_prod):
	prod = Categoria.objects.get(id = id_prod) 
	ctx = {'categoria':prod}
	return render_to_response('home/single_categoria.html',ctx,context_instance = RequestContext(request))

def single_color_view(request, id_prod):
	prod = Color.objects.get(id = id_prod) 
	ctx = {'color':prod}
	return render_to_response('home/single_color.html',ctx,context_instance = RequestContext(request))

def single_ingredientes_view(request, id_prod):
	prod = Ingredientes.objects.get(id = id_prod) 
	ctx = {'ingredientes':prod}
	return render_to_response('home/single_ingredientes.html',ctx,context_instance = RequestContext(request))

def single_advertencias_view(request, id_prod):
	prod = Advertencias.objects.get(id = id_prod) 
	ctx = {'advertencias':prod}
	return render_to_response('home/single_advertencias.html',ctx,context_instance = RequestContext(request))


def cosmeticos_view(request, pagina):
	lista_prod = Cosmetico.objects.filter(status = True) 
	paginator = Paginator(lista_prod, 5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		cosmeticos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		cosmeticos = paginator.page(paginator.num_pages)

	ctx = {'cosmeticos' :cosmeticos}
	return render_to_response ('home/cosmeticos.html', ctx, context_instance = RequestContext(request))


def login_view(request):
	mensaje = ""
	if request.user.is_authenticated(): #verificamos si el usuario ya esta authenticado o logueado
		return HttpResponseRedirect('/') #si esta logueado lo redirigimos a la pagina pricipal
	else: #si no esta authenticado
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
	formulario = Login_form()
	ctx = {'form':formulario, 'mensaje':mensaje}
	return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/') 


def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
