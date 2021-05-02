#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7
    '''
    pri_num = print('ingrese primer numero')
    num_1 = float(input()) 
    seg_num = print('ingrese segundo numero')
    num_2 = float(input())
    Suma = num_1 + num_2
    Resta = num_1 - num_2
    Multiplicación = num_1 * num_2
    División = num_1 / num_2
    Potencia = num_1 **2
    pot_2 = num_2**2
    print('la suma de', num_1,'y',num_2, 'es',Suma)
    print('la resta de', num_1,'y',num_2, 'es',Resta)
    print('la multiplicacion de', num_1,'y',num_2, 'es',Multiplicación)
    print('la divisio de', num_1,'y',num_2, 'es',División)
    print('la potencia de', num_1, 'es',Potencia)
    print('la potencia de', num_2, 'es',pot_2)
    
    


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona
    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.
    '''
    pri_num = print('ingrese su nombre y apellido')
    nombre = str(input())
    dni = print('ingrese su DNI')
    DNI = input()
    edad = print('ingrese su edad')
    Edad = int(input())
    alt = print('ingrese su altura')
    Alt = float(input())
    print('nombre completo:',nombre,'dni:',DNI)
    print('nombre completo:',nombre,'edad:',Edad,'altura:',Alt)



def ej3():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    pri_padr = print('ingrese su nombre y apellido')
    padre_1 = str(input())
    seg_padr = print('ingrese su nombre y apellido')
    padre_2 = str(input())
    hijo = print('ingrese solamente nombre del hijo ')
    Hijo1 = str(input())
    nombre1,apellido1 = padre_1.split()
    nombre2,apellido2 = padre_2.split()
    print(Hijo1,apellido1,apellido2)


def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''
    pri_per = print('ingrese su nombre y apellido')
    persona_1 = str(input())
    seg_per = print('ingrese su nombre y apellido')
    persona_2 = str(input())
    nombre1,apellido1 = persona_1.split()
    nombre2,apellido2 = persona_2.split()
    if apellido2 == apellido1:
      print('estas personas son parientes')
    elif apellido2 != apellido1:
      print('estas personas no son parientes')

    



def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''
    pri_per = print('ingrese su nombre y apellido')
    persona_1 = str(input())
    print(persona_1.lower())
    print(persona_1.upper())
    print(persona_1.capitalize())


if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
