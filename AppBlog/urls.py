from django.urls import path
from AppBlog.views import PostCreate, PostDelete, PostDetail, PostList, PostUpdate, contact, inicio, login_request, post, register_request, resultadosBusqueda, usuario, about, nuevoPostForm
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('post/', post, name='Post'),
    path('profile/', usuario, name='Profile'),
    path('about/', about, name='About'),
    path('nuevoPostForm/', nuevoPostForm, name='nuevoPostForm'),
    path('resultadosBusqueda/', resultadosBusqueda, name='resultadosBusqueda'),
    path('contact/', contact, name='contact'),
   

    path('post/create', PostCreate.as_view(), name='post_create'),
    path('post/update/<pk>', PostUpdate.as_view(), name='post_update'),
    path('post/delete/<pk>', PostDelete.as_view(), name='post_delete'),
    path('post/<pk>', PostDetail.as_view(), name='post_detail'),

    path('login', login_request, name='login'),
    path('signup', register_request, name='signup'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='logout'),
]
