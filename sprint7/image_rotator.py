# image_rotator.py

from PIL import Image

# cargar imagen
im = Image.open('tripleten_logo.jpeg')

# obtener el tamaño de la imagen
print(im.size)

#girar imagen 90 grados, antihorario
rotated = im.rotate(90)

#guardar imagen modificada
rotated.save('rotated.png')
