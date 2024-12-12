from flask import Flask, render_template
from models.role_model import RoleModel
from views.home_view import home_blueprint
from views.auth_view import auth_blueprint
from views.vacations_view import vacations_blueprint
from views.like_view import like_blueprint
from utils.app_config import AppConfig


app = Flask(__name__)

app.secret_key = AppConfig.session_secret_key
app.register_blueprint(home_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(vacations_blueprint)
app.register_blueprint(like_blueprint)


@app.errorhandler(404)
def page_not_found(error): # error sent here and not used because it's required as a function variable
    return render_template("404.html", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)

@app.errorhandler(Exception)
def catch_all(error): # error sent here and not used but it's required as a function variable
    return render_template("500.html", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)
