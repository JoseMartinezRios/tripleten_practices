#module.py

import re

def check_email(string: str):
    '''
    usa expresiones regulares para comprobar el formato de la direccion de correo electronico
    el patron es "algo@algo.algo"
    '''
    if re.match('[.\w]+@\w+[.]\w+', string):
        print('correcto')
    else:
        print('comprobar direccion de correo electronico')

def check_age(age: int):
    if age >= 50:
        print('acceso permitido')
    else:
        print('Eres demasiado joven')
