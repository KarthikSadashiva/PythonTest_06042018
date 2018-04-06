'''This is the 1st question.'''
n = 0
while(n<4):
    n = int(input("Enter the number of sentences you need to type in. It should be more than 4."))
s = []
for i in range(n):
    s.append("Enter the sentence : ")
print(s)
middle = n//2
s.insert(middle, "UST Global specializes in Healthcare, Retail & Consumer Good, Banking & Financial Services, Telecom, Media & TEchnology, Insurance, Transportation and Logistics and Manufacturing and Utilities.")
vowels = 0
uppercases = 0
lowercases = 0 
special_char = 0
repeating_words = []
ss = str(s)
for i in range(len(ss)):
    if(ss[i] in ["aeiouAEIOU"]):
        vowels += 1
    if(ss[i].islower()):
        lowercases += 1
    elif(ss[i].isupper()):
        uppercases += 1
    elif(ss[i] in '''~`!@#$%^&*()_-+={}[]:";'<>?,./'''):
         special_char += 1
print("The number of vowels in the sentence is ", vowels, " uppercase is ", uppercases, " lowercases is ", lowercases, " special chars is ", special_char)
###############################################################################
