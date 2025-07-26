# args - arguments - tupla
#kwargs - keyword arguments(key,value), dict

print('###Argumentos variables por llave###')

def supuerheroe_superpoderes(nombre,*args,**kwargs):
    print(f'supreheroe: {nombre},{args},{kwargs}')
    for superpoder in args:
        print(f'superpoder: {superpoder}')
    for informacion_extra in kwargs.items():
        print(f'con informacion extra: {informacion_extra}')

# LLamamos a la funcion
supuerheroe_superpoderes('Flask','Supervelocidad', edad=46,empresa='DC')
supuerheroe_superpoderes('Andy','Superimpetud', edad=36,empresa='Micasa')