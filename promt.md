    Caso 2: Sistema de control de estacionamiento para un evento masivo
Contexto
Una institución realizará una feria tecnológica y habilitará un parqueadero temporal para vehículos de asistentes, proveedores y personal. El equipo logístico necesita una aplicación sencilla que registre los ingresos, controle la capacidad disponible, calcule el valor del servicio y genere un reporte al finalizar la jornada.

Problema
Desarrolle un programa en Python que resuelva el caso planteado. La solución debe estar dividida en exactamente 6 funciones principales, descritas a continuación.

Estructura de los datos
Cada registro principal debe representarse mediante un diccionario y almacenarse en una lista.

placa: Placa del vehículo.
tipo: Moto, Carro o Camioneta.
categoria: Asistente, Proveedor o Personal.
hora_entrada: Hora entera entre 6 y 20.
hora_salida: Inicialmente 0.
valor_pagado: Inicialmente 0.
activo: True mientras permanezca en el parqueadero.
Funciones obligatorias
1. registrar_ingreso(vehiculos)
Registrar vehículos uno a uno hasta completar 15 ingresos o hasta que el usuario decida terminar. No se permite repetir una placa que esté activa. Retorna la lista actualizada.

2. validar_cupo(vehiculos, capacidad)
Contar cuántos vehículos tienen activo=True y determinar si aún existe espacio. La capacidad máxima será de 10 vehículos simultáneos. Retorna True si existe cupo y False en caso contrario.

3. calcular_horas(hora_entrada, hora_salida)
Calcular las horas de permanencia. Si la diferencia es menor que 1, se cobra 1 hora. La salida debe ser mayor que la entrada. Retorna la cantidad de horas o -1 si los datos son inválidos.

4. calcular_tarifa(tipo, categoria, horas)
Aplicar tarifa por hora: Moto $2.000, Carro $3.500, Camioneta $5.000. El personal tiene 100% de descuento y los proveedores 20% de descuento. Retorna el valor final.

5. registrar_salida(vehiculos, placa)
Buscar la placa activa, solicitar hora de salida, calcular permanencia y tarifa, actualizar hora_salida, valor_pagado y activo=False. Retorna True si la salida fue registrada y False si la placa no existe o los datos son inválidos.

6. generar_cierre(vehiculos)
Mostrar total de vehículos registrados, vehículos aún activos, ingresos recaudados, promedio de horas de los vehículos que ya salieron y tipo de vehículo que más ingresó. Para hallar el tipo más frecuente debe usar contadores, ciclos y condicionales.

Restricciones técnicas
No utilizar clases, archivos, bases de datos, librerías externas ni estructuras diferentes a las trabajadas en clase.
Utilizar únicamente funciones, ciclos, condicionales, listas, diccionarios, variables y operaciones básicas.
No utilizar max() con key, Counter, lambda ni herramientas que resuelvan automáticamente la frecuencia solicitada.
Cada función debe participar del flujo general de la solución.
El programa debe impedir cobros con horas inválidas y respetar la capacidad máxima.
Entrega esperada
Código fuente ejecutable en Python.
Las 6 funciones solicitadas claramente identificadas.
Programa principal que invoque las funciones y permita comprobar el funcionamiento completo.
Nombres de variables y funciones comprensibles.
Salidas en consola suficientemente claras para interpretar el resultado.
Importante: se evaluará tanto que el programa funcione como la forma en que el problema fue dividido y resuelto mediante funciones.