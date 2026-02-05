# Práctica 10: Proxy Inverso, Caché y Seguridad Perimetral
**Asignatura:** Seguridad y Alta Disponibilidad (SAD)  
**Autor:** Mario Garvin

## 1. Descripción del Proyecto
Este proyecto despliega una infraestructura de microservicios mediante **Docker Compose**. El objetivo es implementar un sistema de alta disponibilidad con dos niveles de caché y aislamiento de servicios para garantizar la seguridad perimetral.

## 2. Arquitectura y Tecnologías
La infraestructura se compone de tres servicios integrados en una red privada:

* **Nginx (Proxy Inverso):** Actúa como único punto de entrada (Puerto 80). Implementa la **Caché de Nivel 1** (60 segundos).
* **Flask API (Backend):** Procesa las peticiones y gestiona la **Caché de Nivel 2**.
* **Redis:** Almacén de datos en memoria para la persistencia de la caché de nivel 2.

## 3. Instrucciones de Despliegue
Para levantar el entorno completo desde cero, ejecuta:

```bash
sudo docker compose up -d --build