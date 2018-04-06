name = []#['a','b','c','d','e','f','g','h','i','j']
sub1 = []#[67,78,89,90,91,76,56,46,67,87]
sub2 = []#[67,78,89,90,91,76,56,46,67,87]
sub3 = []#[67,78,89,90,91,76,56,46,67,87]
for i in range(10):
    name.append(input("Enter the name of the student : "))
    sub1.append(int(input("Enter the marks obtained in subject 1 : ")))
    sub2.append(int(input("Enter the marks obtained in subject 2 : ")))
    sub3.append(int(input("Enter the marks obtained in subject 3 : ")))
print("Name\tSub1\tSub2\tSub3")
for i in range(10):
    print(name[i], sub1[i], sub2[i], sub3[i])
print()    
print("Subject\tMean\tMode\tMedian")
print("Subject 1",np.mean(sub1),stats.mode(sub1),np.median(sub1))
print("Subject 2",np.mean(sub2),stats.mode(sub2),np.median(sub2))
print("Subject 3",np.mean(sub3),stats.mode(sub3),np.median(sub3))

total = []
for i in range(10):
    total.append((sub1[i]+sub2[i]+sub3[i])/3)
total_names = list(zip(total,name))
total_names.sort()
print("Top 3 students : ")
for i in range(3):
    print(total_names[9-i])

print("Subject Marks in sorted order")
sub1.sort()
sub2.sort()
sub3.sort()
print("Sub1 : " , sub1)
print("Sub2 : " , sub2)
print("Sub3 : " , sub3)

grade = []
for i in range(10):
    if(total[i]<50):
        grade.append("D")
    elif(total[i]>50 and total[i]<=60):
        grade.append("C")
    elif(total[i]>60 and total[i]<=70):
        grade.append("B")
    elif(total[i]>70 and total[i]<=80):
        grade.append("B+")
    elif(total[i]>80 and total[i]<=90):
        grade.append("A")
    elif(total[i]>90):
        grade.append("A+")
print("The grdaes of the student are as follows : ")
for i in range(10):
    print(name[i], grade[i])
    
###############################################################################
'''    OUTPUT
Subject Mean    Mode    Median
Subject 1 74.7 ModeResult(mode=array([67]), count=array([2])) 77.0
Subject 2 74.7 ModeResult(mode=array([67]), count=array([2])) 77.0
Subject 3 74.7 ModeResult(mode=array([67]), count=array([2])) 77.0
Top 3 students : 
(91.0, 'e')
(90.0, 'd')
(89.0, 'c')
Subject Marks in sorted order
Sub1 :  [46, 56, 67, 67, 76, 78, 87, 89, 90, 91]
Sub2 :  [46, 56, 67, 67, 76, 78, 87, 89, 90, 91]
Sub3 :  [46, 56, 67, 67, 76, 78, 87, 89, 90, 91]
The grdaes of the student are as follows : 
a B
b B+
c A
d A
e A+
f B+
g C
h D
i B
j A
'''
###############################################################################
