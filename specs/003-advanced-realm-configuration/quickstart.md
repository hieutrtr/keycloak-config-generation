# Quickstart: Advanced Realm Configuration

This guide demonstrates how to use the newly added advanced realm configuration features.

## Prerequisites

*   The Keycloak Config Generation CLI must be installed.

## Usage

1.  **Create a YAML configuration file** (e.g., `production-realm.yaml`) with the new advanced sections:
    ```yaml
    realm: production-realm
    enabled: true

    # 1. Define all roles (realm and client)
    roles:
      - name: realm-admin
        description: "Administrator for the entire realm"
      - name: "my-app-user"
        description: "User role for my-app"
        clientRole: true # This role belongs to the 'my-app' client
      - name: composite-auditor
        description: "A composite role for auditing"
        composites:
          realm:
            - "realm-admin" # Inherits realm-admin
          client:
            my-app: # Inherits from the 'my-app' client
              - "my-app-user"

    # 2. Define Client Scopes
    clientScopes:
      - name: "custom-claims-scope"
        protocolMappers:
          - name: "Custom Claim Mapper"
            protocol: "openid-connect"
            protocolMapper: "oidc-usermodel-attribute-mapper"
            config:
              "user.attribute": "customAttribute"
              "claim.name": "custom_claim"
              "jsonType.label": "String"

    # 3. Define Clients and assign scopes
    clients:
      - clientId: my-app
        secret: "a-very-secure-secret"
        defaultClientScopes:
          - "custom-claims-scope" # Assign the scope here

    # 4. Set Default Flow Bindings
    browserFlow: "browser"
    registrationFlow: "registration"

    # 5. Configure Brute Force Protection
    bruteForceProtected: true
    maxFailureWaitSeconds: 900
    failureFactor: 30

    # 6. Configure Required Actions
    requiredActions:
      - alias: "UPDATE_PASSWORD"
        enabled: true
      - alias: "CONFIGURE_TOTP"
        enabled: true
        defaultAction: true

    # 7. Configure SMTP
    smtpServer:
      host: "smtp.example.com"
      port: 587
      from: "noreply@example.com"
      auth: "true"
      user: "keycloak-user"
      password: "smtp-password"

    # 8. Set advanced token lifespans
    ssoSessionMaxLifespans: 36000
    offlineSessionIdleTimeout: 2592000

    # 9. Configure Identity Providers with Mappers for account linking
    identityProviders:
      - alias: "google"
        providerId: "google"
        enabled: true
        config:
          "clientId": "your-google-client-id"
          "clientSecret": "your-google-client-secret"
        mappers:
          - name: "google-email-mapper"
            identityProviderMapper: "oidc-user-attribute-idp-mapper"
            config:
              "user.attribute": "email"
              "claim": "email"
              "syncMode": "FORCE"
    ```

2.  **Run the CLI to generate the JSON file:**
    ```bash
    kc-generate --input production-realm.yaml --output production-realm.json
    ```

3.  **Verify the output:**
    The `production-realm.json` file will now contain configurations for composite roles, client scopes, brute force protection, required actions, SMTP settings, and the other advanced features.
