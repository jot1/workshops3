__author__ = 'jc450453'
from random import randint

quick_pick=int(input("How many quick picks? "))
pick_of_6nos=[]
num=0
for i in range(0,quick_pick):
    num=randint(1,45)
    for n in range(0,6):
     while num in pick_of_6nos:
        num=randint(1,45)
     pick_of_6nos.append(num)
    print(sorted(pick_of_6nos))
    pick_of_6nos=[]


