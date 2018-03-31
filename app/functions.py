from flask import jsonify, request
"""These are custom messages for handling json replies """


def make_json_reply(title, message):
    json_message = {title: message}
    return jsonify(json_message)

def app_error(message,code):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = make_json_reply('error',message)
        response.status_code = code 
        return response
    else:
        return message,code