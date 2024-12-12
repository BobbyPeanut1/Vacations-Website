from flask import Blueprint, render_template, redirect, url_for, send_file, request, session
import json
from facades.vacation_facade import VacationFacade
from facades.user_facade import UserFacade
from facades.like_facade import LikeFacade
from models.client_error import ValidationError, AuthError, ResourceNotFound
from models.role_model import RoleModel
from utils.image_handler import ImageHandler

vacations_blueprint = Blueprint("vacations_view", __name__)

@vacations_blueprint.route("/vacations")
def vacations_list():
    try: 
        with UserFacade() as auth_facade:
            auth_facade.block_anonymous()

        error = request.args.get('error')

        with VacationFacade() as vacation_facade, LikeFacade() as like_facade:
            vacations = vacation_facade.return_all_vacations_ordered_by_start_date()
            countries = vacation_facade.return_all_countries()
            liked_vacation_amount = like_facade.get_liked_vacations_amount()
            users_and_their_liked_vacations = like_facade.get_users_and_their_liked_vacations(session["current_user"]['userId'])

        return render_template("vacations.html", active = "vacations", error = error, vacations = vacations, countries_dicts = countries, vacationLikeCount = liked_vacation_amount, usersLikedVacations = json.dumps(users_and_their_liked_vacations), admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)

    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))

@vacations_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)

@vacations_blueprint.route("/vacations/new", methods = ["GET", "POST"])
def add_vacation():
    try:
        with UserFacade() as auth_facade:
            auth_facade.block_non_admin()

        if request.method == "GET":
            error = request.args.get('error')
            with VacationFacade() as vacation_facade:
                countries = vacation_facade.return_all_countries()
            
            return render_template("insert_vacation.html", error = error, active = "insert", countries_dicts = countries, admin_role = RoleModel.Admin.value)
        
        with VacationFacade() as vacation_facade:
            vacation_facade.add_vacation()
        
        return redirect(url_for("vacations_view.vacations_list"))
    
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    except ValidationError as err:
        return redirect(url_for("vacations_view.add_vacation", error = err.message))
        
@vacations_blueprint.route("/vacations/edit/<int:id>", methods = ["GET", "POST"])
def edit_vacation(id):
    try:
        with UserFacade() as auth_facade:
            auth_facade.block_non_admin()
        
        if request.method == "GET":
            error = request.args.get('error')
            with VacationFacade() as vacation_facade:
                requested_vacation = vacation_facade.return_one_vacation(id)
                countries = vacation_facade.return_all_countries()

            return render_template("edit_vacation.html", error = error , vacation = requested_vacation, countries_dicts = countries, admin_role = RoleModel.Admin.value)

        with VacationFacade() as vacation_facade:
            vacation_facade.update_vacation()
        
        return redirect(url_for("vacations_view.vacations_list"))
    
    except (AuthError, ResourceNotFound) as err:
        return redirect(url_for("vacations_view.vacations_list", error = err.message))
    except ValidationError as err:
        return redirect(url_for("vacations_view.edit_vacation", id = id, error = err.message))
    

@vacations_blueprint.route("/vacations/delete/<int:id>")
def delete_vacation(id):
    try:
        with UserFacade() as auth_facade:
            auth_facade.block_non_admin()
        
        with VacationFacade() as vacation_facade:
            vacation_facade.delete_vacation(id)
        return redirect(url_for("vacations_view.vacations_list"))
    
    except AuthError as err:
        return redirect(url_for("vacations_view.vacations_list", error = err.message))

    