from src import create_app
from src.populate import populate_subscriptions

app = create_app()
populate_subscriptions(app)

if __name__ == '__main__':

    app.run()