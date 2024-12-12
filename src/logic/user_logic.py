from utils.dal import DAL

class User_Logic:
    def __init__(self):
        self.dal = DAL()

    def insert_user_to_db(self, user):
        sql = "insert into second_project_db.users(firstName, lastName, email, password, roleId) values(%s, %s, %s, %s, %s)"
        parameters = (user.first_name, user.last_name, user.email, user.password, user.role_id)
        added_user_id = self.dal.insert(sql, params=parameters)
        return added_user_id
    
    def is_email_in_database(self, check_email):
        sql = "select email from second_project_db.users where email = %s"
        parameters = (check_email, )
        email = self.dal.get_scalar(sql, params=parameters)
        if email is None:
            return False
        return True
    
    def return_user_by_email_and_password(self, credentials):
        sql = "select * from second_project_db.users where (email = %s and password = %s)"
        parameters = (credentials.email, credentials.password)
        user = self.dal.get_scalar(sql, params=parameters)
        return user
    
    def is_user_in_database(self, check_userId):
        sql = "select userId from second_project_db.users where userId = %s"
        parameters = (check_userId, )
        user_id = self.dal.get_scalar(sql, params=parameters)
        if user_id is None:
            return False
        return True

