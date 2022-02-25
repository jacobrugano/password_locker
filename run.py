#!/usr/bin/env python3.6

from credential import Credential
from user import User


#Creating a new user
def create_user(first_name,last_name,number,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,number,password)
    return new_user

#Saving the new user
def save_user(user):
    '''
    Function to save user details
    '''
    user.save_user()

# Creating credentials
def create_credential(username,password,phone,email):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credential(username,password,phone,email)
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
                # Code for user class kwanza.
        print("Hello!! Welcome to Password Locker! Kindly enter your FIRST name:")
        first_name = input()
        print("To proceed, enter your SECOND name:..")
        last_name = input()
        print("*" * 50)
        print(f"Hello {first_name} {last_name}. Sign up to continue")
        print('\n')
        print("*" * 50)
        print ("Reply with capital: CC -to sign/Create an Account, EX -to Exit the application")
        print("*" * 50)

        while True:
            short_code = input().lower()

            if short_code == "CC":
                print("You are now creating an account on Password Locker...")
                print("Key in the following details:")
                print("Enter Username:.....")
                username = input()

                print("Enter your password:")
                password = input()


        # while True:
        #             print("Use these short codes : cc - create a new contact into Password Locker, dc - display your credentials, fc -find a contact, ex -exit the contact list ")

        #             short_code = input().lower()

        #             if short_code == 'cc':
        #                     print("New Contact")
        #                     print("-"*10)

        #                     print ("First name ....")
        #                     f_name = input()

        #                     print("Last name ...")
        #                     l_name = input()

        #                     print("Phone number ...")
        #                     p_number = input()

        #                     print("Email address ...")
        #                     e_address = input()


                    #         save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                    #         print ('\n')
                    #         print(f"New Contact {f_name} {l_name} created")
                    #         print ('\n')

                    # elif short_code == 'dc':

                    #         if display_contacts():
                    #                 print("Here is a list of all your contacts")
                    #                 print('\n')

                    #                 for contact in display_contacts():
                    #                         print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                    #                 print('\n')
                    #         else:
                    #                 print('\n')
                    #                 print("You dont seem to have any contacts saved yet")
                    #                 print('\n')

                    # elif short_code == 'fc':

                    #         print("Enter the number you want to search for")

                    #         search_number = input()
                    #         if check_existing_contacts(search_number):
                    #                 search_contact = find_contact(search_number)
                    #                 print(f"{search_contact.first_name} {search_contact.last_name}")
                    #                 print('-' * 20)

                    #                 print(f"Phone number.......{search_contact.phone_number}")
                    #                 print(f"Email address.......{search_contact.email}")
                    #         else:
                    #                 print("That contact does not exist")

                    # elif short_code == "ex":
                    #         print("Bye .......")
                    #         break
                    # else:
                    #         print("I really didn't get that. Please use the short codes")

main()