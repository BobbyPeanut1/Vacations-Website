from flask import request, session
from models.vacation_like_model import VacationLikeModel
from models.user_like_model import UserLikeModel
from models.client_error import ValidationError
from logic.like_logic import Like_Logic

class LikeFacade:

    def __init__(self):
        self.logic = Like_Logic()

    def like_vacation(self):
        vacation_id = request.form.get("vacation_id")
        user_id = session.get("current_user")["userId"]

        if self.logic.did_user_like_vacation_already(user_id, vacation_id):
            raise ValidationError("User already liked vacation", None)

        self.logic.like_vacation(user_id, vacation_id)

    def unlike_vacation(self):
        vacation_id = request.form.get("vacation_id")
        user_id = session.get("current_user")["userId"]

        if not self.logic.did_user_like_vacation_already(user_id, vacation_id):
            raise ValidationError("The vacation you are trying to unlike does'nt exist", None)

        self.logic.unlike_vacation(user_id, vacation_id)

    def get_liked_vacations_amount(self):
        vacationLikes = self.logic.get_liked_vacations_amount()
        vacations_ids_and_likes = VacationLikeModel.dictionaries_to_list_of_lists(vacationLikes)

        return vacations_ids_and_likes


    def get_users_and_their_liked_vacations(self, userId):
        sql_data = self.logic.get_user_and_their_liked_vacations(userId)
        users_and_their_liked_vacations = UserLikeModel.dictionaries_to_user_dictionary(sql_data)

        return users_and_their_liked_vacations

    def close(self):
        self.logic.dal.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()

