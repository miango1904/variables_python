#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.5

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.5"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7
    res_sum = numero_1 + numero_2
    print(res_sum)
    rest = numero_1 -numero_2
    print(rest)

    # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....

    # Imprimir en pantalla el resultado de la suma
    # print(....)

    # Repita el procedimiento para realizar la resta


def ej2():
    # Ejercicios de práctica numérica

    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())
    op_suma = numero_1 + numero_2
    op_resta = numero_1 - numero_2
    op_division = numero_1 / numero_2
    op_mult = numero_1 * numero_2
    print('El resultado de sumar',numero_1,'mas',numero_2,'es',op_suma,)
    print('El resultado de restar',numero_1,'menos',numero_2,'es',op_resta,)
    print('El resultado de dividi',numero_1,'entr',numero_2,'es',op_division,)
    print('El resultado de multiplicar',numero_1,'entre',numero_2,'es',op_mult)

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    # El resultado de sumar 4 y 2 es 6
    # NOTA: No coloque usted los nùmeros y resultados, use las variables

    # Suma

    # Resta

    # División

    # Multiplicación


def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())
    nombre_completo = nombre+apellido
    print(nombre_completo)
    print(len(nombre_completo))

    # Imprima su nombre completo

    # Almacenar su nombre completo en una variable
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo


def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())
    
    inicial_1 = palabra_1[0]
    inicial_2 = palabra_2[0]
    inicial_3 = palabra_3[0]
    print (inicial_1,inicial_2,inicial_3)

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    pri_3 = palabra_1[:3]
    ult_3 = palabra_2[-3:]
    print(pri_3,ult_3)

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
