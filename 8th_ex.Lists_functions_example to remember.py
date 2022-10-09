"""
no of lists functions include

clear() =>> removes all elements from list
copy() =>> returns a copy of list
count() =>> returns the no of elements with specified value
extend() =>> add the elements of the list(or any iterable) to the end of current list
index() =>> returns the index of 1st element with specified value
insert() =>> adds an element at specified position
pop() =>> removes the element at specified position
remove() =>> removes the element (1st if there are multiple with same name) with specified value
reverse() =>> reverse the order of list
sort() =>> sorts the list

"""

list=["Fruits","Vegetables","Dry Fruits"]
print(list[0])#0 is index for 1st item
print(list[1])
print(list[2])


print(list[-1])#neg 1 is the last index of the list
print(list[-2])
print(list[-3])

list.append("Water") #water will be added at the end of list
print(list)
list.remove("Water") 
list.copy()
print(list)
list.count("water")
list.extend("abc") #these will be added at the end, each letter separated
print(list)
list.pop(0) #item at index 1 will be deleted.
print(list)
