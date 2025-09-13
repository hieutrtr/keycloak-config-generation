# Data Model: Enhanced Realm Configuration

This document outlines the new data structures being added to the Keycloak configuration. These are extensions to the existing data model.

## Group

*   **Description**: Represents a user group within the realm.
*   **Fields**:
    *   `name`: (string, required) The name of the group.
    *   `realmRoles`: (list of string, optional) A list of realm-level roles assigned to the group.

## User Federation Provider

*   **Description**: Represents a user federation provider, such as LDAP.
*   **Fields**:
    *   `providerName`: (string, required, e.g., "ldap") The type of provider.
    *   `config`: (dictionary, required) The provider-specific configuration. This will vary depending on the provider.

## Identity Provider

*   **Description**: Represents an identity provider, such as Google or GitHub.
*   **Fields**:
    *   `alias`: (string, required) A unique alias for the provider.
    *   `providerId`: (string, required, e.g., "google") The ID of the provider.
    *   `enabled`: (boolean, optional, default: `true`) Whether the provider is enabled.
    *   `config`: (dictionary, required) The provider-specific configuration (e.g., client ID and secret).

## Authentication Flow

*   **Description**: Represents a custom authentication flow.
*   **Fields**:
    *   `alias`: (string, required) The name of the flow.
    *   `providerId`: (string, required, e.g., "basic-flow") The type of flow.
    *   `description`: (string, optional) A description of the flow.
    *   `authenticationExecutions`: (list of `AuthenticationExecution`, required) The steps in the flow.

## Authentication Execution

*   **Description**: Represents a single step within an authentication flow.
*   **Fields**:
    *   `authenticator`: (string, required) The authenticator to use (e.g., "auth-username-password-form").
    *   `requirement`: (string, required, e.g., "REQUIRED", "ALTERNATIVE", "DISABLED") The requirement level for this step.

## Realm Settings (Extended)

*   **Description**: Additional general realm settings.
*   **Fields**:
    *   `accessTokenLifespan`: (integer, optional) The lifespan of access tokens in seconds.
    *   `ssoSessionIdleTimeout`: (integer, optional) The idle timeout for SSO sessions in seconds.
