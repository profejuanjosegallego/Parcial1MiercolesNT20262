def validar_cupo(vehiculos, capacidad):
    """
    Función 2: Cuenta cuántos vehículos tienen activo=True y determina si hay espacio.
    """
    activos = 0
    for v in vehiculos:
        if v["activo"]:
            activos += 1
            
    if activos < capacidad:
        return True
    else:
        return False

def registrar_ingreso(vehiculos):
    """
    Función 1: Registra vehículos hasta completar 15 ingresos o hasta que el usuario termine.
    """
    if len(vehiculos) >= 15:
        print("Límite histórico de 15 registros alcanzado.")
        return vehiculos

    while len(vehiculos) < 15:
        if not validar_cupo(vehiculos, 10):
            print("\n>> ATENCIÓN: Capacidad máxima de 10 vehículos simultáneos alcanzada. No hay cupo.")
            break
            
        continuar = input("\n¿Desea registrar un vehículo? (s/n): ").lower()
        if continuar != 's':
            break
            
        placa = input("Ingrese placa: ").upper()
        
        # Validar que la placa no esté activa actualmente
        placa_activa = False
        for v in vehiculos:
            if v["placa"] == placa and v["activo"]:
                placa_activa = True
                break
                
        if placa_activa:
            print(">> ERROR: La placa ya se encuentra activa dentro del parqueadero.")
            continue
            
        tipo = input("Ingrese tipo (Moto / Carro / Camioneta): ").capitalize()
        if tipo not in ["Moto", "Carro", "Camioneta"]:
            print(">> ERROR: Tipo de vehículo inválido.")
            continue
            
        categoria = input("Ingrese categoría (Asistente / Proveedor / Personal): ").capitalize()
        if categoria not in ["Asistente", "Proveedor", "Personal"]:
            print(">> ERROR: Categoría inválida.")
            continue
            
        hora_entrada = int(input("Ingrese hora de entrada (Formato 24h, entre 6 y 20): "))
        if hora_entrada < 6 or hora_entrada > 20:
            print(">> ERROR: Hora de entrada inválida. Debe ser entre las 6 y las 20.")
            continue
            
        # Creación del diccionario
        nuevo_vehiculo = {
            "placa": placa,
            "tipo": tipo,
            "categoria": categoria,
            "hora_entrada": hora_entrada,
            "hora_salida": 0,
            "valor_pagado": 0,
            "activo": True
        }
        
        vehiculos.append(nuevo_vehiculo)
        print(">> Vehículo registrado exitosamente.")
        
    return vehiculos

def calcular_horas(hora_entrada, hora_salida):
    """
    Función 3: Calcula las horas de permanencia. La salida debe ser mayor a la entrada.
    """
    if hora_salida <= hora_entrada:
        return -1
        
    diferencia = hora_salida - hora_entrada
    
    if diferencia < 1:
        return 1
    
    return diferencia

def calcular_tarifa(tipo, categoria, horas):
    """
    Función 4: Calcula el valor a pagar aplicando tarifas y descuentos.
    """
    tarifa_base = 0
    if tipo == "Moto":
        tarifa_base = 2000
    elif tipo == "Carro":
        tarifa_base = 3500
    elif tipo == "Camioneta":
        tarifa_base = 5000
        
    total = tarifa_base * horas
    
    if categoria == "Personal":
        total = 0 # 100% descuento
    elif categoria == "Proveedor":
        total = total * 0.8 # 20% descuento (paga el 80%)
        
    return total

def registrar_salida(vehiculos, placa):
    """
    Función 5: Busca la placa, pide hora de salida, calcula tarifa y libera el cupo.
    """
    for v in vehiculos:
        if v["placa"] == placa and v["activo"]:
            hora_salida = int(input(f"Ingrese la hora de salida para la placa {placa} (mayor a {v['hora_entrada']}): "))
            
            horas_permanencia = calcular_horas(v["hora_entrada"], hora_salida)
            if horas_permanencia == -1:
                print(">> ERROR: La hora de salida es inválida (debe ser posterior a la entrada).")
                return False
                
            valor_pagar = calcular_tarifa(v["tipo"], v["categoria"], horas_permanencia)
            
            v["hora_salida"] = hora_salida
            v["valor_pagado"] = valor_pagar
            v["activo"] = False
            
            print(f"\n>> SALIDA EXITOSA <<")
            print(f"Vehículo: {v['tipo']} | Categoría: {v['categoria']}")
            print(f"Horas facturadas: {horas_permanencia}")
            print(f"Total a pagar: ${valor_pagar}")
            return True
            
    print(">> ERROR: La placa no se encontró o el vehículo ya registró su salida.")
    return False

def generar_cierre(vehiculos):
    """
    Función 6: Muestra estadísticas de la jornada. 
    Halla el tipo más frecuente de forma manual.
    """
    total_registrados = len(vehiculos)
    vehiculos_activos = 0
    ingresos_recaudados = 0
    suma_horas = 0
    cantidad_salieron = 0
    
    # Diccionario para contar manualmente los tipos de vehículo
    conteo_tipos = {}
    
    for v in vehiculos:
        # 1. Contar activos
        if v["activo"]:
            vehiculos_activos += 1
        else:
            # 2. Sumar ingresos y horas de los que ya salieron
            ingresos_recaudados += v["valor_pagado"]
            suma_horas += (v["hora_salida"] - v["hora_entrada"])
            cantidad_salieron += 1
            
        # 3. Registrar el tipo para contar frecuencias
        tipo = v["tipo"]
        if tipo in conteo_tipos:
            conteo_tipos[tipo] += 1
        else:
            conteo_tipos[tipo] = 1

    # Calcular promedio de horas
    promedio_horas = 0
    if cantidad_salieron > 0:
        promedio_horas = suma_horas / cantidad_salieron

    # Encontrar el tipo más frecuente con ciclo y condicionales (sin max() ni lambda)
    tipo_mas_ingreso = "Ninguno"
    max_frecuencia = -1
    
    for tipo_vehiculo in conteo_tipos:
        if conteo_tipos[tipo_vehiculo] > max_frecuencia:
            max_frecuencia = conteo_tipos[tipo_vehiculo]
            tipo_mas_ingreso = tipo_vehiculo

    print("\n" + "="*35)
    print("       REPORTE DE CIERRE")
    print("="*35)
    print(f"Total vehículos registrados : {total_registrados}")
    print(f"Vehículos aún en parqueadero: {vehiculos_activos}")
    print(f"Ingresos recaudados         : ${ingresos_recaudados}")
    print(f"Promedio horas (los q salieron): {promedio_horas:.2f} horas")
    print(f"Tipo vehículo más ingresado : {tipo_mas_ingreso} ({max_frecuencia} ingresos)")
    print("="*35)