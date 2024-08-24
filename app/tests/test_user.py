import pytest
from app import createApp, db
from app.services.user_service import createUser, getUserByUsername

@pytest.fixture
def app():
    app = createApp('app.config.TestingConfig')
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def testCreateUser(client):
    username = "testuser"
    email = "test@test.com"
    password = "password"

    user = createUser(username, email, password)
    assert user.username == username
    assert user.email == email

def testGetUserByUsername(client):
    username = "testuser"
    email = "test@test.com"
    password = "password"

    createUser(username, email, password)
    user = getUserByUsername(username)
    assert user.username == username
    assert user.email == email