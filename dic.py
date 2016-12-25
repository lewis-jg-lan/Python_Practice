bob = dict(name='Bob Smith',age=42,pay=300,job='dev')
sue = dict(name='Sue hehe',age=32,pay=3433,job='soft')
print(bob)
print(sue)

keys = ['name','age','pay','job']
values = ['Smith John',34,4000,'dev']
print(list(zip(keys,values)))
sue = dict(zip(keys,values))
print(sue)
value = sue.get("name")
print(value)

print
for i in range(10,0,-1):
    print('i = %d' % i)
print

i = 10
while i>0:
	print('i = %d' % i)
	i -= 1;
print

for i in range(10):
    print(i)





