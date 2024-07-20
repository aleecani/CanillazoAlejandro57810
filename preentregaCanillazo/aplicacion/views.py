from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login,authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.views import PasswordChangeView 

from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required 

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")


def acerca(request):
    return render(request, "aplicacion/acerca.html")

def mas_info_contacto(request):
    return render(request, "aplicacion/mas_info_contacto.html")

#_______________________________________________________________________________


#______________Compradores___________

@login_required
def compradores(request):
    contexto = {"compradores": Comprador.objects.all()}
    return render(request, "aplicacion/compradores.html", contexto)

@login_required
def compradorForm(request):
    if request.method == "POST":
        miForm = CompradorForm(request.POST)
        if miForm.is_valid():
            comprador_nombre = miForm.cleaned_data.get("nombre")
            comprador_domicilio = miForm.cleaned_data.get("domicilio")
            comprador_nro_documento = miForm.cleaned_data.get("nro_documento")
            comprador = Comprador(nombre=comprador_nombre,domicilio=comprador_domicilio,nro_documento=comprador_nro_documento)
            comprador.save()
            contexto = {"compradores": Comprador.objects.all()}
            return render(request, "aplicacion/compradores.html", contexto)
    else:
        miForm = CompradorForm()
    
    return render(request,'aplicacion/compradorForm.html', {"form": miForm})

@login_required
def compradorUpdate(request, id_comprador):

    comprador = Comprador.objects.get(id=id_comprador)

    if request.method == "POST":
        miForm = CompradorForm(request.POST)
        if miForm.is_valid():
            comprador.nombre = miForm.cleaned_data.get("nombre")
            comprador.domicilio = miForm.cleaned_data.get("domicilio")
            comprador.nro_documento = miForm.cleaned_data.get("nro_documento")
            comprador.save()
            contexto = {"compradores": Comprador.objects.all()}
            return render(request, "aplicacion/compradores.html", contexto)    

    else:

        miForm = CompradorForm(initial={"nombre": comprador.nombre, "domicilio": comprador.domicilio ,"nro_documento": comprador.nro_documento}) 

    

    return render(request, "aplicacion/compradorForm.html", {"form": miForm})

@login_required
def compradorDelete(request, id_comprador):

    comprador = Comprador.objects.get(id=id_comprador)

    comprador.delete()

    contexto = {"compradores": Comprador.objects.all() }

    return render(request, "aplicacion/compradores.html", contexto)


#___________Vendedores____________

@login_required
def vendedores(request):
    contexto = {"vendedores": Vendedor.objects.all()}
    return render(request, "aplicacion/vendedores.html",contexto)

@login_required
def vendedorForm(request):
    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        if miForm.is_valid():
            vendedor_nombre = miForm.cleaned_data.get("nombre")
            vendedor_nro_documento = miForm.cleaned_data.get("nro_documento")
            vendedor = Vendedor(nombre=vendedor_nombre,nro_documento=vendedor_nro_documento)
            vendedor.save()
            contexto = {"vendedores": Vendedor.objects.all()}
            return render(request, "aplicacion/vendedores.html", contexto)
    else:
        miForm = VendedorForm()
    
    return render(request,'aplicacion/vendedorForm.html', {"form": miForm})


@login_required
def vendedorUpdate(request, id_vendedor):

    vendedor = Vendedor.objects.get(id=id_vendedor)

    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        if miForm.is_valid():
            vendedor.nombre = miForm.cleaned_data.get("nombre")
            vendedor.nro_documento = miForm.cleaned_data.get("nro_documento")
            vendedor.save()
            contexto = {"vendedores": Vendedor.objects.all()}
            return render(request, "aplicacion/vendedores.html", contexto)    

    else:

        miForm = VendedorForm(initial={"nombre": vendedor.nombre, "nro_documento": vendedor.nro_documento}) 

    

    return render(request, "aplicacion/vendedorForm.html", {"form": miForm})

@login_required
def vendedorDelete(request, id_vendedor):

    vendedor = Vendedor.objects.get(id=id_vendedor)

    vendedor.delete()

    contexto = {"vendedores": Vendedor.objects.all() }

    return render(request, "aplicacion/vendedores.html", contexto)


#___________Proveedores__________

