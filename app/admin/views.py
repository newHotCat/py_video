from . import admin

@admin.route('/')
def adminIndex():
    return '<h1 style="color: pink">this is ADMIN</admin>'