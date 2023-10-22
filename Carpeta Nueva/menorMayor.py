def menorMayor(numeros):

    '''La funcionllamada mayorMenor recibe como argumento un arreglo de numeros llamado 'numeros' y debe devolver un arreglo que contenga el mayor 
    numero del arreglo 'numeros' en la posicion uno y  el menor numero del arreglo en la posicion cero

        Ej:
        mayorMenor[(9,17,6,2,4)] debe retornar [2,17]
        ya que 17 es el numero mas grande (mayor) dentro de [(9,17,6,2,4)]
        y 2 es el numero mas chico (menor) dentro del arreglo [(9,17,6,2,4)]'''

#Tu codigo aca:
    max=numeros.copy()
    min=numeros.copy()
    max.sort(reverse=False)
    min.sort(reverse=True)
    M=max.pop()
    m=min.pop()

    resultado=[m,M]

    return resultado

print(menorMayor([-1,-9,-17,2,4,9,10]))