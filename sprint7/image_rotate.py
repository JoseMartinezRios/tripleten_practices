from PIL import Image
import argparse #importar argparse

#iniciar analizados sintáctico
parser = argparse.ArgumentParser()

# agregar argumentos con nombres correspondientes
parser.add_argument('input_file')	# primer argumento: archivo de entrada
parser.add_argument('output_file')	# segundo argumento: archivo de salida
parser.add_argument('angle',type=int)	# tercer argumento: ángulo

# analizar argumentos
args = parser.parse_args()

#cargar imagen del argumento input_file
im = Image.open(args.input_file)

# muestra el tamaño de la imagen
print(im.size)

# girar la imagen al tamaño proporcionado como argumento
rotated = im.rotate(args.angle)

#guardar imagen girada usando la ruta de salida de un argumento output_file
rotated.save(args.output_file)
