
class VacationLikeModel:


    @staticmethod
    def dictionary_to_list(dictionary):
        vacationId = dictionary["vacationId"]
        vacationLikeAmount = dictionary["vacationLikeAmount"]
        id_and_likes = [vacationId, vacationLikeAmount]
        return id_and_likes
    
    @staticmethod
    def dictionaries_to_list_of_lists(list_of_dictionaries):
        ids_and_likes = []
        for item in list_of_dictionaries:
            data_list = VacationLikeModel.dictionary_to_list(item)
            ids_and_likes.append(data_list)
        return ids_and_likes