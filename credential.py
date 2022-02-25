class Credential:   #Class that generates new instances of credentials
    
    credential_list = [] #credential_list is a Class variables(variables that belong to the entire class and can be  accessed by all instances of the class. This user_list var will be used to store our created user objects
    def __init__(self,username,password,number):
                            #  __init__ method to create new instances of a class Credential and to allow us to pass in properties for the new object.
        self.username = username
        self.password = password
        self.phone_number = number


#We create a credential_user() method and called it on Credential object to save credentialss into the credential_list using append() method.'''  
    def save_credential(self):  
        Credential.credential_list.append(self) 

#We create a delete_credential method that uses the remove() method to delete the credential object from the credential_list.
    def delete_credential(self):
        Credential.credential_list.remove(self)


    @classmethod #///////////////1
    def find_by_username(cls,username):
        '''
        Method that takes in the username and returns a username that matches that name.
        Args:
            number: username to search for
        Returns :
            Credentials of person that matches the username.
        '''
        for credential in cls.credential_list:
            if credential.username == username:
                return credential

    
    @classmethod             #///////////////2
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list