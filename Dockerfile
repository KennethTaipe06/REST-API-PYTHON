# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y el código de la aplicación al contenedor
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Define el comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]