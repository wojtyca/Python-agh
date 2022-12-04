import random

def array_random_generator(value_count):
    random_array = []
    for i in range(value_count):
        random_array.append(random.randint(0, 100))
    return random_array

def sorter(array_prod):

    n = len(array_prod)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array_prod[j] > array_prod[j + 1]:

                array_prod[j], array_prod[j + 1] = array_prod[j + 1], array_prod[j]
                already_sorted = False

        if already_sorted:
            break

    array_prod.reverse()
    print("wynikowa macierz:\n", array_prod, "\n")
    return (array_prod)

def sorting_tester(sorted_array):
    n = len(sorted_array)
    for i in range(n-1):
        if sorted_array[i] >= sorted_array[i+1]:
            continue
        else:
            print ("blad, indeks:",i)
            exit(0)
    print("pass")


sorting_tester(sorter(array_random_generator(50)))

