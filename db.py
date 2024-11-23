from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_db(app):
    with app.app_context():
        # Import models here to avoid circular imports
        from models.dog import Dog
        from models.daycare import Daycare
        from models.caretaker import Caretaker
        from models.user import User

        db.drop_all()
        db.create_all()

        # Create initial data
        daycare = Daycare(
            name="La favorita",
            address="123 Pet Street"
        )
        db.session.add(daycare)
        db.session.commit()

        # Create initial caretakers
        caretakers = [
            Caretaker(
                name="John Smith",
                phone="555-0123",
                id_daycare=daycare.id
            ),
            Caretaker(
                name="Jane Doe",
                phone="555-4567",
                id_daycare=daycare.id
            ),
            Caretaker(
                name="Mario",
                phone="555-8910",
                id_daycare=daycare.id
            )
        ]
        db.session.add_all(caretakers)
        db.session.commit()

        # Create initial dogs
        dogs = [
            Dog(
                name="Max",
                breed="Labrador",
                age=3,
                weight=30,
                id_daycare=daycare.id,
                id_caretaker=caretakers[0].id
            ),
            Dog(
                name="Luna",
                breed="Golden Retriever",
                age=2,
                weight=25,
                id_daycare=daycare.id,
                id_caretaker=caretakers[1].id
            ),
            Dog(
                name="Rocky",
                breed="German Shepherd",
                age=0,
                weight=3,
                id_daycare=daycare.id,
                id_caretaker=caretakers[1].id
            ),
            Dog(
                name="Lassie",
                breed="Poodle",
                age=1,
                weight=2,
                id_daycare=daycare.id,
                id_caretaker=caretakers[0].id
            ),
            Dog(
                name="Lassie",
                breed="German Shepherd",
                age=1,
                weight=12,
                id_daycare=daycare.id,
                id_caretaker=caretakers[1].id
            )
        ]
        db.session.add_all(dogs)
        db.session.commit()

        users = [
            User(username="admin", password="admin", is_admin=True),
            User(username="mario", password="mario"),
            User(username="juan", password="juan"),
            User(username="pedro", password="pedro")
        ]
        db.session.add_all(users)
        db.session.commit()
