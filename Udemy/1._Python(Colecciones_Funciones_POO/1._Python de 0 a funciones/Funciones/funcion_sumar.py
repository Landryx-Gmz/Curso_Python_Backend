from modulo_funcion_sumar import sumar

print('###Funcion sumar###')


if __name__ == '__main__':
    print(f'Funcion sumar desde este modulo')

num1 = int(input("dame el parametro de suma a: "))
num2 = int(input("dame el parametro de suma b: "))

suma=sumar(num1,num2)
print(f'El resultado es: {suma}')