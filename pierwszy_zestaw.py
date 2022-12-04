#!/usr/bin/python3

def hello():
    print("Hello world")

def dane():
    x, y, z = input("Podaj imie, nazwisko i rok urodzenia: ").split()
    return(x,y,z)

def szyfr(imie,nazwisko,rok):
    part1=imie[::-1] #odwrocenie stringa
    part2=nazwisko[0] #pierwsza litera stringa
    part3=(int(rok)//20) #int/20 bez cyfr po przecinku
    return part1+part2+str(part3)

def main():
    wygenerowane = szyfr(*dane())
    haslo = input("podaj hasło")
    if haslo == wygenerowane:
        print ("zgadles!!")
    else:
        print ("nie zgadles")

main();

