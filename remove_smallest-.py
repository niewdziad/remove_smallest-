def remove_smallest(num, list_):
    # Tworzymy kopię oryginalnej listy, aby nie zmieniać jej bezpośrednio
    original_copy = list(list_)
    
    # Usuwamy daną liczbę najmniejszych elementów z kopii oryginalnej listy
    for _ in range(num):
        if original_copy:
            original_copy.remove(min(original_copy))
    
    # Zwracamy zmodyfikowaną kopię oryginalnej listy
    return original_copy

# Testy
tests = [
    (3, [1,2,3,1,2,4], [3,2,4]), 
    (2, [5,4,1,3], [5,4]), 
    (4, [1,2,1], [])
]

for test in tests:
    number, original, expected = test
    actual = remove_smallest(number, original)
    assert actual == expected, "Wrong :("
    assert actual is not original, "You can't change original list"

print("All tests passed successfully!")