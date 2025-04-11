# ProyectoFinal

Python Comision 75140

Alumno: Ivan Leonel Gimenez

## De que trata el proyecto 

El proyecto que has creado en Django es una plataforma de interacción social donde los usuarios pueden registrarse, crear su perfil, y realizar publicaciones que pueden ser vistas y compartidas por otros usuarios. A través de esta página, los usuarios pueden compartir contenido, interactuar con las publicaciones de otros, y mantenerse conectados dentro de una comunidad en línea. Además, permite la personalización de los perfiles para que cada usuario pueda mostrar información personal y participar activamente en el sitio.

## Como Ejecutarlo

Para ejecutar tu proyecto Django que permite el inicio de sesión, registro, y visualizar publicaciones y perfiles, sigue estos pasos:

1. Instalar Dependencias
Asegúrate de tener Python y Django instalados. Si no los tienes, puedes instalar Django ejecutando el siguiente comando en tu terminal o consola:
pip install django 
Si tienes un entorno virtual configurado, activa el entorno antes de instalar las dependencias.

2. Configurar el Proyecto
Si aún no has creado la base de datos y las migraciones de tu proyecto, sigue estos pasos:

Abre una terminal y navega hasta el directorio de tu proyecto Django.

Realiza las migraciones para crear la base de datos:

python manage.py makemigrations
python manage.py migrate
Si tienes usuarios de prueba o datos predeterminados, puedes cargar datos iniciales si has configurado fixtures o datos predeterminados.

3. Crear Superusuario (Opcional)
Si deseas acceder al panel de administración de Django, puedes crear un superusuario:
python manage.py createsuperuser
Sigue las instrucciones en la terminal para crear un superusuario (nombre de usuario, correo electrónico y contraseña).

4. Ejecutar el Servidor
Una vez que todo esté configurado y las migraciones se hayan realizado, ejecuta el servidor de desarrollo de Django:
python manage.py runserver
Esto iniciará el servidor en el puerto predeterminado (por lo general, http://127.0.0.1:8000/).

5. Acceder a la Aplicación en el Navegador
Abre tu navegador y ve a la dirección:
http://127.0.0.1:8000/
Aquí podrás ver la página principal de tu aplicación.

6. Registrar Usuario
Haz clic en el enlace de Registro.

Completa el formulario de registro con un nombre de usuario, correo electrónico y contraseña.

Después de registrarte, serás redirigido al inicio de sesión o a la página de inicio si la redirección está configurada correctamente.

7. Iniciar Sesión
Haz clic en el enlace de Iniciar sesión.

Ingresa tus credenciales (nombre de usuario y contraseña) para acceder a tu cuenta.

8. Ver y Crear Publicaciones
Una vez que inicies sesión, podrás ver las publicaciones de otros usuarios y también crear nuevas publicaciones.

Usualmente, deberías tener una sección donde puedas escribir y publicar algo, así como una lista de publicaciones previas de otros usuarios.

9. Ver tu Perfil
En tu página de usuario, podrás acceder a tu perfil, donde puedes ver la información que has proporcionado y posiblemente editarla, dependiendo de la funcionalidad que hayas implementado.

10. Cerrar Sesión
Para cerrar sesión, simplemente haz clic en el enlace de Cerrar sesión en el menú de navegación.

## Mejoras a futuro

Estas son algunas ideas a futuro que podria llegar a realizar en este proyecto:
1. Comentarios en las Publicaciones
Permite que los usuarios dejen comentarios en las publicaciones de otros. Esto fomentaría la interacción entre los usuarios.

Funcionalidad: Los usuarios pueden comentar en las publicaciones de otros usuarios.

Características adicionales: Los comentarios podrían tener un sistema de votos o "me gusta" para resaltar los más populares.

2. Sistema de "Me Gusta" o Reacciones
Implementa un sistema donde los usuarios puedan dar "me gusta" a las publicaciones de otros, lo cual aumenta la interacción social.

Funcionalidad: Los usuarios pueden dar "me gusta" a una publicación.

Características adicionales: Añadir diferentes tipos de reacciones (ej. "me encanta", "me sorprende", "me entristece").

3. Sistema de Notificaciones
Introduce un sistema de notificaciones donde los usuarios puedan recibir alertas de actividades importantes, como nuevos comentarios en sus publicaciones, "me gusta", o nuevos seguidores.

Funcionalidad: Los usuarios reciben notificaciones para interacciones en su perfil y publicaciones.

Características adicionales: Un panel de notificaciones que permita gestionar y ver el historial.

4. Amigos o Seguidores
Agrega la opción de que los usuarios puedan agregar amigos o seguir a otros usuarios. Esto permitiría a los usuarios ver solo las publicaciones de las personas que siguen.

Funcionalidad: Los usuarios pueden seguir a otros y ver sus publicaciones en un feed.

Características adicionales: Permitir solicitudes de amistad, aceptación o rechazo.

5. Mensajería Directa
Implementa una funcionalidad de mensajería privada entre usuarios, lo que permitiría la comunicación directa sin salir del sitio.

Funcionalidad: Los usuarios pueden enviarse mensajes privados entre ellos.

Características adicionales: Crear un sistema de chat en tiempo real.

6. Sistema de Etiquetas o Hashtags
Añade un sistema de etiquetas o hashtags a las publicaciones, para que los usuarios puedan organizar y buscar contenido relevante.

Funcionalidad: Los usuarios pueden agregar hashtags a sus publicaciones.

Características adicionales: Implementar una página de "Explorar" donde los usuarios puedan buscar publicaciones por hashtags populares.

7. Editar Publicaciones
Permite a los usuarios editar sus publicaciones después de haberlas creado, en caso de que deseen corregir errores o agregar algo más.

Funcionalidad: Opción de editar las publicaciones existentes.

Características adicionales: Mostrar la fecha de la última edición.
