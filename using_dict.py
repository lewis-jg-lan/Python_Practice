#!/usr/bin/python
#Filename:using_dict.py

#'ab' is short for 'a'ddress'b'ook

ab = {'Swaroop':'swaroop@swaroopch.com', 'Larry':'larry@wall.org', 'Matsumoto':'matz@ruby-lag.org', 'Spammer':'spammer@hotmail.com'}

print("Swaroop's address is:",ab['Swaroop'])
del ab['Spammer']
print('\n there are {0} contacts in the address-book\n'.format(len(ab)), 'They are:')
for name,address in ab.items():
    print('Contact {0} at {1}'.format(name,address))

ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido\'s address is:",ab['Guido'])

