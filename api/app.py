from flask import Flask
import redis
import time

app = Flask(__name__)

# Conexión a Redis usando el nombre del servicio definido en docker-compose
# Redis actúa como Caché de Nivel 2 [cite: 50, 51, 63]
cache = redis.Redis(host='redis-server', port=6379)

@app.route('/')
def index():
    # 1. Intentar obtener el dato de Redis (Caché L2)
    val = cache.get('mi_dato')
    if val:
        return f"Respuesta (HIT en L2 - Redis): {val.decode('utf-8')}"

    # 2. Si no está en caché, simulamos un proceso lento de 2-3 segundos [cite: 68]
    time.sleep(2)
    resultado = "Información procesada por la API"

    # 3. Guardar el resultado en Redis para futuras peticiones
    cache.setex('mi_dato', 60, resultado)
    return f"Proceso lento finalizado (MISS): {resultado}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)