# Keycloak Config Generator

A simple command-line tool to generate Keycloak realm configurations from human-readable YAML files.

This tool allows you to define your Keycloak realms, clients, roles, and users in a YAML file, which is easier to manage and version control than Keycloak's native JSON format. You can then use this tool to convert the YAML file into a JSON file that can be imported directly into Keycloak.

## Features

-   Define Keycloak realms, clients, roles, users, and groups in YAML.
-   Configure advanced features like User Federation, Identity Providers, and custom Authentication Flows.
-   Manage realm-level settings like token lifespans.
-   Generate Keycloak-compatible JSON configuration files.
-   Command-line interface for easy integration into scripts and workflows.
-   Schema validation to help you catch errors in your configuration.

## Installation

1.  **Prerequisites**: Python 3.9+

2.  **Clone and Install**:
    ```bash
    git clone https://github.com/your-username/keycloak-config-generation.git
    cd keycloak-config-generation
    pip install poetry
    poetry install
    ```

## Usage

1.  **Create a YAML configuration file.**
    See the [YAML_GUIDE.md](YAML_GUIDE.md) for a detailed explanation of all available options. Here is an example showcasing some of the features:

    ```yaml
    # my-realm.yaml
    realm: my-cool-realm
    enabled: true
    accessTokenLifespan: 600

    clients:
      - clientId: my-web-app
        secret: "a-very-secret-string"

    users:
      - username: "alice"
        firstName: "Alice"
        credentials:
          - type: "password"
            value: "password123"
        realmRoles:
          - "admin"

    groups:
      - name: "developers"
        realmRoles:
          - "viewer"

    identityProviders:
      - alias: "github"
        providerId: "github"
        enabled: true
        config:
          clientId: "your-github-client-id"
          clientSecret: "your-github-client-secret"
    ```

2.  **Run the CLI to generate the JSON file.**
    The CLI is available via `poetry run`.

    ```bash
    poetry run kc-generate --input my-realm.yaml --output my-realm.json
    ```

3.  **Import the generated JSON into Keycloak.**
    In the Keycloak Admin Console, you can create a new realm and select the generated `my-realm.json` file to import the configuration.

## Development

This project uses Poetry for dependency management and `pytest` for testing.

-   **Run tests**:
    ```bash
    poetry run pytest
    ```
-   **Run linter**:
    ```bash
    poetry run ruff check .
    ```
