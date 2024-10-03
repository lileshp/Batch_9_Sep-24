'''
for i in range(1,5):
    print(i, end = " ")

print()
ls = ['a',2,'d',5]
for j in ls:
    print(j, end = " ")
'''


'''
iteration
    iterable
    iterator
'''
ls = [1,2,3,4] # iterable
i_ls = iter(ls) # iterator

print(type(ls))
print(type(i_ls))
print(next(i_ls)) #[1,2,3,4]
print(next(i_ls)) #[2,3,4]
print(next(i_ls)) #[3,4]
print(next(i_ls)) #[4]
#print(next(i_ls)) #[]

for i in ls: #[1,2,3,4]
    print(i)

print("HELLO")

'''
control statements:
    break
    continue
    pass
'''
print("#"*20)
for i in range(1,11):
    if i == 5:
        break
    print(i,end=" ")
else:
    print("REACHED")

'''
def login():
    pass
i = 1
if i == 1:
    login()
'''
i = 1
while i <= 10: # 10 < 10
    i += 1 # i = 1+1 = 2
    if i == 5:
        break
    print(i) # 2 3 4 5 6 7 8 9 10
ls = [1,2,4,3]

ma = ls[0] # 4
for i in range(1,len(ls)):
    if ls[i] > ma: # 3 > 4
        ma = ls[i] # 4
res = []
for i in ls:
    res.append((i + ma) * ma)
print(res)




















