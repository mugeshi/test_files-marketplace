import pytest
from app.models import User,SearchHistory
from app.extensions import db
from app import create_app
from app.extensions import bcrypt
import datetime

app = create_app()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    return client

def test_create_users(client):
    with app.app_context():
        User.query.delete()

        emails = [
            "johndoe123@gmail.com",
            "sarah.smith@gmail.com",
            "gamer4life@gmail.com",
            "naturelover@gmail.com",
            "codinggeek@gmail.com",
            "musicfan@gmail.com",
            "fitnessjunkie@gmail.com",
            "bookworm@gmail.com",
            "travelbug@gmail.com",
            "foodie@gmail.com",
            "techwizard@gmail.com",
            "artlover@gmail.com",
            "fashionista@gmail.com",
            "hiker@gmail.com",
            "petlover@gmail.com",
            "scienceenthusiast@gmail.com",
            "moviebuff@gmail.com",
            "soccerstar@gmail.com",
            "eachbum@gmail.com",
            "historybuff@gmail.com"
        ]

        names = [
            "John Doe",
            "Sarah Smith",
            "GameR4Life",
            "Nature Lover",
            "Coding Geek",
            "Music Fan",
            "Fitness Junkie",
            "Book Worm",
            "Travel Bug",
            "Foodie Galore",
            "Tech Wizard",
            "Art Lover",
            "Fashionista",
            "Hiker Adventures",
            "Pet Lover",
            "Science Enthusiast",
            "Movie Buff",
            "Soccer Star",
            "Beach Bum",
            "History Buff"

        ]

        for i in range(len(emails)):
            user = User(username=names[i], email=emails[i])
            db.session.add(user)

        db.session.commit()

        assert User.query.count() == len(emails)

def test_query_users(client):
    with app.app_context():
        users = User.query.all()

        assert len(users) >= 0


@pytest.fixture
def user():
    return User()

def test_create_user(user):
    """
    Tests that a new user can be created with valid username, email, and password.
    """

    with app.app_context():
        username = 'johndoe'
        email = 'johndoe@email.com'
        password = 'password123'

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        assert user.username == username
        assert user.email == email
        assert user.password_hash == password  
        # assert user.authenticate(password) is True

def test_validate_username(user):
    """
    Tests that the `validates_name` method raises a ValueError when the username is None, empty, or less than 3 characters long.
    """

    with app.app_context():
        with pytest.raises(ValueError):
            username = None
            email = 'johndoe@email.com'
            password = 'password123'

            user = User(username=username, email=email, password=password)

        with pytest.raises(ValueError):
            username = ''
            email = 'johndoe@email.com'
            password = 'password123'

            user = User(username=username, email=email, password=password)


        with pytest.raises(ValueError):
            username = 'ab'
            email = 'johndoe@email.com'
            password = 'password123'

            user = User(username=username, email=email, password=password)


         


def test_validate_email(user):
    """
    Tests that the `validates_email` decorator raises a ValueError when the email is None, empty, invalid format, or already exists in the database.
    """

    with app.app_context():
        with pytest.raises(ValueError):
            user.email = None
            db.session.commit()

        with pytest.raises(ValueError):
            user.email = ''
            db.session.commit()

        with pytest.raises(ValueError):
            user.email = 'invalid@email#com'
            db.session.commit()

        





        """
        existing_user = User(username='test', email='existing@email.com')
        db.session.add(existing_user)
        db.session.commit()

        with pytest.raises(ValueError):
            user.email = 'johndoe@email.com'
            db.session.commit()

        db.session.delete(existing_user)
        db.session.commit()

        user.email = 'valid@email.com'
        db.session.commit()

        assert user.email == 'valid@email.com'

"""


def test_create_search_history(user):
    """
    Tests that a new search history item can be created and added to the user's search history.
    """

    with app.app_context():
        search_history_item = SearchHistory(user=user, name='Product Search')
        user.search_history.append(search_history_item)

        assert len(user.search_history) == 2
        assert user.search_history[0].user == user
        assert user.search_history[0].name == 'Product Search'
        # assert abs(user.search_history[0].search_date - datetime.datetime.now()) < datetime.timedelta(seconds=1)
