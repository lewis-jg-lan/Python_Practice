#!/usr/bin/python
#Filename: using_tuple.py

zoo = ('python','elephant','penguin')
print('There are total',len(zoo),'animals in the zoo.They are:',zoo, end=' ')

new_zoo = ('monkey','camel',zoo)
print('Number of cages in the new zoo is',len(new_zoo),'They are:\n')
for item in new_zoo:
   print(item, end=' ')

print('All animals in the new_zoo are:',new_zoo)
print('Animals brought from the old zoo are:',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is:',len(new_zoo)-1 + len(new_zoo[2]))

