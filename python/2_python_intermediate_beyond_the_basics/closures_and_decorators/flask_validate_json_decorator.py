'''
This decotator abstracts the validation of a student ID into a decorator, so similary the validation_json func is called when /grade is routed to before allowin the 
update_grade func to enter.

he decorator takes a variable length list as an argument so that we can pass in as 
many string arguments as necessary, each representing a key used to validate the JSON data. 
'''
from flask import Flask, request, abort
from functools import wraps

app = Flask(__name__)


def validate_json(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@app.route('/grade', methods=['POST'])
@validate_json('student_id')
def update_grade():
    json_data = request.get_json()
    print(json_data)
    # update database
    return "success!"