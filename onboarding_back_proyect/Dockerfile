FROM python:latest

# Evita que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos dependencias
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el proyecto
COPY . .

# Exponemos el puerto de Django
EXPOSE 8000

# Comando para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

