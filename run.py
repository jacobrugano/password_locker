#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_user(username,password):
    '''
    Function to create a new user account
    '''
    new_user = User(username,password) #To create a new user
    return new_user        #To return the new User

def save_users(user):
    '''
    Function to save the user account
    '''
    user.save_user()

def save_usercredentials(credentials):
    '''
    Function to save the user usercredentials
    '''
    credentials.save_usercredentials()

def del_user(user):
    '''
    Function to delete user details
    '''
    user.delete_user()

def find_account(account):
    '''
    Function that finds an account and returns the account
    '''
    return Credentials.find_account(account)

def check_existing_contacts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exist(number)

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()

def main():
        print("Hello Welcome to your Password Locker What is your name?")
        user_name = input()

        print(f"Hello {user_name}. Kindly sign up to continue")
        print('\n')

        while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("Creating account:.....")
                            print("-"*10)

                            print ("Username of choice:.....")
                            f_name = input()

                            print("Password of choice:.....")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_user(create_useraccount(username, password)) # create and save new contact.
                            print ('\n')
                            print(f"Your username: {username} , Password:{password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_contacts(search_number):
                                    search_contact = find_contact(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

main()