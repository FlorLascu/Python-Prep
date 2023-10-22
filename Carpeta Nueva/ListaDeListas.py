def ListadeListas(lista):
    '''Esta funcion recibe una lista, que puede contener elementos que a su vez sean listas y devuelve
    esos elementos por separado en una lista unica.
    En caso de que el parametro no sea del tipo lista, debe retornar nulo.
    Recibe un argumento:
    lista : La lista que puede contener otras listas y se convierte a una lista
    de elementos unicos o no iterables
    Ej:
    ListaDeListas([1,2,['a','b'],[10]]]) debe retornar [1,2,'a', 'b',10]
    ListaDeListas(108) debe retornar el valor nulo.
    ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]'''

    #Tu codigo aca:

    if not (isinstance(lista,list)) :
        return None   
    
    stack = lista.copy()  # copia la lista original a evaluar para no modificarla o alterarla
    resultado = []         # es donde se iran almacenando los elementos a medida que los "limpia y recorre"
    
    while len(stack)>0:     # mientras haya elementos a evaluar en stack seguira corriendo el ciclo
       
        current = stack.pop(0)  #extrae el primer elemento de la lista ingresada, copiada a stack y lo evalua
       
        if isinstance(current,int) or isinstance(current,str): # evalua si el elemento extraido es un str o int
            resultado.append(current) # si es int o str lo agrega a la lista resultado

        if isinstance(current,list):  # si no es un str o int, sino una lista comienza el ciclo for
            for i in range(len(current) - 1, -1, -1):  #
                stack.insert(0, current[i])
        
        if len(stack) == 0:
            return resultado


print(ListadeListas([1,2,3,"a",[5,6,7,[8,9],[10,11]]]))
#print(ListadeListas(['a']))