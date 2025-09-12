# Quickstart: Keycloak Config Generation CLI

This guide provides a quick way to get started with the Keycloak Config Generation CLI.

## Prerequisites

*   Python 3.8+
*   pip

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/keycloak-config-generation.git
    cd keycloak-config-generation
    ```

2.  **Install the package:**
    ```bash
    pip install .
    ```

## Usage

1.  **Create a YAML configuration file** (e.g., `my-realm.yaml`):
    ```yaml
    realm: my-new-realm
    enabled: true
    clients:
      - clientId: my-app
        secret: "super-secret"
        publicClient: false
        redirectUris:
          - "http://localhost:8080/*"
    users:
      - username: testuser
        enabled: true
        email: "test@example.com"
        firstName: "Test"
        lastName: "User"
        credentials:
          - type: "password"
            value: "password"
            temporary: false
        realmRoles:
          - "uma_authorization"
    ```

2.  **Run the CLI to generate the JSON file:**
    ```bash
    kc-generate --input my-realm.yaml --output my-realm.json
    ```

3.  **Verify the output:**
    A `my-realm.json` file should be created in the same directory, containing the Keycloak realm configuration in JSON format.

4.  **Import into Keycloak:**
    You can now import the generated `my-realm.json` file into your Keycloak instance through the Keycloak Admin Console.
