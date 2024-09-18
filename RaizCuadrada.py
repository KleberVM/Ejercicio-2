#Realizado por Yamil Angelo Lara Balderrama
def calcular_raiz(num):
    # Validar que el número sea mayor o igual a cero
    if num < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo"
    else:
        return math.sqrt(num)