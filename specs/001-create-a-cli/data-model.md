# Data Model: Keycloak Configuration

This document outlines the data structures for the Keycloak configuration, as represented in the input YAML and the output JSON.

## Keycloak Realm (Root Object)

*   **Description**: Represents a Keycloak realm. This is the top-level object in the configuration.
*   **Fields**:
    *   `realm`: (string, required) The name of the realm.
    *   `enabled`: (boolean, optional, default: `true`) Whether the realm is enabled.
    *   `clients`: (list of `Client`, optional) A list of clients within the realm.
    *   `roles`: (list of `Role`, optional) A list of realm-level roles.
    *   `users`: (list of `User`, optional) A list of users in the realm.

## Client

*   **Description**: Represents a client application within the realm.
*   **Fields**:
    *   `clientId`: (string, required) The client ID.
    *   `secret`: (string, required) The client secret.
    *   `enabled`: (boolean, optional, default: `true`) Whether the client is enabled.
    *   `publicClient`: (boolean, optional, default: `false`) Whether the client is public.
    *   `redirectUris`: (list of string, optional) A list of valid redirect URIs.

## Role

*   **Description**: Represents a role within the realm.
*   **Fields**:
    *   `name`: (string, required) The name of the role.
    *   `description`: (string, optional) A description of the role.

## User

*   **Description**: Represents a user within the realm.
*   **Fields**:
    *   `username`: (string, required) The username.
    *   `enabled`: (boolean, optional, default: `true`) Whether the user is enabled.
    *   `email`: (string, optional) The user's email address.
    *   `firstName`: (string, optional) The user's first name.
    *   `lastName`: (string, optional) The user's last name.
    *   `credentials`: (list of `Credential`, optional) The user's credentials.
    *   `realmRoles`: (list of string, optional) A list of realm-level roles assigned to the user.

## Credential

*   **Description**: Represents a user's credential (e.g., a password).
*   **Fields**:
    *   `type`: (string, required, e.g., "password") The type of credential.
    *   `value`: (string, required) The credential value.
    *   `temporary`: (boolean, optional, default: `false`) Whether the credential is temporary.
