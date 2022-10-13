def integral(a: float, b: float, n: float, left: bool, func) -> float:
    '''
    Integrates a function in a set interval  [a, b] based on  Riemanns numerical method
    '''
    dx = (b - a) / n
    thesum = 0 
    if left:
        for i in range(n):
            thesum = thesum + func( a + i * dx ) * dx
        return thesum

    else:
        for i in range(n):
            thesum = thesum + func(a + ( i + 1 )* dx) * dx
        return thesum



def f(x):
    return x**2 - 2*x + 2


#print(round(integral(1, 5, 100, 1, f),2))




