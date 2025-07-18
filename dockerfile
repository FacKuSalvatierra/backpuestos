# Usa una imagen oficial de Python como base
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto
COPY . .

# Expone el puerto (Render asignará el puerto automáticamente)
EXPOSE $PORT

# Comando para producción
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]