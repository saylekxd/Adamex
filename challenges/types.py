numbers = [7, 8, 9, 10, 11, 12]
print(numbers)

tupleNumbers = tuple(numbers)
print(tupleNumbers)

mixedList = [18, "helloWorld", 19.3]
print(mixedList)

setMixed = set(mixedList)
print(setMixed)
print(type(setMixed))

frozenSetNumbers = frozenset(tupleNumbers)
print(type(frozenSetNumbers))
print(frozenSetNumbers)

nameAgePairs = (("Aleks", 18),("Marek", 28))
dictAgePairs = dict(nameAgePairs)
print(dictAgePairs["Marek"])

