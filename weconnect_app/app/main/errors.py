from . import main
from flask import request, redirect, url_for
from flask import jsonify


def error_handler(error, message):
    if request.accept_mimtypes.accept_json and not request.accept_mimtypes.accept_html:
        response = jsonify(message)
        response.status_code = error
        return response


@main.app_errorhandler('404')
def page_not_known(e):
    # handle errors in a json format for unknown urls
    return error_handler(404, {'error': 'page not found'})


@main.app_errorhandler('500')
def internal_server_error(e):
    # incase an internal server error occurs due to some bug in the code
    return error_handler(500, {'error': 'internal server error'})
