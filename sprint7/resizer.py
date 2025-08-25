#resizer.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta el archivo de entrada')
#completar codigo
parser.add_argument('output_file', help='ruta de salida')
parser.add_argument('width', help='ancho deseado', type=int)
parser.add_argument('height', help='altura deseada', type=int)
args = parser.parse_args()


im = Image.open(args.input_file)
#completar codigo
new_size = (args.width, args.height)
resized = im.resize(new_size)
resized.save(args.output_file)

im.close()
