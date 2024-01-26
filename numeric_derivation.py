
def derive(f, x, h=0.0001):

    df = (f(x+h) - f(x-h))/(2*h)
    return df  # TODO: implement this function 
