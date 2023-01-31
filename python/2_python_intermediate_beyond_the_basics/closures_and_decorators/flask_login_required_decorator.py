'''
This is a very common pattern in flask., it ensures that a user is logged in/authenticated before they can access a specific route (/secret in this case)
@wraps is a decorator from functools whic preserves the metadata of the wrappted function.
So if somebody directs to /secret authentiaction decorator will be there.
'''
from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass