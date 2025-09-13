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

    expected_data = {
        "realm": "my-test-realm",
        "enabled": True,
        "clients": [
            {
                "clientId": "my-app",
                "secret": "secret",
                "publicClient": False,
                "redirectUris": [],
                "defaultClientScopes": [],
                "optionalClientScopes": [],
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
        "clientScopes": [],
        "requiredActions": [],
        "smtpServer": {},
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


def test_advanced_realm_generation():
    """
    Tests that a YAML file with advanced configurations is correctly converted.
    """
    yaml_content = """
    realm: production-realm
    bruteForceProtected: true
    ssoSessionMaxLifespan: 36000
    roles:
      - name: composite-auditor
        composites:
          realm: ["realm-admin"]
    clientScopes:
      - name: "custom-claims-scope"
        protocolMappers:
          - name: "Custom Claim Mapper"
            protocol: "openid-connect"
            protocolMapper: "oidc-usermodel-attribute-mapper"
            config: { "claim.name": "custom_claim" }
    requiredActions:
      - alias: "UPDATE_PASSWORD"
    identityProviders:
      - alias: "google"
        providerId: "google"
        config: {}
        mappers:
          - name: "google-email-mapper"
            identityProviderMapper: "oidc-user-attribute-idp-mapper"
            config: { "syncMode": "FORCE" }
    smtpServer:
      host: "smtp.example.com"
    """
    data = yaml.safe_load(yaml_content)
    generated_json_str = generate_json(data)
    generated_data = json.loads(generated_json_str)

    assert generated_data["bruteForceProtected"] is True
    assert generated_data["ssoSessionMaxLifespan"] == 36000
    assert generated_data["roles"][0]["name"] == "composite-auditor"
    assert generated_data["roles"][0]["composites"]["realm"] == ["realm-admin"]
    assert generated_data["clientScopes"][0]["name"] == "custom-claims-scope"
    assert generated_data["clientScopes"][0]["protocolMappers"][0]["name"] == "Custom Claim Mapper"
    assert generated_data["requiredActions"][0]["alias"] == "UPDATE_PASSWORD"
    assert generated_data["identityProviders"][0]["mappers"][0]["name"] == "google-email-mapper"
    assert generated_data["smtpServer"]["host"] == "smtp.example.com"
