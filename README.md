# Keycloak Config Generator

A simple command-line tool to generate Keycloak realm configurations from human-readable YAML files.

This tool allows you to define your Keycloak realms, clients, roles, and users in a YAML file, which is easier to manage and version control than Keycloak's native JSON format. You can then use this tool to convert the YAML file into a JSON file that can be imported directly into Keycloak.

## Features

-   Define Keycloak realms, clients, roles, and users in YAML.
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
    See the [YAML_GUIDE.md](YAML_GUIDE.md) for a detailed explanation of the format and a full example. Here is a basic example:

    ```yaml
    # my-realm.yaml
    realm: my-new-realm
    enabled: true
    clients:
      - clientId: my-app
        secret: "super-secret"
    users:
      - username: testuser
        credentials:
          - type: "password"
            value: "password"
    ```

2.  **Run the CLI to generate the JSON file.**
    The CLI is available via `poetry run`.

    ```bash
    poetry run kc-generate --input my-realm.yaml --output my-realm.json
    ```

3.  **Import the generated JSON into Keycloak.**
    In the Keycloak Admin Console, go to "Realm Settings" -> "Action" -> "Import" and select the generated `my-realm.json` file.

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
