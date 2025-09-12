import yaml
import json
from keycloak_generator.generator import generate_json

def test_generate_json_from_yaml():
    """
    Tests that a YAML file is correctly converted to a Keycloak JSON structure.
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
    
    expected_json_str = json.dumps({
        "realm": "my-test-realm",
        "enabled": True,
        "clients": [
            {"clientId": "my-app", "secret": "secret"}
        ],
        "users": [
            {
                "username": "testuser",
                "credentials": [
                    {"type": "password", "value": "password"}
                ]
            }
        ]
    }, indent=2)

    generated_json = generate_json(yaml.safe_load(yaml_content))
    assert json.loads(generated_json) == json.loads(expected_json_str)
