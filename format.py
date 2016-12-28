#practice1
age = 25
name = "hehehe"
print('{0} is {1} years old'.format(name, age))
print('Why is {0} playing with that python?'.format(name))

#practice2
number = 23
running = True
while running:
	guess = int(input("Enter an integer:"))
	if guess == number:
		print("Congratulation,you guessed it.")
		running = False
	elif guess < number:
		print("No, it is a litter lower.")
	else:
		print("No, it is a litter higher.")
else:
	print("the while loop is over.")
print("done")


#practice3
while True:
	s = (input('Enter something:'))
	if s=='quit':
		break;
	print('Length of the string is',len(s))
	if len(s) < 3:
		print("Too small")
	continue;
    print
print("done")

#practice4
def sayHello():
	print('hello world!')
sayHello()

#practice5
def printMax(a,b):
	if a >= b:
		print(a, 'is maximum')
	else:
		print(b,'is maximum')

printMax(3,4)
x=5
y=7
printMax(x,y)


#practice6
x=50
def func(x):
	print('x is',x)
	x=2
	print('changed local x to',x)

func(x)
print("x is still",x)


#practice7
x=50
def func2():
	global x
	print('x is ',x)
	x=2
	print('changed global x to be',x)

func2()
print('value of x is',x)


#practice8
def func_outer():
	x=2
	print('x is',x)

	def func_inner():
		nonlocal x
		x=5
	func_inner()
	print("changed local x to",x)
func_outer()

#practice9
def say(message,times):
	print(message*times)

say('hello')
say('me',5)

#practice10
def func3(a,b=5,c=10):
	print('a is',a,'and b is',b,'and C is',c])
func3(3,7)
func3(25,c=24)
func3(c=250,a=100)

#practice11
def total(initial=5, *numbers, **keywords):
	count = initial
	for number in  numbers:
		count += number
	for key in keywords:
		count += keywords[key]
	return count
print(total(10,1,2,3,4,vegetables=50, fruits=100))


#docStrings
def printMax(x,y):
	'''Prints the maximum of two numbers.
	the two values must be integers.'''
	x=int(x)
	y=int(y)
	if x>y:
		print(x, 'is maximum')
	else:
		print(y,'is maximum')
printMax(3,5)
print(printMax.__doc__)

#using_sys.py
import sys
print('The command line arguments are:')
for i in sys.argv:
	print(i)
print('\n\nThe PYTHONPATH is',sys.path,'\n')



