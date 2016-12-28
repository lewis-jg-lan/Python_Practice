if __name__ == '__main__':
	print('This program is being used by myself')
else:
	print('I am being imported by other module')

def sayhi():
	print('Hi,this is mymodule speaking')
__version__ = '0.1'
sayhi()

import using_name
using_name.sayhi()
print('Version',using_name.__version__)

from using_name import sayhi, __version__
sayhi()
print('Version',__version__)

from using_name import *
sayhi()
print("version",__version__,"name",__name__)

