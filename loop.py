'''
Loop/iteration
    for -> know the iteration count

        for variable in sequence/iterable:
            for body

    while -> iteration depends on condition

        while condition:
            while body
            inc/dec

range()
    range(start, end, steps)
    start: optional. default = 0
    end: required
    steps: optional default = 1

    range(10)
    range(1,20)
    range(1,21,2)


'''

# 1
'''
for i in range(10):
    print(f"{i} Hello",end=" ")
'''
# 2
#WAP to print numbers from  1 to 20
'''
for i in range(1,21):
    print(i,end=" ")
'''
#3
#WAP to print numbers from 1 to 100 (odd numbers)
'''
for i in range(1,101):
    if i % 2 != 0:
        print(i, end=" ")
'''

#4
#WAP to print numbers from 20 to 1
'''
for i in range(20,0,-1):
    print(i, end=" ")
'''
#5 WAP to print all numbers between 2452 to 4587,
# which is divisible by 5 and multiple of 3.
'''
start = 2452
end = 4587
for i in range(start,end+1):
    if i % 5 == 0 and i % 3 ==0:
        print(i)
'''
li = ['john','sam','peter','mac','johny','Jack']
#6 WAP to return a list of all elements from
# given list whose first letter is 'j/J'
res = []
'''
for i in li:
    if i[0] == 'j' or i[0] == 'J':
    #if i.lower()[0] == 'j':
        res.append(i)
print(res)
'''
'''
for i in range(len(li)): # 0
    if li[i].lower()[0] == 'j': # john
        res.append(li[i])
print(res)
'''
'''
for i in li:
    #if i.startswith('j') or i.startswith('J'):
    if i.lower().startswith('j'):
        res.append(i)
print(res)
'''
'''
code = "ABCD-1234-EFGH"
for i in code.lower():
    print(i)
'''
'''
di = {'name':'john','city':'Bhopal','clg': 'LNCT','age':25}
for key,val in di.items():
    print(f"{key} = {val}")
'''

'''
given an array.
    1. fetch maximum value from given array
    2. add maximum value with each element of array
    3. multiply max value with new array's each element
    and return new updated array.

'''


















