import functools
from flask import session, redirect

def require_superadmin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get('has_superadmin'):
            return redirect('/superadmin/login')

        func(*args, **kwargs)
    return wrapper