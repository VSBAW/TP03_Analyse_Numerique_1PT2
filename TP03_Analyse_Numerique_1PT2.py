"""TP03 Analyse numérique"""
"""Bonjour Madame/Monsieur, Voici notre progamme dédié à la resolution  par la methode de Newton des équations"""



import math

def Newton (f, fder, x0, epsilon, Nitermax) :
    n = 1
    xold = x0
    xnew = xold-(f(xold)/fder(xold))
    difference = xnew-xold
       
    while abs(difference) > epsilon and n < Nitermax :
        xnew = xold-(f(xold)/fder(xold))
        n= n+1
        difference = xnew - xold
        xold = xnew
        print (xnew, n, xnew - xold)
    return xnew


def f1(x):
    return((x**4)+(3*x)-9)

def f1der(x):
    return((4*(x**3)+3))

def f2(x):
    return((3*(math.cos(x)))-2-x)

def f2der(x):
    return((-math.sin(x))-1)

def f3(x):
    return(x*(math.exp(x))-7)

def f3der(x):
    return((math.exp(x))+x*math.exp(x))


def f4(x):
    return math.exp(x)-x-10

def f4der(x):
    return math.exp(x)-1

def f5(x):
    return(x+5-2*math.tan(x))

def f5der(x):
    return(1-(2/(math.cos(x))**2))

def f6(x):
    return(math.exp(x)-(x**2)-3)

def f6der(x):
    return(math.exp(x)-(2*x))

def f7(x):
    return((3*x)+(4*math.log(x))-7)

def f7der(x):
    return 3+((4/x))

def f8(x):
    return((x**4)-2*(x**2)+(4*x)-17)

def f8der(x):
    return(4*(x**3)-(4*x)+4)

def f9(x):
    return(math.exp(x)-(2*math.sin(x))-7)


def f9der(x):
    return(math.exp(x)-(2*math.cos(x)))

def f10(x):
    return(((math.log((x**2)+4))*(math.exp(x)))-10)

def f10der(x):
    return(((2*x)*math.exp(x)/((x**2)+4))+((math.log((x**2)+4))*math.exp(x)))

print ("="*5,"Fonction 1","="*5)

solf1 = Newton(f1, f1der, -2, 1E-10, 1E4) 
print (solf1, "Est solution  négative de f1")
solf1bis = Newton(f1, f1der, 0, 1E-10, 1E4)
print (solf1bis, "Est solution positive de f1")

print ("="*5,"Fonction 2","="*5)

solf2= Newton(f2, f2der, 0, 1E-10, 1E4)
print(solf2, "Est solution positive de f2")
solf2bis = Newton(f2, f2der, -1, 1E-10, 1E4)
print (solf2bis, "Est solution négative de f2")

print ("="*5,"Fonction 3","="*5)

solf3 = Newton(f3, f3der, 1, 1E-10, 1E4)    
print (solf3, "Est solution de f3")

print ("="*5,"Fonction 4","="*5)

solf4 = Newton(f4, f4der, -12, 1E-10, 1E4)
print(solf4, "Est solution negative de f4")
 
solf4bis = Newton(f4, f4der, 4, 1E-10, 1E4)
print(solf4bis, "Est solution  positive de f4")

print ("="*5,"Fonction 5","="*5)

solf5 = Newton(f5, f5der, 1, 1E-10, 1E4)
print(solf5, "Est solution de f5")

print ("="*5,"Fonction 10","="*5)

solf10=Newton(f10, f10der, 0, 1E-10, 1E4)
print(solf10, "Est solution de f10") 

print ("="*5,"Fonction 9","="*5)

solf9=Newton(f9, f9der,2.15, 1E-0, 1E4)
print(solf9, "Est solution de f9")

print ("="*5,"Fonction 8","="*5)

solf8=Newton(f8, f8der,2 ,1E-10, 1E4)
print(solf8, "Est solution positive de f8 ")

solf8bis=Newton(f8, f8der,-3 ,1E-10, 1E4)
print(solf8bis, "Est solution négative de f8")

print ("="*5,"Fonction 7","="*5)

solf7=Newton(f7, f7der,0.5 ,1E-10, 1E4)
print(solf7, "Est solution de f7")

print ("="*5,"Fonction 6","="*5)

sol6=Newton(f6, f6der,1.5, 1E-10, 1E4)
print(sol6, "Est solution de f6")

