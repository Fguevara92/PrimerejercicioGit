import random

def simulador_vehiculo():
    """Solicita la distancia, genera una velocidad aleatoria
    y determina la acción del vehículo."""

    try:
        distancia = int(input("Ingrese la distancia al obstáculo (en metros): "))
    except ValueError:
        print("¡Error! Ingresa un número válido.")
        return

    # Generar velocidad aleatoria
    velocidad = random.randint(10, 120)

    # Árbol de decisión
    if distancia <= 20 and velocidad > 60:
        accion = "FRENADO DE EMERGENCIA"
    elif 21 <= distancia <= 50:
        accion = "DESACELERACIÓN PREVENTIVA"
    else:
        accion = "MANTENER CURSO NORMAL"

    
    print("\n====================================")
    print("REPORTE DEL VEHÍCULO AUTÓNOMO")
    print("====================================")
    print(f"Distancia ingresada : {distancia} metros")
    print(f"Velocidad generada  : {velocidad} km/h")
    print(f"Acción del sistema  : {accion}")
    print("====================================\n")


def menu_principal():
    """Controla el menú principal."""

    while True:
        print("===== SISTEMA DE CONTROL AUTOMOTRIZ =====")
        print("1. Ejecutar prueba")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            simulador_vehiculo()
        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")



if __name__ == "__main__":
    menu_principal()