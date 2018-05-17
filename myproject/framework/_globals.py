app = None # FlaskAlpha对象

def get_globals_object(*args):
    arr = []
    for name in args:
        arr.append(getattr(app, name))
    return arr[0] if len(arr) == 1 else arr


def set_globals_object(name, value):
    setattr(app, name, value)
