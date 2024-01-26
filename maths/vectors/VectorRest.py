def restar_vectores(*vectores):
    if len(vectores) < 2:
        raise ValueError("Se requieren al menos dos vectores para realizar la resta.")

    # Verificar que todos los vectores tengan la misma longitud
    longitud = len(vectores[0])
    if not all(len(v) == longitud for v in vectores):
        raise ValueError("Todos los vectores deben tener la misma longitud.")

    # Verificar que todos los elementos sean numéricos
    for componente in vectores:
        for elemento in componente:
            if not isinstance(elemento, (int, float)):
                raise ValueError("Todos los elementos de los vectores deben ser numéricos.")

    # Restar los vectores componente por componente
    resta = [vectores[0][i] - sum(vectores[j][i] for j in range(1, len(vectores))) for i in range(longitud)]

    return resta

# Ingresar los vectores desde el usuario
num_vectores = int(input("Ingrese el número de vectores que desea restar: "))
vectores_ingresados = [ingresar_vector() for _ in range(num_vectores)]

# Calcular la resta de los vectores
resultado = restar_vectores(*vectores_ingresados)

# Mostrar el resultado
print("La resta de los vectores es:", resultado)
