# Conditional Statement/ control statements/ desicion making

#vikas mekchand

'''
    1. program memory
    2. local storage (files)
    3. Server/cloud
'''
#nuccfxu
'''
    if
    if - else
    if - elif - ... - else - (Ladder if)
    if - if -... - else - else (Nested if)
'''
#LOGIN SYSTEM

# Scenario -1
'''
user = input("Enter your username: ").lower()
pwd = input("Enter your password: ")

username = 'john'
password = 'j123'

if user == username and pwd == password:
    print(f"Welcome {user} LOOGED IN")
else:
    print("WRONG Credentials")
'''
#Scenario 2
'''
Register
    fee
        attendance
            form forward
'''
'''
username = 'john'
password = 'j123'
user = input("Enter your username: ").lower()
if user == username:
    pwd = input("Enter your password: ")
    if pwd == password:
        print(f"WELCOME {user}")
    else:
        print("WRONG PASSWORD")
else:
    print("WRONG USERNAME")
'''
#Scenario 3
# WAP to check login logic with 5 users.
'''
username = ['john','sam','mac','peter','zack']
password = {'john':'j123','mac':'m123','sam':'s123','peter':'p123','zack':'z123'}
user = input("Enter your username: ").lower() #sam
if user in username:
    print(f"WELCOME {user}")
    pwd = input("Enter your password: ") #s123
    if pwd == password[user]: #'s123' == 's123'
        print(f"LOGGED IN")
    else:
        print(f"Hello {user} you entered WRONG PASSWORD")
else:
    print("WRONG USERNAME")
'''


# SCENARIO 4
print("""
Options:
    1. Registration
    2. Login
    3. change Password
    4. Exit

""")
users = []
pwd = {}
choice = input("Enter option number: ")
print(choice)
if choice == '1':
    pass
elif choice == '2':
    pass
elif choice == '3':
    pass
elif choice == '4':
    print("Thanks for visiting")
    exit()
else:
    print("Please choose correct option")

'''
    1. CLI (Command Line Interface)
    2. GUI (Graphical User Interface) - Tkinter
    3. CGI (Common Gateway Interface) - cgi, flask, django
'''









