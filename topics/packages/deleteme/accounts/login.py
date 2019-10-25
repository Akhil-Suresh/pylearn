
# When python is run as module
if __name__ == 'deleteme.accounts.login':
	from deleteme import main

if __name__ == 'accounts.login':
	import main

print "Executing from login.py"
print "	__name__: {}".format(__name__)
print "	__package__: {}".format(__package__)

form = main.Form()
form.println()

