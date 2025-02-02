import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        # Käyttäjätunnuksen validointi
        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")

        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username must consist of lowercase letters only")

        # Tarkistetaan, onko käyttäjätunnus jo olemassa
        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already taken")

        # Salasanan validointi
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")

        if not re.search(r"[a-zA-Z]", password):  # Tarkistaa, että salasanassa on kirjaimia
            raise UserInputError("Password must contain at least one letter")

        if not re.search(r"[0-9]", password):  # Tarkistaa, että salasanassa on numero
            raise UserInputError("Password must contain at least one number")

        # Tarkistetaan, että salasana ja sen vahvistus täsmäävät
        if password != password_confirmation:
            raise UserInputError("Passwords do not match")


user_service = UserService()
