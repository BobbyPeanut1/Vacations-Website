from flask import Blueprint, render_template
from models.role_model import RoleModel

home_blueprint = Blueprint("home_view", __name__)

@home_blueprint.route("/")
@home_blueprint.route("/home")
def home():
    return render_template("home.html", active = "home", admin_role = RoleModel.Admin.value, user_role = RoleModel.User.value)

