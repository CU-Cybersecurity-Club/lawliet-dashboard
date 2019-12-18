import os
import random

from django.test import TestCase
from django.contrib.auth.models import User
from dashboard.forms.auth import LoginForm, SignupForm
from uuid import UUID

# Helper functions

random_username = lambda rd: f"meepy-{UUID(int=rd.getrandbits(128)).hex[:10]}"
random_email = lambda rd: f"meepy-{UUID(int=rd.getrandbits(128)).hex[:10]}@colorado.edu"
random_password = lambda rd: UUID(int=rd.getrandbits(128)).hex


"""
---------------------------------------------------
LoginForm and SignupForm tests
---------------------------------------------------
"""


class SignupFormTestCase(TestCase):
    def setUp(self):
        # Set up RNG to get reproducible results
        self.rd = random.Random()
        self.rd.seed(0)

        self.username = random_username(self.rd)
        self.email = random_email(self.rd)
        self.password = random_password(self.rd)
        self.form_data = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "repassword": self.password,
        }

    def test_signup(self):
        signup_form = SignupForm(data=self.form_data)
        self.assertTrue(signup_form.is_valid())

    def test_cannot_sign_up_existing_username_or_email(self):
        signup_form = SignupForm(data=self.form_data)
        self.assertTrue(signup_form.is_valid())

        User.objects.create_user(
            username=self.username, password=self.password, email=self.email
        )

        # Can't sign up same username twice
        signup_form = SignupForm(
            data={
                "username": self.username,
                "email": random_email(self.rd),
                "password": self.password,
                "repassword": self.password,
            }
        )
        self.assertFalse(signup_form.is_valid())

        # Can't sign up same email twice
        signup_form = SignupForm(
            data={
                "username": random_username(self.rd),
                "email": self.email,
                "password": self.password,
                "repassword": self.password,
            }
        )
        self.assertFalse(signup_form.is_valid())

    def test_password_and_repassword_must_match(self):
        signup_form = SignupForm(
            data={
                "username": self.username,
                "email": self.email,
                "password": random_password(self.rd),
                "repassword": random_password(self.rd),
            }
        )
        self.assertFalse(signup_form.is_valid())


class LoginFormTestCase(TestCase):
    def setUp(self):
        # Seed RNG for reproducible results
        self.rd = random.Random()
        self.rd.seed(0)

        self.username = random_username(self.rd)
        self.email = random_email(self.rd)
        self.password = random_password(self.rd)
        self.form_data = {"username": self.username, "password": self.password}

        self.user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password
        )

    def test_login(self):
        user = User.objects.get(username=self.username)
        login_form = LoginForm(data=self.form_data)
        login_form.is_valid()
        self.assertTrue(login_form.is_valid())

        # Try a couple of invalid logins
        login_form = LoginForm(
            data={"username": self.username, "password": random_password(self.rd)}
        )
        self.assertFalse(login_form.is_valid())

        login_form = LoginForm(
            data={"username": random_username(self.rd), "password": self.password}
        )
        self.assertFalse(login_form.is_valid())
