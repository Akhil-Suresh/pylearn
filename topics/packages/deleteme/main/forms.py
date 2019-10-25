class Form(object):
	
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

	def __str__(self):
		return "Form object"
	
	def println(self):
		print "println function from form object got called"