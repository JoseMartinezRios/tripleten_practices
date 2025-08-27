# Crear la funcion sign()
def sign(x):
    """Devuelve el signo del numero."""
    if x == None:
        return None
    if x < 0:
        return -1
    return 1

# Prueba de la funcion sign()
def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None
