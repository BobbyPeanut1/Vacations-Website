from flask import Blueprint, redirect, url_for
from facades.user_facade import UserFacade
from facades.like_facade import LikeFacade
from models.client_error import ValidationError, AuthError

like_blueprint = Blueprint("like_view", __name__)

@like_blueprint.route("/vacations/like", methods = ['POST'])
def like_vacation():
    try:
        with UserFacade() as auth_facade:
            auth_facade.block_anonymous()

        with LikeFacade() as like_facade:
            like_facade.like_vacation()
        
        return redirect(url_for("vacations_view.vacations_list"))

    except ValidationError as err:
        return redirect(url_for("vacations_view.vacations_list", error = err.message))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))


@like_blueprint.route("/vacations/unlike", methods = ['POST'])
def unlike_vacation():
    try:
        with UserFacade() as auth_facade:
            auth_facade.block_anonymous()

        with LikeFacade() as like_facade:
            like_facade.unlike_vacation()
            
        return redirect(url_for("vacations_view.vacations_list"))
    
    except ValidationError as err:
        return redirect(url_for("vacations_view.vacations_list", error = err.message))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))
    
