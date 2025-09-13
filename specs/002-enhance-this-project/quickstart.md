# Quickstart: Enhanced Realm Configuration

This guide demonstrates how to use the newly added realm configuration features.

## Prerequisites

*   The Keycloak Config Generation CLI must be installed.

## Usage

1.  **Create a YAML configuration file** (e.g., `enhanced-realm.yaml`) with the new sections:
    ```yaml
    realm: my-enhanced-realm
    enabled: true
    # Existing configurations (clients, users) would go here
    
    groups:
      - name: "admins"
        realmRoles:
          - "admin"
      - name: "viewers"

    userFederationProviders:
      - providerName: "ldap"
        config:
          # LDAP-specific configuration
          "bindDn": "cn=admin,dc=example,dc=org"
          "bindCredential": "password"
          "usersDn": "ou=users,dc=example,dc=org"
          "connectionUrl": "ldap://ldap.example.org"

    identityProviders:
      - alias: "google"
        providerId: "google"
        enabled: true
        config:
          "clientId": "your-google-client-id"
          "clientSecret": "your-google-client-secret"

    authenticationFlows:
      - alias: "My Custom Flow"
        providerId: "basic-flow"
        description: "A custom authentication flow"
        authenticationExecutions:
          - authenticator: "auth-username-password-form"
            requirement: "REQUIRED"
          - authenticator: "conditional-otp-form"
            requirement: "OPTIONAL"
            
    # Note: RealmSettings are top-level keys in the YAML
    accessTokenLifespan: 300
    ssoSessionIdleTimeout: 1800
    ```

2.  **Run the CLI to generate the JSON file:**
    ```bash
    kc-generate --input enhanced-realm.yaml --output enhanced-realm.json
    ```

3.  **Verify the output:**
    The `enhanced-realm.json` file will now contain configurations for groups, user federation, identity providers, and the custom authentication flow.
