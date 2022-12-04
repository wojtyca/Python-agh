import re

def __init__ (self, real, imag=0.0):
    '''Form complex number'''
    self.real = real
    self.imag = imag

def __add__(self, other):
    return complex(self.real + other.real, self.imag + other.imag)

def __sub__(self, other):
    return complex(self.real - other.real, self.imag - other.imag)

def __mul__(self, other):
    return complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.real)


def wprowadzanie():
    equation = input("podaj dzialanie\n")
    cyfry = (re.findall('-?\d+\.?\d*', equation))
    x = re.findall("j.*", equation)
    y = re.findall("[-+*]", x[0])
    print(y[0])

    i = complex(int(cyfry[0]), int(cyfry[1]))
    k = complex(int(cyfry[2]), int(cyfry[3]))
    return (y[0], i, k)

def liczenie(arg_123):
    if arg_123[0] == "+":
        print(__add__(arg_123[1],arg_123[2]))
    elif arg_123[0] == "-":
        print(__sub__(arg_123[1],arg_123[2]))
    else:
        print(__mul__(arg_123[1],arg_123[2]))

liczenie(wprowadzanie())