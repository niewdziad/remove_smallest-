# remove_smallest-
#
#
def remove_smallest(num, list_):: Deklaracja funkcji remove_smallest, która przyjmuje dwa argumenty: num - liczba elementów do usunięcia, list_ - oryginalna lista.
original_copy = list(list_): Tworzymy kopię oryginalnej listy, używając konstrukcji list(list_). Dzięki temu unikamy bezpośrednich zmian w oryginalnej liście.
for _ in range(num):: Pętla iterująca num razy, aby usunąć odpowiednią liczbę najmniejszych elementów.
if original_copy:: Sprawdzamy, czy kopia oryginalnej listy nie jest pusta, aby uniknąć próby usunięcia elementu z pustej listy.
original_copy.remove(min(original_copy)): Usuwamy najmniejszy element z kopii oryginalnej listy, używając funkcji min() do znalezienia najmniejszego elementu.
return original_copy: Zwracamy zmodyfikowaną kopię oryginalnej listy.
for test in tests:: Pętla iterująca przez zestaw testów.
number, original, expected = test: Dekonstrukcja testu na trzy zmienne: number - liczba elementów do usunięcia, original - oryginalna lista, expected - oczekiwany wynik.
actual = remove_smallest(number, original): Wywołanie funkcji remove_smallest z odpowiednimi argumentami i przypisanie wyniku do zmiennej actual.
assert actual == expected, "Wrong :(": Sprawdzenie, czy wynik działania funkcji zgadza się z oczekiwanym wynikiem. W przypadku niezgodności wypisujemy komunikat "Wrong :(".
assert actual is not original, "You can't change original list": Sprawdzenie, czy funkcja nie zmieniła oryginalnej listy. Jeśli tak, wypisujemy komunikat "You can't change original list".
print("All tests passed successfully!"): Komunikat informujący, że wszystkie testy zostały zakończone pomyślnie.