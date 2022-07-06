from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse_lazy

from AppBlog.models import Post, Usuario
from AppBlog.forms import NuevoPostForm, UserRegistrationForm

from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def inicio(self):
    plantilla = loader.get_template('AppBlog/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def post(request):
    return render (request, 'appBlog/post.html')


def usuario(request):   
    return render (request, 'appBlog/profile.html')

def about(request):
    return render (request, 'appBlog/about.html')

def contact(request):
    return render (request, 'appBlog/contact.html')

def nuevoPostForm(request):
    if request.method == 'POST':
        miFormulario = NuevoPostForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        titulo = informacion['titulo']
        subtitulo = informacion['subtitulo']
        autor = informacion['autor']
        fecha = informacion['fecha']
        resenia = informacion['reseña']
        post = Post(titulo=titulo, subtitulo=subtitulo, autor=autor, fecha=fecha, resenia=resenia)
        post.save()
        return render (request, 'AppBlog/.html')
    else:
        miFormulario = NuevoPostForm()    
    return render (request, 'appBlog/nuevoPostForm.html', {'miFormulario': miFormulario})

def resultadosBusqueda(request):
    return render(request, 'appBlog/resultadosBusqueda.html')

def buscar(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        post = Post.objects.filter(titulo=titulo)
        return render(request, 'appBlog/resultadosBusqueda.html', {'post': post, 'titulo': titulo})
    else:
        respuesta = "Su busqueda no existe"
    return HttpResponse(respuesta)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

class PostList(ListView):
    model = Post
    template_name = 'AppBlog/inicio.hmtl'

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy('Inicio')
    fields = ['titulo', 'subtitulo', 'resenia', 'autor', 'fecha', 'resenia']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('Inicio')

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy('Inicio')
    fields = ['titulo', 'subtitulo', 'resenia', 'autor', 'fecha', 'resenia']

class PostDetail(DetailView):
    model = Post
    template_name = 'AppBlog/post.hmtl'
    
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////    

def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render (request, 'AppBlog/profile.html', {'mensaje': f'Bienvenido {usuario}'})
            else:
                return render (request, 'AppBlog/profile.html', {'mensaje': 'Datos incorrectos'})
        else:
            return render (request, 'AppBlog/profile.html', {'mensaje': 'Error, datos invalidos'})
    else:
        form = AuthenticationForm()
        return render (request, 'AppBlog/login.html', {'form':form})

def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request, 'AppBlog/inicio.html', {'mensaje': f'Usuario {username} creado con exito!'})
        else:
            return render (request, 'AppBlog/inicio.html', {'mensaje': 'Error al crear el usuario'})
    else:
        form = UserRegistrationForm()
        return render(request, 'AppBlog/signup.html', {'form':form})


