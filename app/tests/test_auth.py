import pytest

from app import createApp, db


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

def testRegister(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'email': 'test@test.com',
        'password': 'password'
    })
    assert response.status_code == 201
    assert response.get_json()['username'] == 'testuser'

def testLogin(client):
    client.post('/register', json={
        'username': 'testuser',
        'email': 'test@test.com',
        'password': 'password'
    })
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'password'
    })
    assert response.status_code == 200
    assert 'accessToken' in response.get_json()