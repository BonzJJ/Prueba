
# For

# While

# Realizar un programa que imprima en pantalla los numeros del 0 al 100.


def cicloMientras():
    x = 0
    while x <= 100 : # condicion de prueba
        print(x)   # sentencia o orden en el codigo
        x = x + 1 # sentencia que varia la variante contadora x

def cicloFor():
    for x in range(101) :
        print(x)

def cicloMientras2():
    for x in range(50,101,5) :
        print(x)

if __name__ == '__main__':
    #cicloMientras()
    print()
    cicloMientras()