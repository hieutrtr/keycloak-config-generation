# Research: Advanced Realm Configuration

## Keycloak JSON Schema for Advanced Entities

*   **Decision**: To ensure complete accuracy, we will manually configure a Keycloak realm with all the specified advanced features: composite roles, client scopes with protocol mappers, brute force protection, detailed token settings, required actions, and an SMTP server. We will then export the realm's JSON representation.
*   **Rationale**: This is the most reliable method to capture the exact JSON structure, nesting, and property names that Keycloak expects for these complex configurations. It eliminates guesswork and ensures 100% compatibility.
*   **Alternatives considered**: Relying solely on Keycloak's API documentation. This was rejected because the documentation can sometimes be less precise than a real-world export, especially concerning the structure of nested objects and component configurations.

## Python Data Modeling Strategy

*   **Decision**: We will continue to extend the existing Pydantic-style classes in `src/keycloak_generator/models.py`. New classes will be created for `Role`, `ClientScope`, `ProtocolMapper`, and `RequiredAction`. The main `Realm` model will be significantly expanded to include all the new top-level settings.
*   **Rationale**: This maintains consistency with the existing codebase, leverages the validation capabilities of the current data model, and provides a clear, object-oriented structure for the new configuration options.

## YAML Structure for Advanced Entities

*   **Decision**: The new configurations will be added as top-level keys in the input YAML, mirroring the structure of the Keycloak JSON export as closely as possible. For example: `roles:`, `clientScopes:`, `bruteForceProtected:`, `smtpServer:`. The structure for defining composite roles will be explicitly designed for clarity.
*   **Rationale**: A structure that closely follows the Keycloak API makes the tool predictable for users already familiar with Keycloak. It also simplifies the mapping logic in the generator.
