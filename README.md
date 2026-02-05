# Práctica 10 - Proxy Inverso y Caché (SAD)

Este proyecto implementa una infraestructura de microservicios utilizando **Docker Compose**, diseñada para maximizar la alta disponibilidad y la seguridad perimetral mediante el uso de **Nginx** como proxy inverso y **Redis** como caché de segundo nivel.

## 1. Estructura del Repositorio
* `api/`: Contiene el backend en Flask (Python) y su Dockerfile.
* `nginx.conf`: Configuración del proxy inverso y caché L1.
* `docker-compose.yml`: Orquestación de los servicios.
* `.gitignore`: Exclusión de archivos innecesarios.

## 2. Arquitectura del Sistema
El flujo de una petición sigue este orden:
1. **Cliente** -> Realiza petición al puerto 80.
2. **Nginx (Caché L1)** -> Si el dato está en caché (60s), lo devuelve instantáneamente.
3. **Flask API** -> Si Nginx no lo tiene, la API procesa la petición.
4. **Redis (Caché L2)** -> La API consulta a Redis antes de simular el proceso lento (2s).

## 3. Instrucciones de Despliegue
Para poner en marcha el entorno, clona el repositorio y ejecuta:

```bash
docker-compose up -d --build