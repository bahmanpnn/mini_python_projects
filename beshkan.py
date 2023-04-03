"""
in this project we want to have a game that with one beshkan(persian word) or click in one button;
every 49 from 50 people give 1$ to one person.at the end everyone that no money to give to others
faild and go out from game.at last we use matploit and chart to show them how many people 
will have no money after n round of beshkan/click
"""

import random

people=[]
for i in range(0,50):
    #50 people that have 100$
    people.append(100)

#this loop is for round of beshkan and click that is 1000 round
for beshkan in range(0,1000):
    #this loop is for choose random one person from 50 
    for person in range(0,50):
        person2=random.randrange(0,50)

        # this while is for dont choose person that has no money and faild from game
        while people[person2]==0:
            person2=random.randrange(0,50)

        #check person1 has money too give random to others.if person has no money loop cross from it
        if people[person] !=0:
            people[person]=people[person]-1
            people[person2]=people[person2]+1

#we can sort money of people to know how many people that have no money or other data.
# one of sorting way is use list.sort()
# people.sort()

#now we want to user chart to show money of people
import matplotlib.pyplot as plt
#first field of bar is width of our chart and next one is height of our chart that is money of people
print(plt.bar(range(0,50),sorted(people)))
# print(plt.bar(range(0,50),sorted(people,reverse=True)))