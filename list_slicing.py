a=[5, 6, 7, 8, 9, 10, 12, 13, 17]
#  0, 1, 2, 3, 4, 5,  6,  7,  8  (index reference)
# -9,-8,-7,-6,-5,-4, -3, -2, -1,   (other way of indexing)

print(a[:])     # complete list will be printed
print(a[::])    # complete list will be printed

print(a[2:])    # slice (starting index :  ) open end means end is included
print(a[:4])    # slice ( : end) open start means all list upto index will be printed, but index is not included

print(a[0:8:2]) # slice the list from 0 index to last, but last excluded, and with interval of 2
print(a[0::2])  # slice all list with end included, and interval of 2
print(a[::2])   # slice all the list with interval of 2

