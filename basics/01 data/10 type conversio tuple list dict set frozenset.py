#konwersje typów typle() oraz list()

listData = [1,2,3,4]

tupleData = tuple(listData)
print(type(tupleData))
print(tupleData)

otherList = list(("ola", 23, 234))
print(type(otherList))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

tupleData = (("Ola", 1234), ("Adam", 23654))
dictData = dict(tupleData)
print(dictData)
print(dictData["Ola"])