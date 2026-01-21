# Usando multiproceso quiero que calcules el coste de envío 
# de varios paquetes
# Si un paquete tiene un coste mayor a 100€, debe ser 
# auditado por un proceso hijo
# que imprimirá un mensaje especial para esos paquetes "Premium".

from time import sleep

# 1. Función para calcular coste
def calcular_envio(id_paquete: int, peso: float, distancia: float) -> tuple[int, float]:
    # Simula un cálculo complejo
    costo = peso * distancia * 0.5
    sleep(0.5)  # Simula tiempo de procesamiento
    return (id_paquete, costo)

# 2. Función para el proceso de Auditoría (Consumidor)
def proceso_auditoria(cola):
    print("Auditor: Esperando paquetes de alto valor...")
    while True:
        # COMPLETA: Obtén el item de la cola
        item = None 
        
        if item is None: # Señal de parada
            break
        
        print(f"💰 AUDITORÍA: Paquete {item[0]} procesado con coste crítico: {item[1]}€")

if __name__ == '__main__':
    # Datos de entrada: (id, peso, distancia)
    paquetes = [
        (1, 10, 50),   # 250€ (Premium)
        (2, 2, 10),    # 10€
        (3, 20, 100),  # 1000€ (Premium)
        (4, 5, 5)      # 12.5€
    ]



    # --- PASO A: Paralelismo con Pool ---
    # COMPLETA: Usa starmap para procesar la lista 'paquetes' y 
    # guardar los resultados en una lista
    resultados = []

    # --- PASO B: Comunicación con Proceso Hijo ---
    # COMPLETA: Crea e inicia el proceso 'auditor' que recibe la cola
    p_auditor = None

    # --- PASO C: Filtrado y Envío ---
    for id_p, coste in resultados:
        if coste > 100:
            # COMPLETA: Envía el paquete a la cola si es Premium
            pass

    # --- PASO D: Finalización ---
    # COMPLETA: Que todos los procesos terminen correctamente
    
    print("Sistema logístico finalizado.")