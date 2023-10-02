class Funciones:
    def __init__(self,lista_numeros):
        self.lista = lista_numeros
    
    def list_primo(self,b):
        c=[] #lista donde almacenar los numeros primos de la lista
        for i in self.lista: #iterar por cada elemento de la lista b
            if self.__es_primo(int(i)):
                c.append(i) #almacenar en c todos los elementos de b que sean primos
        return c   

    def convert_temp(self,valor,origen,destino):
        for i in self.lista:
            self.__convert_temp(i,origen,destino)

    def factorial(self,n):
        e=[]
        for i in self.lista:
            j=self.__ft(i)
            e.append(j)
        return e

    def __es_primo(self,a):
        primo = True #defino la variable de resultado
        for div in range (2,a): # itera el divisor desde 2 hasta a-1 
            if (a % div==0): #si el resto de a por cualquier numero desde 2 a a-1 es cero => No es primo
                primo=False
                break
        return primo # sino primo sigue siendo True
    
    def sacar_valor(self,listaA):
        moda=0
        veces_repetido=0
        for num in listaA:
            numero_modal=listaA.count(num)
            if numero_modal > veces_repetido:
                veces_repetido=numero_modal
                moda=num
        return moda,veces_repetido
    
    def __ft(self,n):
        f=1
        if type(n)!=int:
            print("Input error n not integer")
            return None
        elif n < 0:
            print("Input error n is negative")
            return None
        else:
            for n in range (1,n+1):
                f=f*n
        return f

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
    
    A=[5,2,6]
    factorial(A)