first = ["Apple", "Guava", "Mango", "Banana", "Kiwi"]

print("Length of list: ", len(first))
print("First element: ", first[0])
print("Last element: ", first[-1])

first.append("Pineapple")
print("Updated list: ", first)

first.remove("Guava")
print("Updated list: ", first)

first.sort()
print("Sorted list: ", first)

first.pop(1)
print("Updated list: ", first)

first.reverse()
print("Reversed list: ", first)

print("Multiplication of list: ", first*2)

first = first[:4]
print("Sliced list: ", first)

first.clear()
print("Cleared list: ", first)