import logging

log = logging.getLogger(__name__)


log.info('Account __init__ reached')
log.debug("__name__: {}".format(__name__)) 
log.debug("__package__: {}".format(__package__))

print 'Account __init__ reached'
print "__name__: {}".format(__name__)
print "__package__: {}".format(__package__)