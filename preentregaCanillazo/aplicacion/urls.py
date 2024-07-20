from django.urls import path, include
from aplicacion.views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    
    path('acerca/', acerca, name="acerca"),
    path('mas_info_contacto/', mas_info_contacto, name="mas_info_contacto"),
    
    #___________________________________________
    #_______________Compradores______________
    path('compradorForm/', compradorForm, name="compradorForm"),
    path('compradores/', compradores, name="compradores"),
    path('compradorUpdate/<id_comprador>/', compradorUpdate, name="compradorUpdate"),
    path('compradorDelete/<id_comprador>/', compradorDelete, name="compradorDelete"),

    
    #_______________Vendedores_____________
    path('vendedorForm/', vendedorForm, name="vendedorForm"),
    path('vendedores/', vendedores, name="vendedores"),
    path('vendedorUpdate/<id_vendedor>/', vendedorUpdate, name="vendedorUpdate"),
    path('vendedorDelete/<id_vendedor>/', vendedorDelete, name="vendedorDelete"),
    
    
    #______________Proveedores______________
    path('proveedorForm/', proveedorForm, name="proveedorForm"),
    path('proveedores/', proveedores, name="proveedores"),
    path('proveedorUpdate/<id_proveedor>/', proveedorUpdate, name="proveedorUpdate"),
    path('proveedorDelete/<id_proveedor>/', proveedorDelete, name="proveedorDelete"),
    

    
    #_______________Productos___________
    path('productoForm/', productoForm, name="productoForm"),
    path('productos/', productos, name="productos"),
    path('productoUpdate/<id_producto>/', productoUpdate, name="productoUpdate"),
    path('productoDelete/<id_producto>/', productoDelete, name="productoDelete"),

        
    #_______________Buscar__________
    path('buscar_productos/', buscar_productos , name="buscar_productos"),
    path('encontrar_productos/', encontrar_productos , name="encontrar_productos"),
    
    #_______________Login/Logout/Registro__________
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('registro/', register, name="registro"),


    #_______________Edicion de Perfil/Avatar______________
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),



    

]