from Ejer_Sistema_Empleados.empleados import Empleado
from Ejer_Sistema_Empleados.empresa import Empresa

print('### Sistema de Empleados ###')

if __name__ == '__main__':
    empresa1 = Empresa('Coderland')
    empresa1.contratar_empleados('Andy', 'Administracion')
    empresa1.contratar_empleados('Rosa', 'Administracion')
    empresa1.contratar_empleados('Ania', 'ventas')

    # Obtener total de empleados
    print(
        f'En la empresa tenemos: {Empleado.contador_empleados}  total de empleados')

    # Obtener total de empleados de departamento de Administración
    print(
        f'En la empresa tenemos: {empresa1.obtener_numero_empleados_departamento('Administracion')}  total de empleados de administracion\n')
    # Enseñar todos los datos de los empleados

    empresa1.mostrar_todos_los_empleados()
