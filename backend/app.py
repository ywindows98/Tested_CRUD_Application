from src import create_app
from src.populate import populate_subscriptions, populate_users

app = create_app()
populate_subscriptions(app)
populate_users(app)

if __name__ == '__main__':

    app.run()
