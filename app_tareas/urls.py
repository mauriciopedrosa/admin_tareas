from django.urls import path
from .views import CrearArea, EditarArea, EditarUsuario, EliminarArea, ListaAreas, ListaUsuarios, home, CrearCategoria,  DetalleCategoria,  EditarCategoria,  EliminarCategoria,  ListaCategorias,   ListaTareas,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea, Logueo, registro, tarea, about
from .views import home, CrearCategoria,  DetalleCategoria,  EditarCategoria, EliminarCategoria,  ListaCategorias,  ListaTareas,DetalleTarea,CrearTarea,EditarTarea, EliminarTarea, Logueo, registro, tarea, about,agregar_avatar, EliminarAvatar
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name ='home'), 
    path('login/', Logueo.as_view(), name ='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name ='logout'),   
    path('registro/', registro, name ='registro'),   
    path('about/', about, name ='about'),   
    # --------- TAREAS ------------
    path('tareas/', ListaTareas.as_view(), name ='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name ='tarea'),
    path('crear_tarea/', CrearTarea.as_view(), name ='crear_tarea'),
    path('editar_tarea/<int:pk>', EditarTarea.as_view() , name ='editar_tarea'),
    path('eliminar_tarea/<int:pk>', EliminarTarea.as_view(), name ='eliminar_tarea'), 
    path('tarea_usuario/<int:usuario_id>', tarea , name ='tarea_usuario'),
    
    #---------- CATEGORIAS -----------
    path('categorias/', ListaCategorias.as_view(), name ='categorias'),       
    path('categoria/<int:pk>', DetalleCategoria.as_view(), name ='categoria'),           
    path('crear_categoria/', CrearCategoria.as_view(), name ='crear_categoria'),
    path('editar_categoria/<int:pk>', EditarCategoria.as_view(), name ='editar_categoria'),
    path('eliminar_categoria/<int:pk>', EliminarCategoria.as_view(), name ='eliminar_categoria'),  
    
    #---------- AREAS -----------
    path('areas/', ListaAreas.as_view(), name ='areas'),       
    path('crear_area/', CrearArea.as_view(), name ='crear_area'),
    path('editar_area/<int:pk>', EditarArea.as_view(), name ='editar_area'),
    path('eliminar_area/<int:pk>', EliminarArea.as_view(), name ='eliminar_area'),  
    
    
    # -----------USUARIOS ---------------
    path('usuarios/', ListaUsuarios.as_view(), name ='usuarios'),        
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(), name ='editar_usuario'),
    path('agregar_avatar/', agregar_avatar, name='agregar_avatar'),
    path('eliminar_avatar/<int:pk>', EliminarAvatar.as_view(), name='eliminar_avatar'),
]
