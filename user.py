class User:   #Class that generates new instances of contacts
    
    user_list = [] #user_list is a Class variables(variables that belong to the entire class and can be  accessed by all instances of the class. This user_list var will be used to store our created user objects

    def __init__(self,first_name,last_name,password):
                            ''' __init__ method to create new instances of a class User and to allow us to 
                                pass in properties for the new object.   
                            Args:
                                first_name: User's first name.
                                last_name : User's last name.
                                pasword: User's password.
                            '''  
        self.first_name = first_name
        self.last_name = last_name
        self.password = password