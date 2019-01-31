from app import createApp

app = createApp()

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
