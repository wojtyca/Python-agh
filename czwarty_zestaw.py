import cmath
import numpy as np

#############zad1###########

def row_kwadrat():
    x = list(map(int, input("Enter multiple values: ").split()))

    delta = (x[1]**2) - (4*x[0]*x[2])
    sol1 = (-x[1]-cmath.sqrt(delta))/(2*x[0])
    sol2 = (-x[1]+cmath.sqrt(delta))/(2*x[0])

    print('The solutions are {0} and {1}'.format(sol1,sol2))


###########zad3###########

def matrix_skalar():
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    c = np.dot(a, b)
    print(c)

############zad4############

def matrix_add():
    a = np.random.randint(0, 10, size=(3, 3))
    b = np.random.randint(0, 10, size=(3, 3))
    c = np.add(a,b)
    print("pierwsza macierz:\n", a,  "\ndruga macierz:\n", b, "\nmacierz wynikowa:\n", c)


########zad5########
def matrix_multiply():
    a = np.random.randint(0, 10, size=(3, 3))
    b = np.random.randint(0, 10, size=(3, 3))
    c = np.multiply( a, b)
    print("pierwsza macierz:\n", a, "\ndruga macierz:\n", b, "\nmacierz wynikowa:\n", c)

#######zad6########

def matrix_wyznacznik():
    a = np.random.randint(0, 10, size=(3, 3))
    print(np.linalg.det(a))

matrix_wyznacznik()