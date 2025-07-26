from Final_Ejer_MundoPC.computadora import Computadora
from Final_Ejer_MundoPC.monitor import Monitor
from Final_Ejer_MundoPC.orden import Orden
from Final_Ejer_MundoPC.raton import Raton
from Final_Ejer_MundoPC.teclado import Teclado

print('### MUNDO PC ###')

# Primera computadora

teclado0 = Teclado('HP', 'USB')
raton0 = Raton('HP', 'USB')
monitor0 = Monitor('HP', 27)
computadora0 = Computadora('HP', monitor0, teclado0, raton0)

# Segunda computadora
teclado1 = Teclado('Acer', 'Cable')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('Asus', 25)
computadora1 = Computadora('Asus', teclado1, raton1, monitor1)

# Tercera computadora:
teclado2 = Teclado('Gamer', 'Bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 50)
computadora2 = Computadora('Gamer', teclado2, raton2, monitor2)

# Lista de computadoras
computadoras1 = [computadora0, computadora1, computadora2]

# Creamos un primera orden
orden1 = Orden(computadoras1)
print(orden1)

computadoras2 = [computadora0, computadora2]

orden2 = Orden(computadoras2)
print(orden2)
