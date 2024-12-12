from flask import Blueprint, render_template, redirect, url_for, request
from models.client_error import ValidationError, AuthError
from models.role_model import RoleModel
from facades.user_facade import UserFacade

auth_blueprint = Blueprint("auth_view", __name__)

@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET":
            error = request.args.get('error')
            return render_template("register.html", error = error , user={}, active = "register", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)
        
        with UserFacade() as auth_facade:
            auth_facade.user_sign_up()

        return redirect(url_for("auth_view.login"))
    
    except ValidationError as err:
        return render_template("register.html", error = err.message, user = err.model, active = "register", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value) 

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            error = request.args.get('error')
            return render_template("login.html",error = error, credentials = {}, active = "login", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)
        
        with UserFacade() as auth_facade:
            auth_facade.user_log_in()

        return redirect(url_for("home_view.home"))
    
    except (ValidationError, AuthError) as err: 
        return render_template("login.html", error = err.message, credentials = err.model, active = "login", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)
    
@auth_blueprint.route("/logout")
def logout():

    with UserFacade() as auth_facade:
        auth_facade.user_log_out()

    return redirect(url_for("home_view.home"))

