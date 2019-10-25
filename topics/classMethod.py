	# Class Method
	# ============
	# 	A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod.
		
	# 	The difference between a static method and a class method is:
	# 		- Static method knows nothing about the class and just deals with the parameters
	# 		- Class method works with the class since its parameter is always the class itself.
		
	# 	The class method can be called both by the class and its object.

class NameInvalidError(Exception):
	pass

class UserAccount(object):
    def __init__(self, *args, **kwargs):
        self.first_name = kwargs.get('first', '')
        self.last_name = kwargs.get('last', '')
        
    def __str__(self):
        return '{} {}'.format(self.first_name , self.last_name)

    def __repr__(self):
    	return 'UserAccount({} {})'.format(self.first_name, self.last_name)
    
    @classmethod
    def name_from_string(cls, string):
        name = string.split(' ')
        return cls(first=name[0], last=name[1])

    @staticmethod
    def is_user_name_valid(name):
    	if name == ''
    	raise NameInvalidError('Entered username is invalid')

names = ['Akhil Suresh', 'Sajitha Kumari', 'Ebin Paulose', 'Sooraj Lal']

user_accounts = [UserAccount.name_from_string(name) for name in names]

print user_accounts

UserAccount.is_user_name_valid('')
