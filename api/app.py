from flask import Flask
import redis
import time

app = Flask(__name__)

cache = redis.Redis(host='redis-server', port=6379)

@app.route('/')
def index():

    val = cache.get('mi_dato')
    
    if val:

        return f"RESPUESTA: {val.decode('utf-8')} (HIT en Nivel 2 - Redis)"

   
    time.sleep(2) 
    resultado = "Información procesada por la API"
    

    cache.setex('mi_dato', 60, resultado)
    
    return f"Proceso lento finalizado (MISS): {resultado}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)