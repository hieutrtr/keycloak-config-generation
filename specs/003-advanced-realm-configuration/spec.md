# Feature Specification: Advanced Realm Configuration

**Feature Branch**: `003-advanced-realm-configuration`
**Status**: Draft

---

## User Scenarios & Testing

### Primary User Story
As a Keycloak administrator, I want to define a production-ready realm configuration, including detailed security policies, client scopes, and composite roles, in a single YAML file, so that I can fully automate and version control my entire Keycloak setup.

### Acceptance Scenarios
1.  **Given** a YAML file defining a realm role that is a composite of other realm and client roles, **When** the generator is run, **Then** the output JSON should contain the corresponding composite role definitions.
2.  **Given** a YAML file defining custom client scopes with protocol mappers, **When** the generator is run, **Then** the output JSON should contain the `clientScopes` and their associated protocol mappers.
3.  **Given** a YAML file that assigns a client to use a specific client scope, **When** the generator is run, **Then** the output JSON should reflect this assignment in the client's `defaultClientScopes` or `optionalClientScopes`.
4.  **Given** a YAML file specifying default flow bindings (e.g., `browserFlow`, `registrationFlow`), **When** the generator is run, **Then** the output JSON should set these top-level flow bindings correctly.
5.  **Given** a YAML file with brute force protection settings enabled, **When** the generator is run, **Then** the output JSON should include the `bruteForceProtected` configuration.
6.  **Given** a YAML file that enables and configures required actions like `UPDATE_PASSWORD`, **When** the generator is run, **Then** the output JSON should contain the `requiredActions` array with the correct settings.
7.  **Given** a YAML file with detailed token lifespan settings (e.g., `ssoSessionMaxLifespan`, `offlineSessionIdleTimeout`), **When** the generator is run, **Then** the output JSON should reflect all specified token settings.
8.  **Given** a YAML file with SMTP server settings, **When** the generator is run, **Then** the output JSON should contain the `smtpServer` configuration block.
9.  **Given** a YAML file with an identity provider configured with a mapper to link users by email, **When** the generator is run, **Then** the output JSON should contain the identity provider with the correct mapper configuration.

### Edge Cases
- How should the tool handle a composite role that references a role not defined in the YAML? (It should probably fail with a clear error).
- What happens if a default flow (e.g., `browserFlow`) is set to a flow alias that doesn't exist? (Fail with an error).

## Requirements

### Functional Requirements
- **FR-001**: The system MUST allow the definition of realm and client roles, including the ability to create **composite roles**.
- **FR-002**: The system MUST allow the definition of **Client Scopes**, including their protocol mappers.
- **FR-003**: The system MUST allow assigning default and optional client scopes to a client.
- **FR-004**: The system MUST support defining **Protocol Mappers** for clients and client scopes.
- **FR-005**: The system MUST allow setting the realm's default flow bindings (`browserFlow`, `registrationFlow`, `directGrantFlow`, etc.).
- **FR-006**: The system MUST allow configuration of **Brute Force Protection** settings.
- **FR-007**: The system MUST allow enabling and configuring **Required Actions** (e.g., `CONFIGURE_TOTP`).
- **FR-008**: The system MUST support the full range of **token lifespan settings** found in a standard Keycloak export.
- **FR-009**: The system MUST support the configuration of an **SMTP Server**.
- **FR-010**: The system MUST support the configuration of **Key Providers** and other items within the `components` object.
- **FR-011**: The system MUST support general realm attributes (`attributes` map).
- **FR-012**: The system MUST support browser security headers (`browserSecurityHeaders`).
- **FR-013**: The system MUST allow defining **Identity Provider Mappers** to link accounts (e.g., by email).

### Key Entities
- **Role**:
    - `name` (string)
    - `clientRole` (boolean)
    - `composite` (boolean)
    - `composites` (dictionary of realm/client roles)
- **ClientScope**:
    - `name` (string)
    - `protocol` (string)
    - `protocolMappers` (list of `ProtocolMapper`)
- **ProtocolMapper**:
    - `name` (string)
    - `protocol` (string)
    - `protocolMapper` (string, e.g., `oidc-usermodel-attribute-mapper`)
    - `config` (dictionary)
- **IdentityProviderMapper**:
    - `name` (string)
    - `identityProviderAlias` (string)
    - `identityProviderMapper` (string)
    - `config` (dictionary)
- **IdentityProvider (Extended)**:
    - `mappers` (list of `IdentityProviderMapper`)
- **Realm (Extended)**:
    - `roles` (dictionary for realm and client roles)
    - `clientScopes` (list of `ClientScope`)
    - `bruteForceProtected` (boolean)
    - `maxFailureWaitSeconds` (integer)
    - `requiredActions` (list of `RequiredAction`)
    - `ssoSessionMaxLifespan` (integer)
    - `offlineSessionIdleTimeout` (integer)
    - `browserFlow` (string)
    - `registrationFlow` (string)
    - `directGrantFlow` (string)
    - `clientAuthenticationFlow` (string)
    - `smtpServer` (dictionary)
    - `components` (dictionary)
    - `attributes` (dictionary)
    - `browserSecurityHeaders` (dictionary)
- **RequiredAction**:
    - `alias` (string)
    - `enabled` (boolean)
    - `defaultAction` (boolean)
