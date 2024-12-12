import datetime

class VacationModel:
    def __init__(self, vacationId, countryId, vacationDescription, vacationStartDate, vacationEndDate, vacationPrice, photoFileName):
        self.vacationId = vacationId
        self.countryId = countryId
        self.vacationDescription = vacationDescription
        self.vacationStartDate = vacationStartDate
        self.vacationEndDate = vacationEndDate
        self.vacationPrice = vacationPrice
        self.photoFileName = photoFileName
    
    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacationId = dictionary["vacationId"]
        countryId = dictionary["countryId"]
        vacationDescription = dictionary["vacationDescription"]
        vacationStartDate = dictionary["vacationStartDate"]
        vacationEndDate = dictionary["vacationEndDate"]
        vacationPrice = dictionary["vacationPrice"]
        photoFileName = dictionary["photoFileName"]
        vacation = VacationModel(vacationId, countryId, vacationDescription, vacationStartDate, vacationEndDate, vacationPrice, photoFileName)
        return vacation
    
    @staticmethod
    def dictionaries_to_vacations(list_of_dictionaries):
        vacations = []
        for item in list_of_dictionaries:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
    
    def validate_insert(self):
        if not self.countryId:
            return "missing country"
        if not self.vacationDescription:
            return "missing vacation description"
        if not self.vacationStartDate:
            return "missing start date"
        if not self.vacationEndDate:
            return "missing end date"
        if not self.vacationPrice:
            return "missing vacation price"
        if not self.photoFileName:
            return "missing photo"
        
        if int(self.vacationPrice)  < 0 or int(self.vacationPrice) > 10000:
            return "price must be between 0 and 10000 nis"
        
        # convert dates to a datetime object for date checking convenience
        # done after validating that the start date or end date are None to avoid receiving an unexpected error from the strptime function
        vacation_start_date_datetime = datetime.datetime.strptime(self.vacationStartDate, '%Y-%m-%d')
        vacation_end_date_datetime = datetime.datetime.strptime(self.vacationEndDate, '%Y-%m-%d')
        
        if vacation_end_date_datetime < vacation_start_date_datetime:
            return "vacation can't have an ending date before its starting date"
        
        if vacation_start_date_datetime.date() < datetime.date.today():
            return "Vacation can't be set before the current date"
        
        return None
    
    def validate_update(self):
        if not self.countryId:
            return "missing country"
        if not self.vacationDescription:
            return "missing vacation description"
        if not self.vacationStartDate:
            return "missing start date"
        if not self.vacationEndDate:
            return "missing end date"
        if not self.vacationPrice:
            return "missing vacation price"
        
        if int(self.vacationPrice)  < 0 or int(self.vacationPrice) > 10000:
            return "price must be between 0 and 10000 nis"
        
        # convert dates to a datetime object for date checking convenience
        # done after validating that the start date or end date are None to avoid receiving an unexpected error from the strptime function
        vacation_start_date_datetime = datetime.datetime.strptime(self.vacationStartDate, '%Y-%m-%d')
        vacation_end_date_datetime = datetime.datetime.strptime(self.vacationEndDate, '%Y-%m-%d')

        if vacation_end_date_datetime < vacation_start_date_datetime:
            return "vacation can't have an ending date before its starting date"
        
        return None

        
        
        




