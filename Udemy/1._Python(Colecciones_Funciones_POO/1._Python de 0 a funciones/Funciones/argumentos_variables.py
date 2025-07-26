print('#### Argumantos Variables ####')


def superheroe_superpoderes(superheroe,nombre,*args):
    print(f'Superheroe: {superheroe}-{nombre}-{args}')
    for superpoder in args:
        print(f'\t Superpoderes: {superpoder}')

superheroe_superpoderes('Bataman','Brucer Wayne','Tecnologia de batalla','Baticueva', 'Dinero')
superheroe_superpoderes('Flash','Barri','Velocidad maxima')
superheroe_superpoderes('Vecino', 'Juanito')