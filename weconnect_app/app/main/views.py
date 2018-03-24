from flask import render_template, url_for
from . import main


@main.route('/')
def index():
    context = {
        'register_user':
        str(url_for('api.register_new_user', _external=True)),
        'logout_user':
        str(url_for('api.logout_user', _external=True)),
        'reset_password':
        str(url_for('api.reset_password', _external=True)),
        'login':
        str(url_for('api.login', _external=True)),
        'register_business':
        str(url_for('api.register_business', _external=True)),
        'update_business':
        str(url_for('api.register_business', _external=True)) +
        '/<businessId>',
        'delete_business':
        str(url_for('api.register_business', _external=True)) +
        '/<businessId>',
        'retrieve_all_businesses':
        str(url_for('api.retrieve_all_businesses', _external=True)),
        'retrieve_a_business':
        str(url_for('api.retrieve_all_businesses', _external=True)) +
        '/<businessId>',
        'review_a_business':
        str(url_for('api.retrieve_all_businesses', _external=True)) +
        '/<businessId>/reviews'
    }
    return render_template('index.html', context=context)
