import pytest

from src.auth import auth_login_v1

# def auth_login_v1(email, password):


def test_user_taken():
    with pytest.raises(ValueError):
        auth_login_v1('poo@gmail.com', '1234557')


def test_password_incorrect():
    with pytest.raises(ValueError):
        auth_register_v1('poo@gmail.com', '1234557', 'Michel', 'Gao')
        auth_login_v1('poo@gmail.com', '12345678')
