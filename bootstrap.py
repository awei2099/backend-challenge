import os
import json
from app import app, db, DB_FILE
from models import User, Club


def create_user():
    # check if the user already exists
    if User.query.filter_by(username='josh').first():
        print("User 'josh' already exists.")
        return

    # create new user
    user = User(username='josh', email='josh@gmail.com', password='password')
    db.session.add(user)
    db.session.commit()

    # debug code
    print("User 'josh' created")

def load_data():
    # open json file
    with open('clubs.json', 'r') as file:
        clubs_data = json.load(file)
    
    # extract data from json
    for club_data in clubs_data:
        club = Club(
            code=club_data['code'],
            name=club_data['name'],
            description=club_data['description'],
            tags=club_data['tags']
        )
        db.session.add(club)
    
    db.session.commit()

    # debug code
    print("Club data loaded")


# No need to modify the below code.
if __name__ == "__main__":
    # Delete any existing database before bootstrapping a new one.
    LOCAL_DB_FILE = "instance/" + DB_FILE
    if os.path.exists(LOCAL_DB_FILE):
        os.remove(LOCAL_DB_FILE)

    with app.app_context():
        db.create_all()
        create_user()
        load_data()
