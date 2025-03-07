from .models import db, Subscription

def populate_subscriptions(app):
    # Insert default subscription types if they don't exist
    default_subscriptions = ['standard', 'premium', 'premium+']

    with app.app_context():
        for sub in default_subscriptions:
            existing = Subscription.query.filter_by(name=sub).first()
            if not existing:
                db.session.add(Subscription(name=sub))

        db.session.commit()

