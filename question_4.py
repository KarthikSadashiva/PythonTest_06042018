###############################################################################
'''This is the 4th question input is name and age of 20 persons. Output is 
mapping them into different groups based on age
children = 0-18
youth = 19-30
middle aged = 31-60
senior = >60'''
name = []
age = []
for i in range(20):
    name.append(input("Enter the name of the family member : "))
    age.append(int(input("Enter the age of the family member : ")))
children = []
youth = []
middle_aged = []
senior = []
for i in range(20):
    if(age[i]<18):
        children.append(name[i])
    elif(age[i]>18 and age[i]<=30):
        youth.append(name[i])    
    elif(age[i]>30 and age[i]<=60):
        middle_aged.append(name[i])
    elif(age[i]>60):
        senior.append(name[i])
print("The children in the family are, ")
print(children)
print("The youth in the family are, ")
print(youth)
print("The middle-aged in the family are, ")
print(middle_aged)
print("The senior in the family are, ")
print(senior)

###############################################################################
'''OUTPUT
Enter the name of the family member : a

Enter the age of the family member : 56

Enter the name of the family member : b

Enter the age of the family member : 45

Enter the name of the family member : c98

Enter the age of the family member : 98

Enter the name of the family member : d

Enter the age of the family member : 78

Enter the name of the family member : e

Enter the age of the family member : 45

Enter the name of the family member : f

Enter the age of the family member : 23

Enter the name of the family member : g

Enter the age of the family member : 12

Enter the name of the family member : h

Enter the age of the family member : 78

Enter the name of the family member : i

Enter the age of the family member : 13

Enter the name of the family member : j

Enter the age of the family member : 56

Enter the name of the family member : k

Enter the age of the family member : 46

Enter the name of the family member : l

Enter the age of the family member : 37

Enter the name of the family member : m

Enter the age of the family member : 49

Enter the name of the family member : n

Enter the age of the family member : 65

Enter the name of the family member : o

Enter the age of the family member : 26

Enter the name of the family member : p

Enter the age of the family member : 46

Enter the name of the family member : q

Enter the age of the family member : 28

Enter the name of the family member : r

Enter the age of the family member : 48

Enter the name of the family member : s

Enter the age of the family member : 45

Enter the name of the family member : t

Enter the age of the family member : 26
The children in the family are, 
['g', 'i']
The youth in the family are, 
['f', 'o', 'q', 't']
The middle-aged in the family are, 
['a', 'b', 'e', 'j', 'k', 'l', 'm', 'p', 'r', 's']
The senior in the family are, 
['c98', 'd', 'h', 'n']
'''
###############################################################################
