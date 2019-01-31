from . import home

@home.route('/')
def index():
    return '<h1 style="color: skyblue">this is HOME</h1>'