# Controlflows 

array = ["231","123","124123","1231","123123","654236234"]

# if

if array[0] == array[1]:
    print("The first array item is esqual to the second.")
elif array[0] == array[2]:
    print("The second array item is esqual to the third.")
else:
    print("The first array item is unique in the array")

#in this case should print "The first array item is unique in the array"

# for
for number in array:
    print(number)

#in this case should print 231,123,124123,1231,123123 and 654236234

#for with range

for number in range(0, len(array) - 1):
    print(array[number])

#in this case should print 231,123,124123,1231 and 123123.

# Range

for number in range(0, len(array), 2):
    print(array[number])

#in this case should print 231,124123, 123123.

for number in range(0, 10, 2)
    print(number)

#in this case should print 0, 2, 4, 6, 8 and 10.

# defining functions

def sum_only_even(arr):
    return sum(number for number in arr if number % 2 == 0)

print(sum_only_even([0,4,6,3,2,5,1,5,6]))

#in this case should print 18.

def sum_only_odden(arr):
    return sum(number for number in arr if number % 2 != 0)

print(sum_only_even([0,4,6,3,2,5,1,5,6]))

#in this case should print 14.