import threading

saldo = 100
candado = threading.Lock()

def retirar_dinero(cantidad):
    global saldo
    with candado:  # Aquí el hilo "toma" el candado
        print(f"Hilo {threading.current_thread().name} ha tomado el control.")
        if saldo >= cantidad:
            # Simulamos un pequeño retraso para forzar el riesgo
            nuevo_saldo = saldo - cantidad
            saldo = nuevo_saldo
            print(f"Retiro exitoso. Saldo restante: {saldo}")
        else:
            print("Saldo insuficiente")
    # Al salir del bloque 'with', el candado se libera automáticamente


def retirar_dinero_manual(cantidad):
    global saldo
    # 1. Intentamos adquirir el candado
    candado.acquire()
    
    try:
        print(f"Hilo {threading.current_thread().name} ha tomado el control.")
        if saldo >= cantidad:
            nuevo_saldo = saldo - cantidad
            saldo = nuevo_saldo
            print(f"Retiro de {cantidad} exitoso. Saldo: {saldo}")
        else:
            print("Saldo insuficiente.")
    finally:
        # 2. Pase lo que pase, liberamos el candado para los demás
        candado.release()
        print(f"Hilo {threading.current_thread().name} ha soltado el candado.")