class herramientas:
    ''' Esta es la clase creada con las funcinoes del Homework #7 para un elemento.
    Sin variables definidas para la clase'''
    def __init__(self):
        pass
    
    def factorial(self,n):
        f=1
        if type(n)!=int:
            print ("Input Error. Debe ser un entero")
            return None
        elif n<0:
            print ("Input Error. Debe ser positivo")
            return None
        elif n==0:
            f=1
            return f
        else:
            for i in range(1,n+1):
                f=f*i
            return f


    def primo(self,a):
        es_primo = True
        for i in range(2,a):
            if a%i==0:
                es_primo=False
                break
        return es_primo

    def suma(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def mas_repe(self,A):
            a=0 #elemento_repetido en la lista
            q=0 # cantidad de veces que se repite en la lista
            b=0 #contador/compara
            if len(A)==0:
                return print("Lista vacia")
            for i in A:
                b=A.count(i) #se cuentan cuantas veces esta presente el elemento en la lista
                if b > q: #si la cantidad de veces que se repite el elemento es mayor que la cantidad anterior, guarda el elemento en a
                    a=i
                    q=b
            print(a,"es el elemento mas repetido y se repite ",q,"veces")
            return a,q
    
    def convert_temp(self,valor,origen,destino):
        if origen == 'C':
            if destino == 'C':
                valor_destino = valor # No hay conversion 
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'F':
                valor_destino = valor*9/5+32
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'K':
                valor_destino = valor + 273.15
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
        elif origen == 'F':
            if destino == 'F': # No hay conversion
                valor_destino = valor
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'C':
                valor_destino = valor*5/9-17.777
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'K':
                valor_destino = valor * 0.556+255.37
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
        elif origen == 'K':
            if destino == 'K': # No hay conversion
                valor_destino = valor
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'C':
                valor_destino= valor - 273.15
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'F':
                valor_destino=1.8*valor-439.67
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
        return valor_destino,destino   
    
    
class Funciones:
    '''Esta es la Clase creada a partir de la clase herramientas, pero con la variable de ingreso definida como una lista
    Las funciones se modificaron de manera que corrieran para un input lista.
    Se encapsularon las funciones que se utilizaron en la clase anterior creandose nuevas funciones que iterasen sobre 
    los elementos de las listas que son dadas como ingreso'''

    def __init__(self,lista_nro):
        if (type(lista_nro)!=list):
            self.lista=[]
            raise ValueError('Error de input. Se esperaba una lista de numeros enteros')
        for i in lista_nro:
                if type(i) != int:
                    raise ValueError('Error de input. Se esperaba una lista de enteros')
        else:
            self.lista = lista_nro
        

    def factorial(self):
        factor=[]
        for i in self.lista:
            #print(f'el factorial de {i} es {self.__factorial(i)}')
            factor.append(self.__factorial(i))
        return factor

    def __factorial(self,n):
        #for i in self.lista:
        #    assert (type(i)!=int), f'el valor de {i} debe ser un entero'
        #    assert (n<0), f'el valor de {i} debe ser positivo'
        f=1
        if type(n)!=int:
            print ("Input Error. Debe ser un entero")
            return None
        elif n<0:
            print ("Input Error. Debe ser positivo")
            return None
        
        if n==0:
            f=1
            return f
        else:
            for i in range(1,n+1):
                f=f*i
            return f

    def primo(self):
        P=[]
        for i in self.lista:
            if self.__primo(i):
                #print(f'el valor {i} es primo')
                P.append(True)
            else:
                #print(f'el valor {i} no es primo')
                P.append(False)
        print(P)
        return P
                       
    def __primo(self,a):
        es_primo = True
        for i in range(2,a):
            if a % i==0:
                es_primo=False
                break
        return es_primo

    def mas_repe(self,A):
            a=0 #elemento_repetido en la lista
            q=0 # cantidad de veces que se repite en la lista
            b=0 #contador/compara
            if len(A)==0:
                return print("Lista vacia")
            for i in A:
                b=A.count(i) #se cuentan cuantas veces esta presente el elemento en la lista
                if b > q: #si la cantidad de veces que se repite el elemento es mayor que la cantidad anterior, guarda el elemento en a
                    a=i
                    q=b
           # print(a,"es el elemento mas repetido y se repite ",q,"veces")
            return [a,q]
    
    def convert_temp(self,origen,destino):
        grados_esperados=['C','F','K']
        salida_esperada=[]
        if str(origen) not in grados_esperados:
            print('los parametros esperados son', grados_esperados)
        if str(destino) not in grados_esperados:
             print('los parametros esperados son', grados_esperados)
        for i in self.lista:
            salida_esperada.append(self.__convert_temp(i,origen,destino))
        return salida_esperada

    def __convert_temp(self,valor,origen,destino):
        if origen == 'C':
            if destino == 'C':
                valor_destino = valor # No hay conversion 
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'F':
                valor_destino = valor*9/5+32
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'K':
                valor_destino = valor + 273.15
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
        elif origen == 'F':
            if destino == 'F': # No hay conversion
                valor_destino = valor
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'C':
                valor_destino = valor*5/9-17.777
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'K':
                valor_destino = valor * 0.556+255.37
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
        elif origen == 'K':
            if destino == 'K': # No hay conversion
                valor_destino = valor
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'C':
                valor_destino= valor - 273.15
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
            elif destino == 'F':
                valor_destino=1.8*valor-439.67
                print(valor,"",origen,"son equivalentes a ",valor_destino," ",destino)
        return valor_destino,destino   
    