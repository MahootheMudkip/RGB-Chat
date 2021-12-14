import re
from data_operations import add_user


def auth_login_v1(email, password):

    return {
        'auth_user_id'
    }


def auth_register_v1(email, name_first, name_last, password):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'

    if not re.match(pattern, email):
        raise ValueError('Invalid email')

    if len(password) < 6:
        raise ValueError('Invalid password length')

    if not 1 < len(name_first) < 25 and 1 < len(name_last) < 25:
        raise ValueError('Invalid name length')

    # Passed error checks, add user using SQL function
    user_id = add_user(email, name_first, name_last, password, '', '')

    return {
        'auth_user_id': user_id
    }


auth_register_v1('mrmaxilikestoeat@gmail.com', 'Christian', 'Lam', '123456')
