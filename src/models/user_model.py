from email_validator import validate_email, EmailSyntaxError, EmailUndeliverableError
from models.role_model import RoleModel

class UserModel:
    def __init__(self, userId, first_name, last_name, email, password, role_id):
        self.userId = userId
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id
    
    def validate_registration(self):
        try:
            if not self.first_name:
                return "missing first name"
            if not self.last_name:
                return "missing last name"
            if not self.email:
                return "missing email"
            if not self.password:
                return "missing password"
            if not self.role_id:
                return "missing role id"

            if len(self.first_name) < 2 or len(self.first_name) > 45:
                return "first name must be between 2-45 characters"
            
            if len(self.last_name) < 2 or len(self.last_name) > 45:
                return "last name must be between 2-45 characters"
            
            if len(self.password) < 4 or len(self.password) > 50:
                return "password must be at between 4-50 characters"
            
            if self.role_id != RoleModel.Admin.value and self.role_id != RoleModel.User.value:
                return "not a valid role"
            
            validate_email(self.email)
            
            return None
        
        # EmailSyntaxError happens when the email is not in the correct syntax of a valid email
        except EmailSyntaxError:
            return "email is not valid"
        # EmailUndeliverableError happens when the domain for the email is not valid
        except EmailUndeliverableError:
            return "email domain is invalid"
