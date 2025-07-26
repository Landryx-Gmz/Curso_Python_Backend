
# Tienda de isntrumentos:

productos = [
    ('P001','Guitarra Electrica', 1500),
    ('P001','Bajo Electrica', 1300),
    ('P001','Bateria', 2500)
]
print('--Descripcion de compra--')
print(f'{"ID":<10} {"Instrumento":<20} {"Precio":>10}')
print('_'*42)

for id, instrumento, precio in productos:
    print(f'{id:<10} {instrumento:<20} {precio:>10}')
