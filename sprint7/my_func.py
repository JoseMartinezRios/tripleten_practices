#my_func.py
product_price = 12.0    #global variable
product_qty = 5         #global variable

def total_price():
#    product_price = 11.0    #local variable
#    product_qty = 4         #local variable
    print(f'Precio total: {product_price * product_qty}')

total_price()

#another function
def trip_price(dist_miles, mpg, price, loc_from='A', loc_to='B'):
    total_price = dist_miles * price/mpg
    print(f'Un viaje de {loc_from} a {loc_to} cuesta ${total_price}')

#trip_price(409, 35, 5.1, 'A', 'B')
trip_price(409, 35, price=3.8)

