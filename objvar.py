#!/usr/bin/python
# Filename: objvar.py

class Robot:
    '''Represents a robot,with a name.'''
    #A class variable, counting the number of robots
    population = 0

    def __init__(self,name):
        '''Initializes the data.'''
        self.name = name
        print('(Initialize {0})'.format(self.name))

        #When this person is created, the robot adds to the population
        Robot.population += 1
    def __del__(self):
        '''I am dying'''
        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {0:d} robots working'.format(Robot.population))
    def SayHi(self):
        '''Greeting by the robot.
        yeah, they can do that.'''
        print('Greetings, my master call me {0}'.format(self.name))
    def howMany():
        '''Print the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    
    howmany = staticmethod(howMany)

droid1 = Robot('R2-D2')
#droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

print('\n')
print("Robots have done their works,so let\'s destroy them\n")

del droid1
del droid2

Robot.howMany()


