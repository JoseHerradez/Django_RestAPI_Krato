# Django_RestAPI_Krato
Prueba tecnica utilizando Django y Django Rest Framework para Krono.

Tomé la decision de usar ViewSets porque facilitan la creacion de los endpoints para los distintos modelos dandote todas las rutas bases para obtener la información que se pide, permitiendo aun asi customizar distintas rutas para obtener otros resultados que se deseen como era este el caso.

Para el primer endpoint además de agregar los usuarios a la respuesta de cada tienda por id, utilizando:
  .../tiendas/pk/usuarios
Permite obtener todos los usuarios con su información respectiva asociados a la tienda especificada por el parametro "pk".

Para el segundo endpoint además de agregar las tiendas a la respuesta de cada usuario por id, utilizando:
  .../usuarios/pk/tiendas
Permite obtener todas las tiendas con su información respectiva asociadas al usuario especificado por el parametro "pk".

Para el tercer endpoint se necesitan dos parametros de entrada la ciudad y el usuario requerido para filtrar las tiendas, utilizando:
  .../ciudad/pk/usuarios/id
Permite obtener todas las tiendas pertenecientes a la ciudad indicada por "pk" y asociadas al usuario identificado por el parametro "id".

Por último a cada ViewSet se le agregó el mixin ListModel y RetrieveModel de manera de solamente permitir peticiones del tipo GET.

Superusuario: 
jose
Contraseña:
veronj24
