import sys

# Comprobacion de seguridad, ehecutar solo si se reciben 2 argumentos realmente

if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(len(sys.argv[2]))
    for r in range(repeticiones):
        print(texto)
else:
    print('ERROR: Introdujo uno (1) o mas de 2(dos) argumentos')
    print('SOLUCION: Introduzca los argumentos correctamente')
    print('Ejemplo: ejemplo_parametros.py "Texto" 5')
    print("El argumento 0 es el nombre del archivo: ",sys.argv[0])
