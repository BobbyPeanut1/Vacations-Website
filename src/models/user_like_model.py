

class UserLikeModel:


    @staticmethod
    def dictionaries_to_user_dictionary(list_of_dictionaries):
        user_id_and_vacation_likes = {}
        for dictionary in list_of_dictionaries:
            user_id, vacation_id = dictionary.values()
            if user_id not in user_id_and_vacation_likes:
                user_id_and_vacation_likes[user_id] = [vacation_id]
            else:
                user_id_and_vacation_likes[user_id].append(vacation_id)

        return user_id_and_vacation_likes