from funciones import generar_cierre, registrar_ingreso, registrar_salida


def main():
    lista_vehiculos = []
    
    print("BIENVENIDO AL SISTEMA DE ESTACIONAMIENTO")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar ingreso de vehículos")
        print("2. Registrar salida de un vehículo")
        print("3. Finalizar jornada (Generar cierre)")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            
            lista_vehiculos = registrar_ingreso(lista_vehiculos)
            
        elif opcion == '2':
            placa = input("\nIngrese la placa del vehículo a despachar: ").upper()
            registrar_salida(lista_vehiculos, placa)
            
        elif opcion == '3':
            generar_cierre(lista_vehiculos)
            print("Cerrando sistema... ¡Hasta luego!")
            break
            
        else:
            print(">> ERROR: Opción inválida. Intente de nuevo.")

# Punto de entrada para ejecución
if __name__ == "__main__":
    main()