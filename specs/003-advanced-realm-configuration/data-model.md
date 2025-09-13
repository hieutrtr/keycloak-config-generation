# Data Model: Advanced Realm Configuration

This document outlines the new data structures being added to support advanced Keycloak realm configurations.

## Role (Extended)

*   **Description**: Represents a realm or client-level role, now with support for composition.
*   **Fields**:
    *   `name`: (string, required) The name of the role.
    *   `description`: (string, optional) A description of the role.
    *   `clientRole`: (boolean, optional, default: `false`) Set to `true` if this is a client role. If so, the role name should be prefixed with the `clientId`.
    *   `composites`: (dictionary, optional) Defines which other roles are inherited by this role.
        *   `realm`: (list of string, optional) A list of realm-level role names.
        *   `client`: (dictionary, optional) A map where keys are `clientId`s and values are lists of client role names.

## Client Scope

*   **Description**: Represents a client scope, which is a shared set of mappers and roles.
*   **Fields**:
    *   `name`: (string, required) The name of the client scope.
    *   `protocol`: (string, optional, default: "openid-connect") The protocol for the scope.
    *   `protocolMappers`: (list of `ProtocolMapper`, optional) A list of protocol mappers attached to this scope.

## Protocol Mapper

*   **Description**: Defines how a piece of information is mapped into a token claim.
*   **Fields**:
    *   `name`: (string, required) The name of the mapper.
    *   `protocol`: (string, required, e.g., "openid-connect") The protocol for the mapper.
    *   `protocolMapper`: (string, required) The type of the mapper (e.g., "oidc-usermodel-attribute-mapper").
    *   `config`: (dictionary, required) The mapper-specific configuration.

## Identity Provider Mapper

*   **Description**: Configures how user information from an external IdP is mapped to a Keycloak user. Used for account linking.
*   **Fields**:
    *   `name`: (string, required) The name of the mapper.
    *   `identityProviderMapper`: (string, required) The type of the mapper (e.g., "oidc-user-attribute-idp-mapper").
    *   `config`: (dictionary, required) The mapper-specific configuration.

## Identity Provider (Extended from Feature 002)

*   **Description**: Represents an identity provider, now with support for mappers.
*   **Fields**:
    *   `alias`: (string, required) A unique alias for the provider.
    *   `providerId`: (string, required, e.g., "google") The ID of the provider.
    *   `enabled`: (boolean, optional, default: `true`) Whether the provider is enabled.
    *   `config`: (dictionary, required) The provider-specific configuration.
    *   `mappers`: (list of `IdentityProviderMapper`, optional) A list of mappers for this provider.

## Required Action

*   **Description**: Represents an action a user must take after authenticating.
*   **Fields**:
    *   `alias`: (string, required) The alias of the action (e.g., "UPDATE_PASSWORD").
    *   `enabled`: (boolean, optional, default: `true`) Whether the action is enabled.
    *   `defaultAction`: (boolean, optional, default: `false`) Whether it's a default action for new users.

## Realm (Root Object - Extended)

*   **Description**: The top-level realm object, extended with new advanced settings.
*   **Fields (New)**:
    *   `roles`: (list of `Role`, optional) A list of all realm and client roles to be defined.
    *   `clientScopes`: (list of `ClientScope`, optional) A list of client scopes to be defined.
    *   `requiredActions`: (list of `RequiredAction`, optional) A list of required actions.
    *   `browserFlow`: (string, optional) The alias of the flow to use for browser authentication.
    *   `registrationFlow`: (string, optional) The alias of the flow for user registration.
    *   `directGrantFlow`: (string, optional) The alias of the flow for direct grants.
    *   `resetCredentialsFlow`: (string, optional) The alias of the flow for resetting credentials.
    *   `clientAuthenticationFlow`: (string, optional) The alias of the flow for client authentication.
    *   `bruteForceProtected`: (boolean, optional, default: `false`) Whether brute force detection is enabled.
    *   `ssoSessionMaxLifespan`: (integer, optional) The maximum lifespan of an SSO session.
    *   `offlineSessionIdleTimeout`: (integer, optional) The idle timeout for offline sessions.
    *   `smtpServer`: (dictionary, optional) Configuration for the SMTP server.
    *   `components`: (dictionary, optional) For defining components like Key Providers.
    *   `attributes`: (dictionary, optional) A map of general realm attributes.
    *   `browserSecurityHeaders`: (dictionary, optional) A map of browser security headers.