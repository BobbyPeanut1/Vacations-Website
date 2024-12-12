from utils.dal import DAL
from time import sleep

class Like_Logic:
    def __init__(self):
        self.dal = DAL()

    def like_vacation(self, userId, vacationId):
        sql = "insert into second_project_db.likedvacations(userId, vacationId) values(%s, %s)"
        parameters = (userId, vacationId)
        result = self.dal.insert(sql, params=parameters)
        return result
    
    def did_user_like_vacation_already(self, check_userId, check_vacationId):
        sql = "select vacationId from second_project_db.likedvacations where (userId = %s and vacationId = %s)"
        parameters = (check_userId, check_vacationId)
        vacation_Id = self.dal.get_scalar(sql, params=parameters)
        if vacation_Id is None: 
            return False
        return True
    
    def unlike_vacation(self, userId, vacationId):
        sql = "delete from second_project_db.likedvacations where (`userId` = %s and `vacationId` = %s)"
        parameters = (userId, vacationId)
        rows_affected = self.dal.delete(sql, params=parameters)
        return rows_affected
    

    def get_liked_vacations_amount(self):
        sql = "select vacationId, count(vacationId) as vacationLikeAmount from second_project_db.likedvacations where vacationId = any(select vacationId from second_project_db.likedvacations) group by vacationId"
        likes_dict = self.dal.get_table(sql)
        return likes_dict

    def get_user_and_their_liked_vacations(self, userId):
        # we are using data from our existing session and not from a user input so technically we don't need to divide with the params
        # but for consistency its kept with params like other functions that receive an input 
        sql = "select userId, vacationId from second_project_db.likedvacations where userId = %s"
        parameters = (userId, )
        users_and_their_liked_vacations = self.dal.get_table(sql, params=parameters)
        return users_and_their_liked_vacations