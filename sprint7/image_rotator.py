# image_rotator.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('angle', help='rotacion deseada', type=int)
parser.add_argument('-i', '--info', help='muestra el tamanio de la imagen')
args = parser.parse_args()

angle = args.angle

try:
    im = Image.open(args.input_file)
except FileNotFoundError:
    print('archivo de entrada no encontrado, introduce el nombre de archivo correcto')
else: 
    rotated = im.rotate(angle)
    im.close() #cerrar archivo de imagen
    rotated.save(args.output_file)
    print("ejecucion fluida")

if args.info:
    print('dimensiones de la imagen de entrada:', im.size)
