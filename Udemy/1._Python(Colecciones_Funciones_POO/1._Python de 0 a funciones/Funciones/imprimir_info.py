print('### Usando kwargs para imprimir informacion ###')

# Funcion que acepta argumentos variables de tipo llave valor

def ingresar_en_diccionario(**kwargs):
    print(f'\n Valores recibidos:')
    for id,(clave, valor) in enumerate(kwargs.items(),start=1):
        print(f'Campo de datos #{id}.\n{clave}-{valor}')


# Lista para almacenar todos los registros
registros_totales = []



# Variable de cuantos datos queremos introducir
campos_de_datos=int(input('Cuantos campos de datos quieres introducir?: '))


# Recorrido por repeticiones introducidas
for i in range(campos_de_datos):
    print(f'\nRegistro #{i + 1}')
    total_datos = int(input('Cuantos datos K/V quieres introducir?: '))

    #Diccionario auxiliar:
    datos={}

    #condicional de recorrido para ingresar datos
    for indice in range(total_datos):
        # Peticion de datos clave valor
        clave = input(f'Ingrese la Clave #: {indice + 1} ')
        valor = input(f'Ingree el valor #{indice + 1} ')
        # Almacenamientos de los datos
        datos[clave]=valor

# Llamamos a la funcion y pasamos los datos
    ingresar_en_diccionario(**datos)

    # Guardamos los registros en la lista
    registros_totales.append(datos)

    # 📋 Resumen final
print('\n--- Resumen de todos los registros introducidos ---')
for id_registro, registro in enumerate(registros_totales, start=1):
    print(f'\nRegistro #{id_registro}:')
    for id_campo, (clave, valor) in enumerate(registro.items(), start=1):
        print(f'  {id_campo}. {clave}: {valor}')

