import yaml
import json
from keycloak_generator.generator import generate_json

def test_generate_json_from_yaml():
    """
    Tests that a basic YAML file is correctly converted to a Keycloak JSON structure.
    """
    yaml_content = """
    realm: my-test-realm
    enabled: true
    clients:
      - clientId: my-app
        secret: "secret"
    users:
      - username: testuser
        credentials:
          - type: "password"
            value: "password"
    """

    # The expected JSON now includes the new empty lists from the Realm model
    expected_data = {
        "realm": "my-test-realm",
        "enabled": True,
        "clients": [
            {
                "clientId": "my-app",
                "secret": "secret",
                "publicClient": False,
                "redirectUris": [],
            }
        ],
        "roles": [],
        "users": [
            {
                "username": "testuser",
                "enabled": True,
                "credentials": [
                    {
                        "type": "password",
                        "value": "password",
                        "temporary": False,
                    }
                ],
                "realmRoles": [],
            }
        ],
        "groups": [],
        "userFederationProviders": [],
        "identityProviders": [],
        "authenticationFlows": [],
    }

    generated_json = generate_json(yaml.safe_load(yaml_content))
    assert json.loads(generated_json) == expected_data


def test_generate_json_with_enhanced_config():
    """
    Tests that a YAML file with the new enhanced configurations is correctly converted.
    """
    yaml_content = """
    realm: my-enhanced-realm
    accessTokenLifespan: 300
    groups:
      - name: "admins"
    userFederationProviders:
      - providerName: "ldap"
        config:
          "bindDn": "cn=admin,dc=example,dc=org"
    identityProviders:
      - alias: "google"
        providerId: "google"
        config:
          "clientId": "test-id"
    authenticationFlows:
      - alias: "My Custom Flow"
        providerId: "basic-flow"
        authenticationExecutions:
          - authenticator: "auth-username-password-form"
            requirement: "REQUIRED"
    """
    
    data = yaml.safe_load(yaml_content)
    generated_json_str = generate_json(data)
    generated_data = json.loads(generated_json_str)

    assert generated_data["realm"] == "my-enhanced-realm"
    assert generated_data["accessTokenLifespan"] == 300
    assert generated_data["groups"][0]["name"] == "admins"
    assert generated_data["userFederationProviders"][0]["providerName"] == "ldap"
    assert generated_data["identityProviders"][0]["alias"] == "google"
    assert generated_data["authenticationFlows"][0]["alias"] == "My Custom Flow"
