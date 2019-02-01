from . import home
from datetime import datetime as dt


@home.route('/')
def index():
    print(dt.now())
    return '<h1 style="color: skyblue">this is HOME %s UTC %s</h1> ' % (dt.now(), dt.utcnow())