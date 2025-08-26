# resizer_2.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('new_size', help='tamano de la imagen', type=tuple)
args = parser.parse_args()

im = Image.open(args.input_file)
resized = im.resize(args.new_size)
resized.save(args.output_file)
im.close()

