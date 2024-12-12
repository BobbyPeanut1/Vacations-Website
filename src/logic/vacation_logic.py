from utils.dal import DAL
from models.vacation_model import VacationModel
from utils.image_handler import ImageHandler

class Vacation_Logic:
    def __init__(self):
        self.dal = DAL()
    
    def return_all_vacations_ordered_by_start_date(self):
        sql = "select * from second_project_db.vacations order by vacationStartDate"
        vacation_table = self.dal.get_table(sql)
        vacations_model_list = VacationModel.dictionaries_to_vacations(vacation_table)
        return vacations_model_list
    
    def return_all_countries(self):
        sql = "select * from second_project_db.countries"
        countries_dict = self.dal.get_table(sql)
        return countries_dict
    
    def get_one_vacation(self, id):
        sql = "select * from second_project_db.vacations where vacationId = %s"
        parameters = (id, )
        return self.dal.get_scalar(sql, params=parameters)
    
    def insert_vacation_to_db(self, vacation):
        image_name = ImageHandler.save_image(vacation.photoFileName, False) # sent with a false variable as to not override the placeholder image
        sql = "insert into second_project_db.vacations(countryId, vacationDescription, vacationStartDate, vacationEndDate, vacationPrice, photoFileName) values(%s, %s, %s, %s, %s, %s)"
        parameters = (vacation.countryId, vacation.vacationDescription, vacation.vacationStartDate, vacation.vacationEndDate, vacation.vacationPrice, image_name)
        added_vacation_id = self.dal.insert(sql, params=parameters)
        return added_vacation_id
    
    def update_vacation(self, vacation):
        old_image_name = self.get_old_image_name(vacation.vacationId)
        image_name = ImageHandler.update_image(old_image_name, vacation.photoFileName)
        sql = "update second_project_db.vacations set countryId = %s, vacationDescription = %s, vacationStartDate = %s, vacationEndDate = %s, vacationPrice = %s, photoFileName = %s where vacationId = %s"
        parameters = (vacation.countryId, vacation.vacationDescription, vacation.vacationStartDate, vacation.vacationEndDate, vacation.vacationPrice, image_name, vacation.vacationId)
        return self.dal.update(sql, params=parameters)
    
    def get_old_image_name(self, id):
        sql = "select photoFileName from second_project_db.vacations where vacationId=%s"
        parameters = (id, )
        result = self.dal.get_scalar(sql, params=parameters)
        return result["photoFileName"]

    def delete_vacation(self, id):
        image_name = self.get_old_image_name(id)
        ImageHandler.delete_image(image_name)
        sql = "delete from second_project_db.vacations where vacationId=%s"
        parameters = (id, )
        return self.dal.delete(sql, params=parameters)
    
    def close(self):
        self.dal.close()




