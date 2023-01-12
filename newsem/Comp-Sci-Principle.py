#question 2
'''x = -1
y = 0

for i in range(10):
    add = x + y
    if add < 0:
        print(0)
    else:
        print(add)
    x += 1
    y +=1'''
#quesion 3
'''string = input('imput word:')
num = 0
for i in range(0, len(string)):
    
    print(string[num])
    num += 2'''

#3 again
'''#string = input('input word:')
print(input("Input word:")[::2])
#print(''.join([string[i] for i in range(len(string)) if i%2==0]))'''
#question4
'''def is_first_last_same(lst):
    return lst[0] == lst[-1]

result = is_first_last_same([1, 2, 3, 1])
print("The first and last number of the list is the same")
print("Result:", result)'''
#q6
'''num = (10,15,11,16,55)
for i in num:
    if i % 5 == 0:
        print(i) '''
    
#q7
'''def count_emma(string):
    count = string.count("Emma")
    print("Emma appeared", count, "times")

string = "Emma is a good developer. Emma is also a writer"
count_emma(string)'''

#q9
'''x = int(121)
if x == 121:
    print('true')
else:
    print('false')'''

'''def is_reverse_same(n):
    original = n
    reverse = int(str(n)[::-1])
    if original == reverse:
        print("Orignal and revers number is equal")
        return True
    else:
        return False
    
number = 131
print(is_reverse_same(number))'''

#q10
listOne = (10, 20, 23, 11, 17)
listTwo = (13, 43, 24, 36, 12)
for i in listOne:
    if i % 2 == 0:
        print(i)
for i in listTwo:
    if i % 2 != 0:
