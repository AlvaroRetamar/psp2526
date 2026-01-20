from multiprocessing import Process, Pipe
import time

def sensor_movimiento(conexion):
    eventos = ["Normal", "Normal", "MOVIMIENTO DETECTADO", "Normal"]
    
    for evento in eventos:
        time.sleep(1)
        print(f"Sensor: Enviando estado... ({evento})")
        conexion.send(evento) # Enviamos datos por el tubo
        
        # Esperamos respuesta del monitor
        respuesta = conexion.recv() 
        print(f"Sensor: Recibida orden del monitor -> {respuesta}")
    
    conexion.close()

def monitor_seguridad(conexion):
    while True:
        try:
            dato = conexion.recv() # Recibimos datos del sensor
            if "MOVIMIENTO" in dato:
                conexion.send("ACTIVAR SIRENA 🔊")
            else:
                conexion.send("CONTINUAR VIGILANCIA ✅")
        except EOFError:
            break # El tubo se cerró

if __name__ == '__main__':
    # Creamos los dos extremos del tubo
    extremo_padre, extremo_hijo = Pipe()

    p1 = Process(target=sensor_movimiento, args=(extremo_hijo,))
    p2 = Process(target=monitor_seguridad, args=(extremo_padre,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()