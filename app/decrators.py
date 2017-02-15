from functools import wraps
from flask_login import current_user
from flask import abort
from .models import Permission

def permission_required(permission):
    def decrator(f):
        @wraps(f)
        def decrated_function(*args,**kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decrated_function
    return decrator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


