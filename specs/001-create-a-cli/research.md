# Research: Keycloak Config Generation CLI

## Keycloak JSON Schema

*   **Decision**: We will use the official Keycloak documentation and export a sample realm configuration to understand the required JSON structure.
*   **Rationale**: This ensures the generated JSON is compatible with Keycloak. Relying on the official source is the most reliable approach.
*   **Alternatives considered**: Trial and error, but this would be inefficient and error-prone.

## Python CLI Libraries

*   **Decision**: We will use the `click` library for building the command-line interface. For YAML parsing, `PyYAML` will be used.
*   **Rationale**: `click` is a popular, well-documented, and easy-to-use library for creating CLIs in Python. `PyYAML` is the de-facto standard for YAML manipulation in Python.
*   **Alternatives considered**: `argparse` (built-in but more verbose), `Typer` (built on `click`, but `click` is sufficient for this simple use case).

## YAML Structure Guidelines

*   **Decision**: The guideline will be a Markdown file (`YAML_GUIDE.md`) included in the repository.
*   **Rationale**: A Markdown file is easy to create, read, and maintain. It can be easily viewed on GitHub or converted to other formats if needed.
*   **Alternatives considered**: A hosted documentation website (overkill for this project), inline comments in the YAML (not as comprehensive).
