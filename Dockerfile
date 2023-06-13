FROM python:3.10

ENV PYTHONUNBUFFERED=1
# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar archivos requeridos al contenedor
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install -r requirements.txt

# Copiar el resto de los archivos al contenedor
COPY . .

# Configurar el comando de inicio del contenedor
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Dar permisos de ejecución al archivo .sh
#RUN chmod +x /app/comands.sh

# Ejecutar el archivo .sh
#CMD ["/app/comands.sh"]
COPY ./store/comands.sh /
ENTRYPOINT [ "sh", "/app/store/comands.sh" ]