#!/usr/bin/env python3.6

from credential import Credential

def create_credential(user_name,pass_word,phone,email):
    '''
    Function to create a new user credentials
    '''
    new_credential = Credential(user_name,pass_word,phone,email)
    return new_credential
