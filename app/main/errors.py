from . import main
from flask import request, jsonify
from ..functions import test_input

@main.app_errorhandler(404)
def page_not_known(e):
    """Error handler for unknown routes"""
    return test_input('Page not found',404)


@main.app_errorhandler(500)
def internal_server_error(e):
    """Error handler for server errors"""
   return test_input('Internal Server Error',500)