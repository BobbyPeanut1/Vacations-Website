from flask import request
from logic.vacation_logic import Vacation_Logic
from models.vacation_model import VacationModel
from models.client_error import ValidationError, ResourceNotFound

class VacationFacade:

    def __init__(self):
        self.logic = Vacation_Logic()

    def return_all_vacations_ordered_by_start_date(self):
        return self.logic.return_all_vacations_ordered_by_start_date()
    
    def return_all_countries(self):
        return self.logic.return_all_countries()
    
    def return_one_vacation(self, id):
        vacation = self.logic.get_one_vacation(id)
        if not vacation:
            raise ResourceNotFound("Vacation doesn't exist, please select an existing vacation", id)
        
        return vacation
    
    def add_vacation(self):
        country_id = request.form.get("country_name") # returns the value from the selected country in the <option> tag
        vacation_description = request.form.get("description")
        vacation_start_date = request.form.get("start_date")
        vacation_end_date = request.form.get("end_date")
        vacation_price = request.form.get("price")
        vacation_photo = request.files["image"]

        vacation = VacationModel(None, country_id, vacation_description, vacation_start_date, vacation_end_date, vacation_price, vacation_photo)
        do_we_have_validation_error = vacation.validate_insert()
        if do_we_have_validation_error:
            raise ValidationError(do_we_have_validation_error, vacation)
        
        self.logic.insert_vacation_to_db(vacation)


    def update_vacation(self):
        id = request.form.get("id")
        country_id = request.form.get("country_name") 
        vacation_description = request.form.get("description")
        vacation_start_date = request.form.get("start_date")
        vacation_end_date = request.form.get("end_date")
        vacation_price = request.form.get("price")
        vacation_photo = request.files["image"]

        vacation = VacationModel(id, country_id, vacation_description, vacation_start_date, vacation_end_date, vacation_price, vacation_photo)
        do_we_have_validation_error = vacation.validate_update()
        if do_we_have_validation_error:
            raise ValidationError(do_we_have_validation_error, vacation)
        
        self.logic.update_vacation(vacation)

    def delete_vacation(self, id):
        return self.logic.delete_vacation(id)

    def close(self):
        self.logic.dal.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close()


