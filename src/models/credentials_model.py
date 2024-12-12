from email_validator import validate_email, EmailSyntaxError, EmailUndeliverableError

class CredentialsModel:

    def __init__(self, email, password):
        self.email = email
        self.password = password


    def validate_login(self):
        try:
            if not self.email:
                return "One of the inputted credentials is incorrect"
            if not self.password:
                return "One of the inputted credentials is incorrect"
            
            validate_email(self.email)
            
            return None
        
        # EmailSyntaxError happens when the email is not in the correct syntax of a valid email
        # EmailUndeliverableError happens when the domain for the email is not valid
        # we don't distinguish between the 2 errors to the user for extra security from trying to hack the account
        except (EmailSyntaxError, EmailUndeliverableError):
            return "please enter a valid email"
        
