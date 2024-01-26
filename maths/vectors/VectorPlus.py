def ingresar_vector():
    # Pedir al usuario que ingrese un vector
    entrada = input("Ingrese un vector como una lista de números separados por comas (por ejemplo, 1,2,3): ")
    
    # Convertir la entrada del usuario a una lista de números
    try:
        vector = [float(x) for x in entrada.split(',')]
        return vector
    except ValueError:
        print("Error: Ingrese valores numéricos.")
        return ingresar_vector()

def sumar_vectores(*vectores):
    if len(vectores) < 2:
        raise ValueError("Se requieren al menos dos vectores para realizar la suma.")

    # Verificar que todos los vectores tengan la misma longitud
    longitud = len(vectores[0])
    if not all(len(v) == longitud for v in vectores):
        raise ValueError("Todos los vectores deben tener la misma longitud.")

    # Verificar que todos los elementos sean numéricos
    for componente in vectores:
        for elemento in componente:
            if not isinstance(elemento, (int, float)):
                raise ValueError("Todos los elementos de los vectores deben ser numéricos.")

    # Sumar los vectores componente por componente
    suma = [sum(componente[i] for componente in vectores) for i in range(longitud)]

    return suma

# Ingresar los vectores desde el usuario
num_vectores = int(input("Ingrese el número de vectores que desea sumar: "))
vectores_ingresados = [ingresar_vector() for _ in range(num_vectores)]

# Calcular la suma de los vectores
resultado = sumar_vectores(*vectores_ingresados)

# Mostrar el resultado
print("La suma de los vectores es:", resultado)
