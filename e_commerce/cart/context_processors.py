from . cart import Cart

def cart(request):
    # Return all data from recorded session
    return {'cart':Cart(request)}