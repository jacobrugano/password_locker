class User:   #Class that generates new instances of contacts
    
    user_list = [] #user_list is a Class variables(variables that belong to the entire class and can be  accessed by all instances of the class. This user_list var will be used to store our created user objects
    def __init__(self,first_name,last_name,password):
                            #  __init__ method to create new instances of a class User and to allow us to pass in properties for the new object.
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


#We create a save_user() method and called it on User object to save users into the user_list using append() method.'''  
    def save_user(self):  
        User.user_list.append(self) 

#We create a delete_user method that uses the remove() method to delete the user object from the user_list.
    def delete_user(self):
         User.user_list.remove(self)

    @classmethod
    def find_by_first_name(cls,first_name):
        '''
        Method that takes in the first_name and returns the first_name that matches that number.

        Args:
            first_name: first name to search for
        Returns :
            User of person that matches the first_name.
        '''

        for first_name in cls.user_list:
            if first_name.first_name == first_name:
                return first_name