from flask import request, session
from utils.cyber import Cyber
from models.user_model import UserModel
from models.credentials_model import CredentialsModel
from models.role_model import RoleModel
from models.client_error import ValidationError, AuthError
from logic.user_logic import User_Logic

class UserFacade:

    def __init__(self):
        self.logic = User_Logic()

    def user_sign_up(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = UserModel(None, first_name, last_name, email, password, RoleModel.User.value)
        do_we_have_validation_error = user.validate_registration()
        if do_we_have_validation_error:
            raise ValidationError(do_we_have_validation_error, user)
        
        if self.logic.is_email_in_database(email):
            raise ValidationError("Email is already taken", user)
        
        user.password = Cyber.hash(user.password)

        self.logic.insert_user_to_db(user)
        
        

    def user_log_in(self):
        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialsModel(email, password)
        do_we_have_validation_error = credentials.validate_login()
        if do_we_have_validation_error:
            raise ValidationError(do_we_have_validation_error, credentials)

        hashed_password = Cyber.hash(password)
        credentials.password = hashed_password
        
        user = self.logic.return_user_by_email_and_password(credentials)
        if not user:
            raise ValidationError("user does not exist", credentials)
        
        del user["password"]
        session["current_user"] = user


    def user_log_out(self):
        session.clear()

    @staticmethod
    def block_anonymous():
        user = session.get("current_user")
        if not user:
            raise AuthError("you are not logged in")
    
    @staticmethod
    def block_non_admin():
        user = session.get("current_user")
        if not user:
            raise AuthError("you are not logged in")
        if user["roleId"] != RoleModel.Admin.value:
            raise AuthError("you are not allowed to do that")


    def close(self):
        self.logic.dal.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

