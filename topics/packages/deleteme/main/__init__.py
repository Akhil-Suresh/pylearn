import logging

log = logging.getLogger(__name__)

if __name__ == "main":
	from main.forms import *

if __name__ == 'deleteme.main':	
	from deleteme.main.forms import *
	

log.info('Main __init__ reached')
log.debug("__name__: {}".format(__name__)) 
log.debug("__package__: {}".format(__package__))

print 'Main __init__ reached'
print "__name__: {}".format(__name__)
print "__package__: {}".format(__package__)