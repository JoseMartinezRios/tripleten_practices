# module_2.py

import module_1

def double_check():
    print('calling useful_function twice: ')
    module_1.useful_function()
    module_1.useful_function()

if __name__ == "__main__":
    print("Ejecutando module_2...")
    double_check()
