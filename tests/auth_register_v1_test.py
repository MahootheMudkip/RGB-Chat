import pytest

from src.auth import auth_register_v1
'''
email entered is not a valid email 
email address is already being used by another user
length of password is less than 6 characters
length of name_first is not between 1 and 50 characters inclusive
length of name_last is not between 1 and 50 characters inclusive
'''


def test_invalid_password_length():
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '12345', 'Michael', 'Gao')


def test_user_taken():
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '1234567', 'Michael', 'Gao')
        auth_register_v1('poo@gmail.com', '1234557', 'Michel', 'Go')


def test_invalid_first_name():
    # 0 characters first name
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '1234567', '', 'Gao')
    # 51 characters first name
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '1234567',
                         'Michaellllllllllllllllllllllllllllllllllllllllsdhafsagkjreewjthfsdyjugdkhjgfyutfhdetstuyellllllllllll', 'Gao')


def test_invalid_last_name():
    # 0 characters last name
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '1234567', 'firstname', '')
    # 51 characters last name
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '1234567', 'firstname',
                         'Michaellllllllllllllllllllllllllllllllllllllllsdhafsagkjreewjthfsdyjugdkhjgfyutfhdetstuyellllllllllll')


def test_user_taken():

    #no .com
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail', '1234567', 'Michael', 'Gao')

    # no @
    with pytest.raises(ValueError):
        auth_register_v1('poogmail.com', '1234567', 'Michael', 'Gao')

    # nothing
    with pytest.raises(ValueError):
        auth_register_v1('poo', '1234567', 'Michael', 'Gao')