@login_required
def proveedores(request):
    contexto = {"proveedores": Proveedor.objects.all()}
    return render(request, "aplicacion/proveedores.html",contexto)

@login_required
def proveedorForm(request):
    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        if miForm.is_valid():
            proveedor_nombre = miForm.cleaned_data.get("nombre")
            proveedor_domicilio = miForm.cleaned_data.get("domicilio")
            proveedor_nro_cuil = miForm.cleaned_data.get("nro_cuil")
            proveedor = Proveedor(nombre=proveedor_nombre,domicilio=proveedor_domicilio ,nro_cuil=proveedor_nro_cuil)
            proveedor.save()
            contexto = {"proveedores": Proveedor.objects.all()}
            return render(request, "aplicacion/proveedores.html", contexto)
    else:
        miForm = ProveedorForm()

    return render(request,'aplicacion/proveedorForm.html', {"form": miForm})

@login_required
def proveedorUpdate(request, id_proveedor):

    proveedor = Proveedor.objects.get(id=id_proveedor)

    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        if miForm.is_valid():
            proveedor.nombre = miForm.cleaned_data.get("nombre")
            proveedor.domicilio = miForm.cleaned_data.get("domicilio")
            proveedor.nro_cuil = miForm.cleaned_data.get("nro_cuil")
            proveedor.save()
            contexto = {"proveedores": Proveedor.objects.all()}
            return render(request, "aplicacion/proveedores.html", contexto)    

    else:

        miForm = ProveedorForm(initial={"nombre": proveedor.nombre, "domicilio":proveedor.domicilio , "nro_cuil": proveedor.nro_cuil}) 

    

    return render(request, "aplicacion/proveedorForm.html", {"form": miForm})

@login_required
def proveedorDelete(request, id_proveedor):

    proveedor = Proveedor.objects.get(id=id_proveedor)

    proveedor.delete()

    contexto = {"proveedores": Proveedor.objects.all() }

    return render(request, "aplicacion/proveedores.html", contexto)



#___________Productos____________

@login_required
def productos(request):
    contexto = {"productos": Producto.objects.all()}
    return render(request, "aplicacion/productos.html",contexto)

@login_required
def productoForm(request):
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_nro_item = miForm.cleaned_data.get("nro_item")
            producto_precio = miForm.cleaned_data.get("precio")
            producto = Producto(nombre=producto_nombre,nro_item=producto_nro_item,precio=producto_precio)
            producto.save()
            contexto = {"productos": Producto.objects.all()}
            return render(request, "aplicacion/productos.html")
    else:
        miForm = ProductoForm()
    
    return render(request,'aplicacion/productoForm.html', {"form": miForm})

@login_required
def productoUpdate(request, id_producto):

    producto = Producto.objects.get(id=id_producto)

    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto.nombre = miForm.cleaned_data.get("nombre")
            producto.nro_item = miForm.cleaned_data.get("nro_item")
            producto.precio = miForm.cleaned_data.get("precio")
            producto.save()
            contexto = {"productos": Producto.objects.all()}
            return render(request, "aplicacion/productos.html", contexto)    

    else:

        miForm = ProductoForm(initial={"nombre": producto.nombre, "nro_item": producto.nro_item, "precio": producto.precio}) 

    

    return render(request, "aplicacion/productoForm.html", {"form": miForm})

@login_required
def productoDelete(request, id_producto):

    producto = Producto.objects.get(id=id_producto)

    producto.delete()

    contexto = {"productos": Producto.objects.all() }

    return render(request, "aplicacion/productos.html", contexto)



#____________________________Buscador

@login_required
def buscar_productos(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def encontrar_productos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains = patron)
        contexto = {'productos': productos}
    else:
        contexto = {'productos': Producto.objects.all()}
    
    return render(request, 'aplicacion/productos.html', contexto)


#__________________________Login/Logout/Registración

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            #_____Leer avatar______
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            
            #___________________________________
            return render(request,"aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm() 
        
    return render(request, "aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:
        miForm = RegistroForm() 
        
    return render(request, "aplicacion/registro.html", {"form": miForm})



#__________Edicion de Perfil/Avatar_______________

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")            
            user.last_name = miForm.cleaned_data.get("last_name")            
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_______Borrar avatares viejos_______
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            
            #_____Enviar la imagen al home________________
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #______________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm})