from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Create your views here.
def cargarInicio(request):
    return render(request, 'inicio.html')

def enviar_correo(request):
    if request.method == "POST":
        destinatario = request.POST.get('email', 'juan-0927cacd@hotmail.com')  # Usa el correo del formulario
        asunto = "Confirmación de datos"
        mensaje = f"Hola, gracias por tu mensaje."

        if not destinatario:
            messages.error(request, "El correo electrónico es obligatorio.")
            return render(request, 'inicio.html')

        try:
            # Configurar el correo
            remitente = "proyectos@estanteriasdecolombia.com"  # Cambia por tu correo real
            password = "Email$Edc.8931"  # Cambia por tu contraseña real

            msg = MIMEMultipart()
            msg["From"] = remitente
            msg["To"] = destinatario
            msg["Subject"] = asunto
            msg.attach(MIMEText(mensaje, "plain", "utf-8"))

            # Iniciar conexión SMTP
            context = ssl.create_default_context()
            with smtplib.SMTP("smtp.estanteriasdecolombia.com", 587) as server:
                server.starttls(context=context)  # Cifrado seguro
                server.login(remitente, password)
                server.sendmail(remitente, destinatario, msg.as_string())

            messages.success(request, "Correo enviado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al enviar correo: {e}")

    return render(request, 'inicio.html')


def enviar_correoaaa(request):
    if request.method == 'POST':
        
        nombres = request.POST.get('firstName')
        apellidos = request.POST.get('lastName')
        email = request.POST.get('email')
        direccion = request.POST.get('address')
        pais = request.POST.get('country')
        municipio = request.POST.get('state')
        barrio = request.POST.get('zip')
        observaciones = request.POST.get('observaciones')

        asunto = "Nuevo formulario de contacto"
        mensaje = f"""
        Nombres: {nombres}
        Apellidos: {apellidos}
        Correo: {email}
        Dirección: {direccion}
        País: {pais}
        Municipio: {municipio}
        Barrio: {barrio}
        Observaciones: {observaciones}
        """
        print(nombres, apellidos , email)

        try:
            send_mail(
                asunto,
                mensaje,
                'proyectos@estanteriasdecolombia.com',  # Cambia esto por tu correo de envío
                ['juan-0927cacd@hotmail.com'],  # Cambia esto por el correo receptor
                fail_silently=False,
            )
            messages.success(request, "Correo enviado correctamente.")
        except Exception as e:
            messages.error(request, f"Error al enviar el correo: {e}")

        #return redirect('formulario')  # Reemplaza con el nombre de tu vista o URL

    return render(request, 'inicio.html')

#"prueba" de nuevo
