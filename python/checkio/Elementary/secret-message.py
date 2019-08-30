"""
Czy próbowaliście wysłać sekretną wiadomość do kogoś używając poczty? Można by użyć gazety, żeby powiedzieć Twój sekret. Nawet jeśli ktoś znajdzie Twoją wiadomość, łatwo go zbyć, że to jest paranoja i fałszywa teoria spiskowa. Najprostszy sposób, żeby ukryć wiadomość, to użyć wielkich liter. Znajdźmy jakieś ukryte wiadomości!

Na wejściu jest kawałek tekstu. Zbierz wszystkie wielkie litery w jeden wyraz w kolejności, w której pojawiły się w tekście.

Na przykład: tekst = "How are you? Eh, ok. Low or Lower? Ohhh.", jeżeli zbierzemy wszystkie wielkie litery, dostaniemy wiadomość "HELLO".

Wejście: Tekst jako napis (unicode).

Wyjście: Sekrenta wiadomość jako napis lub pusty napis.

Założenia: 0 < len(tekst) ≤ 1000
dla-każego(ch in string.printable for ch in tekst)
"""


def find_message(text):
    message = ""
    for x, y in enumerate(text):
        if text[x].isupper():
            message = message+y
    return message


if __name__ == '__main__':
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
