def EsPrimo(valor):
    es_primo=True
    if type(valor)!=int:
        return None
    for i in range(1,valor):
        if valor%i==0:
            es_primo=False
            break
        else:
            es_primo=True
    return es_primo