#Desarrollado por Yahir Leonardo Cayola Cayo
def dividir(num1,num2):
    num1 = int(input("Ingrese el 1er número a dividir: "))
    num2 = int(input("Ingrese el 2do número a dividir: "))
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero."
