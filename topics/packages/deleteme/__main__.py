
print "Executing from deleteme __main__.py"

if __name__ == '__main__':
	import sys
	import logging
	logging.basicConfig(level='DEBUG')
	
	print "Sys Path is : {}".format(sys.path)
	from accounts import login


