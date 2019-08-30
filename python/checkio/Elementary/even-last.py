"""
Na wejściu jest tablica liczb całkowitych. Znajdź sumę elementów o parzystych indeksach (zerowy, drugi, czwarty, ...)
i pomnóż ją przez ostatni elment tablicy. Nie zapomnij, że pierwszy element ma indeks 0.

Dla pustej tablicy, wynik powinien być 0 (zero).

Wejście: List licz całkowitych.

Wyjście: Liczba całkowita.

Założenia: 0 ≤ len(tablica) ≤ 20
dla-każdego(isinstance(x, int) for x in tablica)
dla-każdego(-100 < x < 100 for x in tablica)
"""


def checkio(array):
    if len(array) == 0:
        return 0
    s = 0
    for k, x in enumerate(array):
        if k % 2 == 0:
            s = s + x
    return s * array[-1]


if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
