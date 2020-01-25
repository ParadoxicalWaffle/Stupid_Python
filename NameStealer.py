"""
Program Name: Name Stealer
Author: ParadoxicalWaffle
Version: 1.21.2020.1

"""
import time
n = 1
code_attempt = '1'
list = []
while code_attempt != '12345':
    print('Welcome victim number',n)
    time.sleep(1)
    name = input('Type in your name please: ')
    while name in list:
        print("Ha! You fool, I already have that name!")
        name = input('Type in a different name: ')
    print('No, my name is',name)
    print('What do you say to that?')
    input()
    print("Eat my shorts fleshbag, it's my name now")
    list.append(name)
    time.sleep(1)
    print("I'll give it back if you enter the secret code")
    code_attempt = input("What's the secret code, human?: ")
    if code_attempt=='12345' :
        continue
    else:
        print('Ha! I get to keep your name forever!')
        n += 1
        time.sleep(1)
else:
    print('Good job, well played')
    print('I guess you can have your name back')
    print("Here are all the names I stole, I'm sorry\n", list)
    list.clear
    time.sleep(5)
