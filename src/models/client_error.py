# model to create our own exceptions tailored to the errors in our website
# they inherit from the Exception class and use it

class ClientError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class ResourceNotFound(ClientError):
    def __init__(self, message, id):
        super().__init__(message)
        self.message = message
        self.id = id
    
class ValidationError(ClientError):
    def __init__(self, message, model):
        super().__init__(message)
        self.message = message
        self.model = model


class AuthError(ClientError):
    def __init__(self, message, model = None):
        super().__init__(message)
        self.message = message
        self.model = model