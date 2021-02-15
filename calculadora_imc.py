autor = ["Francisco Javier Sánchez Panduro", "A01639832"]
fecha_creado = "11 de octubre 2020"

#bienvenida

print("Calculadora de IMC\n")

# Información del usuario

# pregunta información al usario y la asigna a varaibles

nombre = input("¿Cuál es tu nombre completo?: ")

estatura = float(input("\n¿Cuál es tu estatura en centímetros?: "))

peso = float(input("\n¿Cuál es tu peso en kilogramos?: "))

calc_IMC = round(peso / ((estatura / 100) ** 2), 2)

IMC = str(calc_IMC) + ","

if calc_IMC < 18.5:
    estado_IMC = "tienes peso bajo."
elif calc_IMC > 18.5 and calc_IMC < 24.9:
    estado_IMC = "tienes un peso saludable."
elif calc_IMC > 24.9 and calc_IMC < 29.9:
    estado_IMC = "tienes sobrepeso."
else:
    estado_IMC = "tienes obesidad."

# lista de información del usuario

usuario = [nombre, peso, estatura, IMC, estado_IMC]

# Se le muestra la información al usario

print("\n\n\nHola", usuario[0],"\n\nTu Peso resgistrado es:",\
      usuario[1],"kg\n\nTu estatura es:",usuario[2]/100,"m\n\nTu IMC es:", \
      usuario[3], "lo que indica que", usuario[4])

# Se le explica como leer resultados al usario

print("\n\n\nCómo leer resultados\n\nNivéles de Peso de acuerdo al IMC:\nIMC pro debajo de 18.5:",\
      "Peso bajo\nIMC entre 18.5 - 24.9: Peso normal\nIMC entre 25.0 - 29.9: Sobrepeso\nIMC de más de",\
      "30.0: Obesidad")

# Información del autor

print("\n\n\nPrograma creado el:",fecha_creado,"\nAutor del programa:",*autor)