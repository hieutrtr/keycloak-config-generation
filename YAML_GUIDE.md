# Keycloak Configuration YAML Guide

This guide explains the structure of the YAML file used to generate Keycloak realm configurations. The structure is based on the Keycloak REST API, but simplified for ease of use.

## Root Object: Realm

The top-level object in the YAML file represents a single Keycloak Realm.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `realm` | String | Yes | | The name of the realm. |
| `enabled` | Boolean | No | `true` | Whether the realm is enabled. |
| `clients` | List of [Client](#client) | No | `[]` | A list of clients to create in the realm. |
| `roles` | List of [Role](#role) | No | `[]` | A list of realm-level roles to create. |
| `users` | List of [User](#user) | No | `[]` | A list of users to create in the realm. |
| `groups` | List of [Group](#group) | No | `[]` | A list of groups to create in the realm. |
| `userFederationProviders` | List of [UserFederationProvider](#userfederationprovider) | No | `[]` | A list of user federation providers (e.g., LDAP). |
| `identityProviders` | List of [IdentityProvider](#identityprovider) | No | `[]` | A list of identity providers (e.g., Google, GitHub). |
| `authenticationFlows` | List of [AuthenticationFlow](#authenticationflow) | No | `[]` | A list of custom authentication flows. |
| `accessTokenLifespan` | Integer | No | `null` | The lifespan of access tokens in seconds. |
| `ssoSessionIdleTimeout` | Integer | No | `null` | The idle timeout for SSO sessions in seconds. |

---

### Client

A client represents an application that will be secured by Keycloak.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `clientId` | String | Yes | | The unique ID of the client. |
| `secret` | String | Yes | | The client secret. |
| `publicClient` | Boolean | No | `false` | Set to `true` if the client is a public client (e.g., a single-page application). |
| `redirectUris` | List of String | No | `[]` | A list of valid redirect URIs for the client. |

---

### Role

A role is a named set of permissions.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | String | Yes | | The name of the role. |
| `description` | String | No | `null` | A description of the role. |

---

### User

A user represents a person who can log in to the realm.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `username` | String | Yes | | The user's username. |
| `enabled` | Boolean | No | `true` | Whether the user account is enabled. |
| `email` | String | No | `null` | The user's email address. |
| `firstName` | String | No | `null` | The user's first name. |
| `lastName` | String | No | `null` | The user's last name. |
| `credentials` | List of [Credential](#credential) | No | `[]` | The user's credentials (e.g., password). |
| `realmRoles` | List of String | No | `[]` | A list of realm-level roles to assign to the user. |

---

### Credential

A credential represents a user's secret, like a password.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `type` | String | Yes | | The type of credential. Should be `"password"`. |
| `value` | String | Yes | | The password value. |
| `temporary` | Boolean | No | `false` | Whether the user must change the password on first login. |

---

### Group

A group is a collection of users. Roles can be assigned to groups.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `name` | String | Yes | | The name of the group. |
| `realmRoles` | List of String | No | `[]` | A list of realm-level roles to assign to the group. |

---

### UserFederationProvider

Connects to an external user database like LDAP or Active Directory.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `providerName` | String | Yes | | The type of provider (e.g., "ldap"). |
| `config` | Dictionary | Yes | | Provider-specific configuration key-value pairs. |

---

### IdentityProvider

Integrates with an external identity provider like Google or GitHub for social login.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `alias` | String | Yes | | A unique alias for the provider. |
| `providerId` | String | Yes | | The ID of the provider (e.g., "google"). |
| `enabled` | Boolean | No | `true` | Whether the provider is enabled. |
| `config` | Dictionary | Yes | | Provider-specific configuration (e.g., client ID and secret). |

---

### AuthenticationFlow

Defines a custom sequence of steps for user authentication.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `alias` | String | Yes | | The name of the flow. |
| `providerId` | String | Yes | | The type of flow (e.g., "basic-flow"). |
| `description` | String | No | `null` | A description of the flow. |
| `authenticationExecutions` | List of [AuthenticationExecution](#authenticationexecution) | No | `[]` | The steps in the flow. |

---

### AuthenticationExecution

Represents a single step within an authentication flow.

| Field | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `authenticator` | String | Yes | | The authenticator to use (e.g., "auth-username-password-form"). |
| `requirement` | String | Yes | | The requirement level ("REQUIRED", "ALTERNATIVE", "DISABLED"). |

---

## Full Example

```yaml
realm: my-cool-realm
enabled: true
accessTokenLifespan: 600
ssoSessionIdleTimeout: 3600

clients:
  - clientId: my-web-app
    secret: "a-very-secret-string"
    publicClient: false
    redirectUris:
      - "https://myapp.com/callback"
      - "http://localhost:3000/callback"
roles:
  - name: "admin"
    description: "Administrator with full permissions"
  - name: "viewer"
    description: "Can view data"
users:
  - username: "alice"
    enabled: true
    email: "alice@example.com"
    firstName: "Alice"
    lastName: "Smith"
    credentials:
      - type: "password"
        value: "password123"
        temporary: true
    realmRoles:
      - "admin"
      - "viewer"
  - username: "bob"
    enabled: true
    email: "bob@example.com"
    firstName: "Bob"
    lastName: "Johnson"
    credentials:
      - type: "password"
        value: "another-password"
    realmRoles:
      - "viewer"

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

authenticationFlows:
  - alias: "Browser with OTP"
    providerId: "basic-flow"
    description: "Adds an OTP step to the standard browser flow."
    authenticationExecutions:
      - authenticator: "auth-username-password-form"
        requirement: "REQUIRED"
      - authenticator: "conditional-otp-form"
        requirement: "REQUIRED"
```
