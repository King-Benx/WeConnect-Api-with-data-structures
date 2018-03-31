from . import main
from flask import request, jsonify
from ..functions import app_error


@main.app_errorhandler(404)
def page_not_known(e):
    """Error handler for unknown routes"""
    return app_error('Page not found', 404)


@main.app_errorhandler(500)
def internal_server_error(e):
    """Error handler for server errors"""
    return app_error('Internal Server Error', 500)
