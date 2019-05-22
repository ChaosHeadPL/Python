"""
Dostajesz tablicę z dodatnimi liczbami naturalnymi i liczbę N. Oblicz N-tą potęgę elementu tablicy o indeksie N.
Jeżeli N jest poza tablicą, zwróć -1. Nie zapomnij, że pierwszy element tablicy ma indeks 0.

Zobaczmy na kilka przykładów:
- tablica = [1, 2, 3, 4] i N = 2, wynik: 32 == 9;
- tablica = [1,2 ,3] i N = 3, ale N jest poza tablicą, więc wynik równa się -1.

Wejście: Dwa parametry. Tablica - lista liczb i liczba (integer).

Wyjście: Wynik jako liczba naturalna (integer).

Założenia: 0 < len(tablica) ≤ 10
0 ≤ N
dla-każdego(0 ≤ x ≤ 100 dla x w tablicy)
"""


def index_power(array, n):
    if len(array) > n:
        return pow(array[n], n)
    return -1


if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
