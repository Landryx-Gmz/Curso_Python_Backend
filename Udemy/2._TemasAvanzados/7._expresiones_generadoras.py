print('*** Expresiones Generadoras ***')

genarador = (x ** 2 for x in range(10) if x % 2 == 0)

for cuadrado_pares in genarador:
    print(cuadrado_pares)
