'''This is the 3rd question. I do not know how exactly merge sort work. 
But I had heard that sort() function in python uses merge sort to quickly 
sort the numbers, hence using the inbuilt function.'''
num = [12,6,48,37,88,31,54,11,60,122,105,88,122,155,105]
num.sort()
print(num)
num_input = []
length = int(input("Please enter the number of elements in the list"))
for i in range(length):
    num_input.append(int(input("Enter the list value : ")))
num_input.sort()
print(num_input)

###############################################################################
''' OUTPUT
[6, 11, 12, 31, 37, 48, 54, 60, 88, 88, 105, 105, 122, 122, 155]

Please enter the number of elements in the list5

Enter the list value : 95

Enter the list value : 68

Enter the list value : 45

Enter the list value : 26

Enter the list value : 13
[13, 26, 45, 68, 95]
'''
###############################################################################
