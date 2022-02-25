#!/usr/bin/env python3.6

from credential import Credential

def create_credential(user_name,pass_word,phone,email):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credential(user_name,pass_word,phone,email)
    return new_credential

#We create a save_credential function that takes in a credential/contact object and then calls the save_contact method to save the credentials.
def save_credential(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()

# We create a del_credential function that takes in a credential object and then calls the delete_credential() method on the contact object deleting it from the credential list.
def del_credential(credential):
    '''
    Function to delete a credentials
    '''
    credential.delete_credential()

# We create a function find_credential that takes in a number and calls the Credentialclass method find_by_number that returns the credentials.
def find_credential(number):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credential.find_by_number(number)

# The function check_existing_credentials takes in a number as an argument and calls the class method credential_exist which returns a boolean.
def check_existing_credential(number):
    '''
    Function that check if credentials exists with that number and return a Boolean
    '''
    return Credential.credential_exist(number)

# We then create a function that displays all the credentials a user enters.

def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_credential()

def main():
        print("Hello!! Welcome to Password Locker! Kindly enter your name to proceed:..")
        user_name = input()

        print(f"Hello {user_name}. Sign up to continue")
        print('\n')

   
main()