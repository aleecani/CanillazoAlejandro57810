- Ésta aplicación simula el entorno de una tienda, en donde los administradores con acceso a la página pueden crear y modificar los registros de productos y personas que operen en esa tienda.

- Utilicé un template descargado desde 'startbootstrap.com', al cual le eliminé varios archivos estáticos y botones que consideraba innecesarios.
- Le agregué 3 modelos que simulan el entorno de una tienda virtual, los cuáles  son:
Comprador, Vendedor, Producto. (Éstos se pueden encontrar en el 'models.py' en la carpeta 'templates/aplicacion/' dentro de la aplicación del proyecto)
- Creé los formularios correspondientes para cada modelo, se encuentran en la misma carpeta de los modelos originales ('templates/aplicacion/').
- También desarrollé una función de 'Busqueda', a la cuál nombré 'buscar_productos' y sirve únicamente para Productos. Trabaja en conjunto con la función 'encontrar_productos'.
- Edité el 'index.html' para que funcione con mis archivos estáticos.
- Agregué un menú que contiene un apartado de 'Acerca' y 'Más info. de Contacto', donde los clientes pueden obtener ayuda adicional.
- Agregué botones para facilitar las interacciones de los usuarios con el entorno, y así poder acceder más fácil a las funciones de la página.(La mayoría de funciones están hechas sin aprovechar el CBV de Django,lo hice así porque estoy añadiendo ésto a el proyecto de mi 3er preentrega y quería que se mantengan en el mismo formato.)
- Modifiqué la página para que sólo los usuarios que iniciaron sesión y tienen una cuenta registrada puedan ver el contenido completo de la página.
- Los usuarios que lo deseen podrán modificar sus datos personales y su contraseña en el apartado de 'Perfil' en la parte superior de la página.