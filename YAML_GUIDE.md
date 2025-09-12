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

## Full Example

```yaml
realm: my-cool-realm
enabled: true
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
```
