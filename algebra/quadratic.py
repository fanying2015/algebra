

def poly(*args):
    """
    
    f(x) = a * x + b * x**2 + c * x**3 + ...
    
    *args = (x, a, b)
    """
    
    if len(args) == 1:
        raise Exception("You have only entered a value for x, and no cofficients.")
    
    x = args[0] # x value
    
    coef = args[1:]
    results = 0
    for power, c in enumerate(coef):
        results += c * (x ** (power + 1))
        
    
    return results