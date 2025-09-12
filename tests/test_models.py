from keycloak_generator.models import Credential, User, Role, Client, Realm


def test_credential_creation():
    """
    Tests that a Credential object can be created with the correct attributes.
    """
    cred_data = {
        "type": "password",
        "value": "supersecret",
        "temporary": True,
    }
    credential = Credential(**cred_data)

    assert credential.type == cred_data["type"]
    assert credential.value == cred_data["value"]
    assert credential.temporary is True


def test_credential_creation_defaults():
    """
    Tests that a Credential object is created with the default temporary value.
    """
    cred_data = {
        "type": "password",
        "value": "supersecret",
    }
    credential = Credential(**cred_data)

    assert credential.type == cred_data["type"]
    assert credential.value == cred_data["value"]
    assert credential.temporary is False


def test_user_creation():
    """
    Tests that a User object can be created with the correct attributes.
    """
    user_data = {
        "username": "testuser",
        "enabled": True,
        "email": "test@example.com",
        "firstName": "Test",
        "lastName": "User",
        "credentials": [],
        "realmRoles": ["user"],
    }
    user = User(**user_data)
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.realm_roles == user_data["realmRoles"]


def test_role_creation():
    """
    Tests that a Role object can be created with the correct attributes.
    """
    role_data = {"name": "admin", "description": "Administrator role"}
    role = Role(**role_data)
    assert role.name == role_data["name"]
    assert role.description == role_data["description"]


def test_client_creation():
    """
    Tests that a Client object can be created with the correct attributes.
    """
    client_data = {
        "clientId": "my-client",
        "secret": "my-secret",
        "publicClient": False,
        "redirectUris": ["http://localhost/"],
    }
    client = Client(**client_data)
    assert client.client_id == client_data["clientId"]
    assert client.secret == client_data["secret"]


def test_realm_creation():
    """
    Tests that a Realm object can be created with the correct attributes.
    """
    realm_data = {
        "realm": "my-realm",
        "enabled": True,
        "clients": [],
        "roles": [],
        "users": [],
    }
    realm = Realm(**realm_data)
    assert realm.realm == realm_data["realm"]
    assert realm.enabled is True
