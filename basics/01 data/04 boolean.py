# Przykład wartości Boolean

""" Wartości Boolean, nazywane również typem logicznym, to bardzo podstawowy typ danych w programowaniu, który może przyjmować jedną z dwóch wartości: `True` (prawda) lub `False` (fałsz). Są one używane do reprezentowania prawdy lub fałszu w logice i operacjach warunkowych.

Oto kilka kluczowych punktów na temat wartości Boolean:

1. **Podstawowe operacje logiczne**: Wartości Boolean są często używane z operatorami logicznymi takimi jak AND (`and`), OR (`or`), NOT (`not`), aby tworzyć bardziej złożone wyrażenia logiczne. Na przykład, `True and False` zwróci `False`, ponieważ obie strony operacji AND muszą być prawdziwe, aby całe wyrażenie było prawdziwe.

2. **Porównania**: Wartości Boolean są często wynikiem porównań. Na przykład, wyrażenie `5 > 2` zwraca `True`, ponieważ 5 jest rzeczywiście większe niż 2.

3. **Warunki**: Są one używane w instrukcjach warunkowych (takich jak `if`), aby kontrolować przepływ programu. Na przykład, jeśli warunek `if` jest `True`, blok kodu zostanie wykonany. Jeśli jest `False`, blok kodu zostanie pominięty.

4. **Reprezentacja prawdy/fałszu**: Wartości Boolean mogą być również używane do reprezentowania stanu lub warunku, na przykład, czy użytkownik jest zalogowany (`True`) czy nie (`False`).

Wartości Boolean są fundamentalne w programowaniu, ponieważ pozwalają na podejmowanie decyzji w kodzie na podstawie logiki i warunków.
"""

is_active = True
print(is_active) # Wypisuje True

# Porównanie zwracające wartość Boolean
is_greater = 5 > 2
print(is_greater) # Wypisuje True, ponieważ 5 jest większe niż 2

# Operacje logiczne na wartościach Boolean
a = True
b = False

# Operator AND
print(a and b) # Wypisuje False, ponieważ obie wartości muszą być True, aby wynik był True

# Operator OR
print(a or b) # Wypisuje True, ponieważ wystarczy, że jedna z wartości jest True

# Negacja
print(not a) # Wypisuje False, ponieważ neguje wartość True

# -----------------------------------------