# estancol

#Inicializadores de proyecto
#django-admin startproject estancol .

python manage.py startapp inicio
python manage.py startapp nosotros
python manage.py startapp servicios
python manage.py startapp productos
python manage.py startapp contactenos


#django-admin startproject estancol .

python manage.py startapp task - Creacion de una nueva aplicacion
python manage.py migrate - Migra los datos al servidor de sql lite
python manege.py makemigrations - cuando se crea una nueva tabla y se debe correr de nuevo el migrate
python manage.py createsuperuser - Para crear super usuario de SQLlite
python manage.py runserver - ejecuta el servidor

---Entorno virtual 

pip install virtualenv

** En la carpeta ejecutar el comando

python -m venv venv - Para crear el entorno 

.\venv\Scripts\activate - Activa el entorno 
deactivate - Apaga el entorno virtual

pip install -r .\requerements.txt - Instala las dependencias en el entorno virutal 



Este codigo es para siempre ponerlo antes de terminar el push
python manage.py collectstatic

este codigo es para cuando eliminamos la carpeta del servidor
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
pip install gunicorn
gunicorn --workers 3 estancol.wsgi:application
