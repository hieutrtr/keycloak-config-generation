# Research: Enhance Realm Configuration

## Keycloak JSON Schema for New Entities

*   **Decision**: We will extend the existing schema knowledge by exporting realm configurations from Keycloak that specifically include Groups, User Federation (LDAP), Identity Providers (Google), Authentication Flows, and advanced realm settings (token lifespan).
*   **Rationale**: This continues the reliable approach from the first feature, ensuring the generated JSON for these new entities is fully compatible with Keycloak.
*   **Alternatives considered**: Manually crafting the JSON based on documentation alone, which is more error-prone.

## Python Data Modeling

*   **Decision**: We will continue to use Pydantic-style classes within our `models.py` to represent these new Keycloak entities.
*   **Rationale**: This maintains consistency with the existing codebase, provides data validation, and is a clean way to structure the data before serialization.
*   **Alternatives considered**: Using basic dictionaries, which would lack validation and a clear schema.

## YAML Structure for New Entities

*   **Decision**: The new configurations will be added as top-level keys in the input YAML file (e.g., `groups:`, `userFederationProviders:`). The structure will mirror the Keycloak API's JSON structure as closely as possible while remaining human-readable.
*   **Rationale**: A consistent and predictable structure makes the YAML easier for users to understand and for the tool to parse.
*   **Alternatives considered**: A deeply nested, complex structure, which would be harder to manage.
