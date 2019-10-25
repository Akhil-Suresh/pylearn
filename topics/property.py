    # Property of class
    # @property 
    # the use of property mainly happens when there is a derived attribute 
    # say suppose you have an user account which takes in last and first name.
    # So now there appears the need to derive a full name from both

    # we can do that by defining a method on the class say 
    #   def full_name(self):
    #       return self.first_name + self.last_name

    # so each time when you need full name you have to call like user_obj.full_name(). 
    # A much convinient way will be defining it as property of class inside init
    # as 
    #   def __inti__(self, first, last):
    #       self.first = first
    #       self.last = last
    #       self.full_name = self.first + self.last

    # so that we can call it like user_obj.full_name
    # But the main problem with this is that. first_name and last_name wont get updated
    # when you change either first name or last_name. Which is a serious trouble

    # In order to overcome that limitation property is introduced

class UserAccount(object):
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    @property
    def full_name(self):
        return self.first_name + self.last_name


# The getters, setters and deleters 
# However there is a minor issue with the above this,
# Think what happens when a user try to change the full_name like below
# user_obj.full_name = 'Anupam Suresh'
# This is going to create a serious trouble. So what we can possibly do is
# provide setters and deleters for that
class InvalidOperation(Exception):
    pass


class UserAccount(object):
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    @property
    def full_name(self):
        return self.first_name + self.last_name

    @full_name.setter
    def full_name(self, name):        
        first, last = name.split()
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        raise InvalidOperation("You can't delete full_name. That is similar to deleting Account")







import unittest 
  
class UserAccountTest(unittest.TestCase): 
  
    def setUp(self):
        self.user_obj = UserAccount(first='akhil', last='suresh')

    def test__full_name(self):
        user_obj = self.user_obj
        self.assertTrue(user_obj.full_name == 'akhilsuresh')
    
    def test__change_last_name(self):
        self.user_obj.last_name = 'anupam'
        self.assertTrue(self.user_obj.full_name == 'akhilanupam')

    def test__change_full_name(self):
        self.user_obj.full_name = 'Anupam Suresh'
        self.assertTrue(self.user_obj.full_name == 'AnupamSuresh')

    def test_del_full_name(self):
        with self.assertRaises(InvalidOperation) as context:
            del self.user_obj.full_name
            self.assertTrue("You can't delete full_name. That is similar to deleting Account" in context.exception)


if __name__ == '__main__':
    unittest.main()