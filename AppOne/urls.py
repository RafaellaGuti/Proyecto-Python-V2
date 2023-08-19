from django.urls import path
from AppOne import views
from django.contrib.auth.views import LogoutView



urlpatterns = [

    path('', views.inicio, name='Inicio'),
    path('productos/', views.productos, name='Productos'),
    path('servicios/', views.servicios, name='Servicios'),
    path('clientes/', views.clientes, name='Clientes'),
    path('busquedacategoria/', views.busquedacategoria, name='Busquedacategoria'),
    path('buscar/', views.buscar, name='Buscar'),

    #path('productosform/', views.productosform, name= 'Productosform'),
    #path('serviciosform/', views.serviciosform, name= 'Serviciosform'),
    #path('clientesform/', views.clientesform, name= 'Clientesform'),

    path('productos/list', views.Productoslist.as_view(), name='List'),
    path('<int:pk>', views.Productosdetalle.as_view(), name='Detail'),
    path('nuevo', views.Productoscreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.Productosupdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.Productosdelete.as_view(), name='Delete'),
    path('categoriasproductos/', views.CategoriaspList.as_view(), name='categoriasp_list'),
    path('productos/<str:categoria>/', views.ProductosPorCategoria.as_view(), name='productos_por_categoria'),

    path('servicios/list', views.Servicioslist.as_view(), name='Slist'),
    path('servicios/<int:pk>', views.Serviciosdetalle.as_view(), name='Sdetail'),
    path('servicios/editar/<int:pk>', views.Serviciosupdate.as_view(), name='Sedit'),
    path('servicios/borrar/<int:pk>', views.Serviciosdelete.as_view(), name='Sdelete'),
    path('categoriasservicios/', views.CategoriassList.as_view(), name='categoriass_list'),
    path('servicios/<str:categoria>/', views.ServiciosPorCategoria.as_view(), name='servicios_por_categoria'),

    
    path('register', views.register, name= 'Register'),
    path('editarperfil', views.editarPerfil, name='Editarperfil'),
    path('about', views.about, name= 'About'),
    path('paginacons', views.paginacons, name= 'Paginacons'),
    
    ]
