autor = "Francisco Javier Sánchez Panduro"
# A01639832
# MA1040 GRUPO 803

#Este programa es una simle caluladora de calorías

# Pregunta al usuario el nombre del alimento y lo asigna a la variable
alimento = input("¿Cuál es el nombre del alimento? ")

# Pregunta al usario la cantidad de carbohidratos y lo asigna a la variable como un número tipo float
carbohidratos = float(input("Ingresa la cantidad de cabrohidratos en gramos: "))

# Pregunta al usario la cantidad de lípidos y lo asigna a la variable como un número tipo float
lipidos = float(input("Ingresa la cantidad de lípidos en gramos: "))

# Pregunta al usario la cantidad de proteinas y lo asigna a la variable como un número tipo float
proteinas = float(input("Ingresa la cantidad de proteínas en gramos: "))

# Calcula las calorías con los otros tres tipos de nutrientes dados
calorias = (carbohidratos * 4) + (lipidos * 9) + (proteinas * 4)

# Le regresa al usuario las calorías dentro de una oración que incluye el nombre del alimento
print("Las calorías proporcionadas por la porción de", alimento, "ingresadas, son:", calorias)

print("Programa creado el 4 de octubre 2020 por", autor)