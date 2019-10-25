import pdb

class MetaClass(object):
	"""
		This class is written here to understand the underlying concept of 
		Python double underscore methods
	"""
	def __init__(self,*args,**kwargs):
		pdb.set_trace()
		print("Object init hit")
		print("Args: ", args, " Kwargs: ", kwargs)
		
		

	def __call__(self, *args, **kwargs):
		print("The instance is being called")
		print("Args: ", args, " Kwargs: ", kwargs)
		

help(MetaClass)
sampleMetaClass = MetaClass('test', 'I dont know Why')
y = sampleMetaClass('test2', 'I dont know Why2')

